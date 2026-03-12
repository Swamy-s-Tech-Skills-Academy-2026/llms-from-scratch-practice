"""Inference and capacity variants synthesized from the Chapter 4 bonus topics."""

from __future__ import annotations

import math

import torch
import torch.nn as nn
from torch import Tensor

from .ch04_core import GELU, GPTConfig


def estimate_mha_kv_cache_bytes(
    batch_size: int,
    seq_len: int,
    emb_dim: int,
    n_layers: int,
    n_heads: int,
    bytes_per_element: int,
) -> int:
    """Estimate total KV-cache size for standard multi-head attention."""

    head_dim = emb_dim // n_heads
    per_layer = batch_size * seq_len * n_heads * head_dim * 2 * bytes_per_element
    return per_layer * n_layers


def estimate_gqa_kv_cache_bytes(
    batch_size: int,
    seq_len: int,
    emb_dim: int,
    n_layers: int,
    n_kv_groups: int,
    n_heads: int,
    bytes_per_element: int,
) -> int:
    """Estimate cache size when multiple query heads share KV heads."""

    head_dim = emb_dim // n_heads
    per_layer = batch_size * seq_len * n_kv_groups * head_dim * 2 * bytes_per_element
    return per_layer * n_layers


def estimate_mla_kv_cache_bytes(
    batch_size: int,
    seq_len: int,
    latent_dim: int,
    n_layers: int,
    bytes_per_element: int,
) -> int:
    """Estimate cache size when only the latent projection is stored."""

    return batch_size * seq_len * latent_dim * n_layers * bytes_per_element


def estimate_swa_kv_cache_bytes(
    batch_size: int,
    window_size: int,
    emb_dim: int,
    n_layers: int,
    n_heads: int,
    bytes_per_element: int,
) -> int:
    """Estimate cache size when attention remembers only a fixed window."""

    return estimate_mha_kv_cache_bytes(
        batch_size=batch_size,
        seq_len=window_size,
        emb_dim=emb_dim,
        n_layers=n_layers,
        n_heads=n_heads,
        bytes_per_element=bytes_per_element,
    )


def estimate_deltanet_state_bytes(
    batch_size: int,
    emb_dim: int,
    n_layers: int,
    n_heads: int,
    bytes_per_element: int,
) -> int:
    """Estimate the recurrent state size for a linear-attention DeltaNet-style layer."""

    head_dim = emb_dim // n_heads
    per_layer = batch_size * n_heads * head_dim * head_dim * bytes_per_element
    return per_layer * n_layers


class CachedCausalSelfAttention(nn.Module):
    """Decoder attention that reuses past keys and values during generation."""

    def __init__(self, config: GPTConfig) -> None:
        super().__init__()
        if config.emb_dim % config.n_heads != 0:
            raise ValueError("emb_dim must be divisible by n_heads")

        self.emb_dim = config.emb_dim
        self.n_heads = config.n_heads
        self.head_dim = config.emb_dim // config.n_heads
        self.query = nn.Linear(config.emb_dim, config.emb_dim, bias=config.qkv_bias)
        self.key = nn.Linear(config.emb_dim, config.emb_dim, bias=config.qkv_bias)
        self.value = nn.Linear(config.emb_dim, config.emb_dim, bias=config.qkv_bias)
        self.out_proj = nn.Linear(config.emb_dim, config.emb_dim)
        self.dropout = nn.Dropout(config.drop_rate)
        self.register_buffer("cache_k", None, persistent=False)
        self.register_buffer("cache_v", None, persistent=False)
        self.current_position = 0

    def _reshape(self, x: Tensor) -> Tensor:
        batch_size, seq_len, _ = x.shape
        return x.view(batch_size, seq_len, self.n_heads, self.head_dim).transpose(1, 2)

    def reset_cache(self) -> None:
        self.cache_k = None
        self.cache_v = None
        self.current_position = 0

    def forward(self, x: Tensor, use_cache: bool = False) -> Tensor:
        batch_size, seq_len, _ = x.shape
        queries = self._reshape(self.query(x))
        keys_new = self._reshape(self.key(x))
        values_new = self._reshape(self.value(x))

        if use_cache:
            if self.cache_k is None:
                self.cache_k = keys_new
                self.cache_v = values_new
            else:
                self.cache_k = torch.cat((self.cache_k, keys_new), dim=2)
                self.cache_v = torch.cat((self.cache_v, values_new), dim=2)
            keys = self.cache_k
            values = self.cache_v
            q_positions = torch.arange(
                self.current_position,
                self.current_position + seq_len,
                device=x.device,
            )
            self.current_position += seq_len
        else:
            keys = keys_new
            values = values_new
            q_positions = torch.arange(seq_len, device=x.device)
            self.current_position = 0

        k_positions = torch.arange(keys.shape[-2], device=x.device)
        mask = q_positions.unsqueeze(-1) < k_positions.unsqueeze(0)

        attn_scores = queries @ keys.transpose(2, 3)
        attn_scores = attn_scores.masked_fill(mask, -torch.inf)
        attn_weights = torch.softmax(attn_scores / math.sqrt(self.head_dim), dim=-1)
        attn_weights = self.dropout(attn_weights)

        context = (attn_weights @ values).transpose(1, 2).contiguous()
        context = context.view(batch_size, seq_len, self.emb_dim)
        return self.out_proj(context)


