"""Core GPT components synthesized from the Chapter 4 learning materials."""

from __future__ import annotations

from dataclasses import dataclass

import torch
import torch.nn as nn
from torch import Tensor


@dataclass(slots=True)
class GPTConfig:
    """Minimal GPT configuration used by the learner-owned Chapter 4 modules."""

    vocab_size: int
    context_length: int
    emb_dim: int
    n_heads: int
    n_layers: int
    drop_rate: float = 0.0
    qkv_bias: bool = False
    ff_mult: int = 4


class LayerNorm(nn.Module):
    """Feature-wise normalization used throughout the transformer stack."""

    def __init__(self, emb_dim: int, eps: float = 1e-5) -> None:
        super().__init__()
        self.eps = eps
        self.scale = nn.Parameter(torch.ones(emb_dim))
        self.shift = nn.Parameter(torch.zeros(emb_dim))

    def forward(self, x: Tensor) -> Tensor:
        mean = x.mean(dim=-1, keepdim=True)
        variance = x.var(dim=-1, keepdim=True, unbiased=False)
        normalized = (x - mean) / torch.sqrt(variance + self.eps)
        return self.scale * normalized + self.shift


class GELU(nn.Module):
    """Activation used in GPT-style feed-forward blocks."""

    def forward(self, x: Tensor) -> Tensor:
        return torch.nn.functional.gelu(x)


class FeedForward(nn.Module):
    """Two-layer MLP block that expands and then compresses token features."""

    def __init__(self, config: GPTConfig) -> None:
        super().__init__()
        hidden_dim = config.ff_mult * config.emb_dim
        self.layers = nn.Sequential(
            nn.Linear(config.emb_dim, hidden_dim),
            GELU(),
            nn.Linear(hidden_dim, config.emb_dim),
        )

    def forward(self, x: Tensor) -> Tensor:
        return self.layers(x)


class CausalSelfAttention(nn.Module):
    """Standard masked multi-head self-attention for decoder-only models."""

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
        self.register_buffer(
            "causal_mask",
            torch.triu(torch.ones(config.context_length, config.context_length), diagonal=1).bool(),
            persistent=False,
        )

    def _reshape(self, x: Tensor) -> Tensor:
        batch_size, seq_len, _ = x.shape
        return x.view(batch_size, seq_len, self.n_heads, self.head_dim).transpose(1, 2)

    def forward(self, x: Tensor) -> Tensor:
        batch_size, seq_len, _ = x.shape
        queries = self._reshape(self.query(x))
        keys = self._reshape(self.key(x))
        values = self._reshape(self.value(x))

        attn_scores = queries @ keys.transpose(2, 3)
        mask = self.causal_mask[:seq_len, :seq_len]
        attn_scores = attn_scores.masked_fill(mask, -torch.inf)

        attn_weights = torch.softmax(attn_scores / self.head_dim**0.5, dim=-1)
        attn_weights = self.dropout(attn_weights)

        context = (attn_weights @ values).transpose(1, 2).contiguous()
        context = context.view(batch_size, seq_len, self.emb_dim)
        return self.out_proj(context)


class TransformerBlock(nn.Module):
    """Pre-norm transformer block with residual connections."""

    def __init__(self, config: GPTConfig) -> None:
        super().__init__()
        self.attention = CausalSelfAttention(config)
        self.feed_forward = FeedForward(config)
        self.norm1 = LayerNorm(config.emb_dim)
        self.norm2 = LayerNorm(config.emb_dim)
        self.dropout = nn.Dropout(config.drop_rate)

    def forward(self, x: Tensor) -> Tensor:
        x = x + self.dropout(self.attention(self.norm1(x)))
        x = x + self.dropout(self.feed_forward(self.norm2(x)))
        return x


class GPTModel(nn.Module):
    """Compact decoder-only GPT assembled from learner-owned components."""

    def __init__(self, config: GPTConfig) -> None:
        super().__init__()
        self.config = config
        self.token_embedding = nn.Embedding(config.vocab_size, config.emb_dim)
        self.position_embedding = nn.Embedding(config.context_length, config.emb_dim)
        self.embedding_dropout = nn.Dropout(config.drop_rate)
        self.blocks = nn.ModuleList([TransformerBlock(config) for _ in range(config.n_layers)])
        self.final_norm = LayerNorm(config.emb_dim)
        self.output_head = nn.Linear(config.emb_dim, config.vocab_size, bias=False)

    def forward(self, token_indices: Tensor) -> Tensor:
        _, seq_len = token_indices.shape
        if seq_len > self.config.context_length:
            raise ValueError("Input sequence exceeds configured context length")

        positions = torch.arange(seq_len, device=token_indices.device)
        x = self.token_embedding(token_indices) + self.position_embedding(positions)
        x = self.embedding_dropout(x)

        for block in self.blocks:
            x = block(x)

        x = self.final_norm(x)
        return self.output_head(x)


def generate_greedy(model: GPTModel, token_indices: Tensor, max_new_tokens: int) -> Tensor:
    """Generate tokens by repeatedly selecting the highest-logit next token."""

    generated = token_indices
    context_length = model.config.context_length

    for _ in range(max_new_tokens):
        context = generated[:, -context_length:]
        with torch.no_grad():
            logits = model(context)
        next_token = logits[:, -1, :].argmax(dim=-1, keepdim=True)
        generated = torch.cat((generated, next_token), dim=1)

    return generated