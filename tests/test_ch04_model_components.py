"""Tests for learner-owned Chapter 4 reusable modules."""

import torch

from src.model import (
    CachedCausalSelfAttention,
    GPTConfig,
    GPTModel,
    GroupedQueryAttention,
    MultiHeadLatentAttention,
    SlidingWindowSelfAttention,
    SparseMoEFeedForward,
    estimate_deltanet_state_bytes,
    estimate_gqa_kv_cache_bytes,
    estimate_mha_kv_cache_bytes,
    estimate_mla_kv_cache_bytes,
    estimate_swa_kv_cache_bytes,
    generate_greedy,
)


def tiny_config() -> GPTConfig:
    return GPTConfig(
        vocab_size=64,
        context_length=16,
        emb_dim=32,
        n_heads=4,
        n_layers=2,
        drop_rate=0.0,
    )


def test_gpt_model_forward_shape() -> None:
    config = tiny_config()
    model = GPTModel(config)
    token_indices = torch.randint(0, config.vocab_size, (2, 8))
    logits = model(token_indices)
    assert logits.shape == (2, 8, config.vocab_size)


def test_cached_attention_preserves_shape() -> None:
    config = tiny_config()
    attention = CachedCausalSelfAttention(config)
    x_first = torch.randn(1, 4, config.emb_dim)
    x_second = torch.randn(1, 1, config.emb_dim)

    first_context = attention(x_first, use_cache=True)
    second_context = attention(x_second, use_cache=True)

    assert first_context.shape == (1, 4, config.emb_dim)
    assert second_context.shape == (1, 1, config.emb_dim)


def test_grouped_query_attention_shape() -> None:
    attention = GroupedQueryAttention(emb_dim=32, n_heads=4, n_kv_groups=2)
    x = torch.randn(2, 6, 32)
    context = attention(x)
    assert context.shape == (2, 6, 32)


def test_mla_shape() -> None:
    attention = MultiHeadLatentAttention(emb_dim=32, n_heads=4, latent_dim=8)
    x = torch.randn(2, 5, 32)
    context = attention(x)
    assert context.shape == (2, 5, 32)


def test_sliding_window_attention_shape() -> None:
    attention = SlidingWindowSelfAttention(tiny_config(), window_size=4)
    x = torch.randn(1, 3, 32)
    context = attention(x, use_cache=True)
    assert context.shape == (1, 3, 32)


def test_sparse_moe_shape() -> None:
    moe = SparseMoEFeedForward(emb_dim=32, hidden_dim=64, num_experts=4, top_k=2)
    x = torch.randn(2, 5, 32)
    out = moe(x)
    assert out.shape == x.shape


def test_memory_estimators_have_expected_ordering() -> None:
    mha_bytes = estimate_mha_kv_cache_bytes(1, 128, 32, 2, 4, 2)
    gqa_bytes = estimate_gqa_kv_cache_bytes(1, 128, 32, 2, 2, 4, 2)
    mla_bytes = estimate_mla_kv_cache_bytes(1, 128, 8, 2, 2)
    swa_bytes = estimate_swa_kv_cache_bytes(1, 32, 32, 2, 4, 2)
    deltanet_bytes = estimate_deltanet_state_bytes(1, 32, 2, 4, 2)

    assert gqa_bytes < mha_bytes
    assert mla_bytes < mha_bytes
    assert swa_bytes < mha_bytes
    assert deltanet_bytes > 0


def test_generate_greedy_output_length() -> None:
    config = tiny_config()
    model = GPTModel(config)
    model.eval()
    prompt = torch.randint(0, config.vocab_size, (1, 3))
    max_new = 5
    output = generate_greedy(model, prompt, max_new_tokens=max_new)
    # Output should be the prompt tokens plus max_new_tokens new tokens
    assert output.shape == (1, 3 + max_new)