class GroupedQueryAttention(nn.Module):
    """Attention variant where query heads share fewer KV heads."""

    def __init__(
        self,
        emb_dim: int,
        n_heads: int,
        n_kv_groups: int,
        dropout: float = 0.0,
        qkv_bias: bool = False,
    ) -> None:
        super().__init__()
        if emb_dim % n_heads != 0:
            raise ValueError("emb_dim must be divisible by n_heads")
        if n_heads % n_kv_groups != 0:
            raise ValueError("n_heads must be divisible by n_kv_groups")

        self.emb_dim = emb_dim
        self.n_heads = n_heads
        self.n_kv_groups = n_kv_groups
        self.group_size = n_heads // n_kv_groups
        self.head_dim = emb_dim // n_heads
        kv_dim = n_kv_groups * self.head_dim

        self.query = nn.Linear(emb_dim, emb_dim, bias=qkv_bias)
        self.key = nn.Linear(emb_dim, kv_dim, bias=qkv_bias)
        self.value = nn.Linear(emb_dim, kv_dim, bias=qkv_bias)
        self.out_proj = nn.Linear(emb_dim, emb_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: Tensor) -> Tensor:
        batch_size, seq_len, _ = x.shape
        queries = (
            self.query(x).view(batch_size, seq_len, self.n_heads, self.head_dim).transpose(1, 2)
        )
        keys = (
            self.key(x).view(batch_size, seq_len, self.n_kv_groups, self.head_dim).transpose(1, 2)
        )
        values = (
            self.value(x).view(batch_size, seq_len, self.n_kv_groups, self.head_dim).transpose(1, 2)
        )

        keys = keys.repeat_interleave(self.group_size, dim=1)
        values = values.repeat_interleave(self.group_size, dim=1)

        causal_mask = torch.triu(torch.ones(seq_len, seq_len, device=x.device), diagonal=1).bool()
        attn_scores = queries @ keys.transpose(2, 3)
        attn_scores = attn_scores.masked_fill(causal_mask, -torch.inf)
        attn_weights = torch.softmax(attn_scores / math.sqrt(self.head_dim), dim=-1)
        attn_weights = self.dropout(attn_weights)

        context = (attn_weights @ values).transpose(1, 2).contiguous()
        context = context.view(batch_size, seq_len, self.emb_dim)
        return self.out_proj(context)


class MultiHeadLatentAttention(nn.Module):
    """Attention variant that stores a compressed latent KV representation."""

    def __init__(
        self,
        emb_dim: int,
        n_heads: int,
        latent_dim: int,
        dropout: float = 0.0,
        qkv_bias: bool = False,
    ) -> None:
        super().__init__()
        if emb_dim % n_heads != 0:
            raise ValueError("emb_dim must be divisible by n_heads")

        self.emb_dim = emb_dim
        self.n_heads = n_heads
        self.head_dim = emb_dim // n_heads
        self.latent_dim = latent_dim
        self.query = nn.Linear(emb_dim, emb_dim, bias=qkv_bias)
        self.down_proj = nn.Linear(emb_dim, latent_dim, bias=qkv_bias)
        self.up_key = nn.Linear(latent_dim, emb_dim, bias=qkv_bias)
        self.up_value = nn.Linear(latent_dim, emb_dim, bias=qkv_bias)
        self.out_proj = nn.Linear(emb_dim, emb_dim)
        self.dropout = nn.Dropout(dropout)
        self.register_buffer("latent_cache", None, persistent=False)
        self.current_position = 0

    def reset_cache(self) -> None:
        self.latent_cache = None
        self.current_position = 0

    def _reshape(self, x: Tensor) -> Tensor:
        batch_size, seq_len, _ = x.shape
        return x.view(batch_size, seq_len, self.n_heads, self.head_dim).transpose(1, 2)

    def forward(self, x: Tensor, use_cache: bool = False) -> Tensor:
        batch_size, seq_len, _ = x.shape
        queries = self._reshape(self.query(x))
        latent_new = self.down_proj(x)

        if use_cache:
            if self.latent_cache is None:
                self.latent_cache = latent_new
            else:
                self.latent_cache = torch.cat((self.latent_cache, latent_new), dim=1)
            latent_total = self.latent_cache
            q_positions = torch.arange(
                self.current_position,
                self.current_position + seq_len,
                device=x.device,
            )
            self.current_position += seq_len
        else:
            latent_total = latent_new
            q_positions = torch.arange(seq_len, device=x.device)
            self.current_position = 0

        keys = self._reshape(self.up_key(latent_total))
        values = self._reshape(self.up_value(latent_total))
        k_positions = torch.arange(keys.shape[-2], device=x.device)
        mask = q_positions.unsqueeze(-1) < k_positions.unsqueeze(0)

        attn_scores = queries @ keys.transpose(2, 3)
        attn_scores = attn_scores.masked_fill(mask, -torch.inf)
        attn_weights = torch.softmax(attn_scores / math.sqrt(self.head_dim), dim=-1)
        attn_weights = self.dropout(attn_weights)

        context = (attn_weights @ values).transpose(1, 2).contiguous()
        context = context.view(batch_size, seq_len, self.emb_dim)
        return self.out_proj(context)


class SlidingWindowSelfAttention(CachedCausalSelfAttention):
    """Cached self-attention that retains only the most recent window of tokens."""

    def __init__(self, config: GPTConfig, window_size: int) -> None:
        super().__init__(config)
        self.window_size = window_size

    def forward(self, x: Tensor, use_cache: bool = False) -> Tensor:
        batch_size, seq_len, _ = x.shape
        queries = self._reshape(self.query(x))
        keys_new = self._reshape(self.key(x))
        values_new = self._reshape(self.value(x))

        if use_cache:
            if self.cache_k is None:
                self.cache_k = keys_new
                self.cache_v = values_new
            else:
                self.cache_k = torch.cat((self.cache_k, keys_new), dim=2)
                self.cache_v = torch.cat((self.cache_v, values_new), dim=2)
            self.cache_k = self.cache_k[:, :, -self.window_size :, :]
            self.cache_v = self.cache_v[:, :, -self.window_size :, :]
            keys = self.cache_k
            values = self.cache_v
            k_len = keys.shape[-2]
            q_positions = torch.arange(
                self.current_position,
                self.current_position + seq_len,
                device=x.device,
            )
            k_start = max(0, self.current_position + seq_len - k_len)
            k_positions = torch.arange(k_start, k_start + k_len, device=x.device)
            self.current_position += seq_len
        else:
            keys = keys_new
            values = values_new
            q_positions = torch.arange(seq_len, device=x.device)
            k_positions = torch.arange(seq_len, device=x.device)
            self.current_position = 0

        distance = q_positions.unsqueeze(-1) - k_positions.unsqueeze(0)
        mask = (distance < 0) | (distance >= self.window_size)

        attn_scores = queries @ keys.transpose(2, 3)
        attn_scores = attn_scores.masked_fill(mask, -torch.inf)
        attn_weights = torch.softmax(attn_scores / math.sqrt(self.head_dim), dim=-1)
        attn_weights = self.dropout(attn_weights)

        context = (attn_weights @ values).transpose(1, 2).contiguous()
        context = context.view(batch_size, seq_len, self.emb_dim)
        return self.out_proj(context)


class SparseMoEFeedForward(nn.Module):
    """Top-k routed mixture-of-experts feed-forward block."""

    def __init__(self, emb_dim: int, hidden_dim: int, num_experts: int, top_k: int) -> None:
        super().__init__()
        if top_k <= 0 or top_k > num_experts:
            raise ValueError("top_k must be between 1 and num_experts")

        self.emb_dim = emb_dim
        self.num_experts = num_experts
        self.top_k = top_k
        self.router = nn.Linear(emb_dim, num_experts, bias=False)
        self.experts = nn.ModuleList(
            [
                nn.Sequential(
                    nn.Linear(emb_dim, hidden_dim),
                    GELU(),
                    nn.Linear(hidden_dim, emb_dim),
                )
                for _ in range(num_experts)
            ]
        )

    def forward(self, x: Tensor) -> Tensor:
        batch_size, seq_len, emb_dim = x.shape
        flat_x = x.reshape(batch_size * seq_len, emb_dim)
        logits = self.router(flat_x)
        top_values, top_indices = torch.topk(logits, self.top_k, dim=-1)
        top_weights = torch.softmax(top_values, dim=-1)

        mixed_output = torch.zeros_like(flat_x)
        for slot in range(self.top_k):
            expert_indices = top_indices[:, slot]
            slot_weights = top_weights[:, slot]
            for expert_id in range(self.num_experts):
                token_mask = expert_indices == expert_id
                if not torch.any(token_mask):
                    continue
                expert_input = flat_x[token_mask]
                expert_output = self.experts[expert_id](expert_input)
                mixed_output[token_mask] += expert_output * slot_weights[token_mask].unsqueeze(-1)

        return mixed_output.view(batch_size, seq_len, emb_dim)
