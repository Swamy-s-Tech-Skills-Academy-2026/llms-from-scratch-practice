"""
Practice Examples: Tokenization (Chapter 2)
============================================
Three-Layer Architecture — Layer 3: Practice

I'm writing these examples to consolidate my understanding of tokenization.
The goal is to be able to rattle off these patterns from memory, not just run
them once and forget.

Topics practised here:
  1. Basic tiktoken encoding / decoding
  2. Handling special tokens
  3. Vocabulary inspection
  4. BPE sub-word splitting intuition
  5. Comparing tokenisation across different strings

Attribution: Concepts from *Build a Large Language Model From Scratch* (Raschka),
Chapter 2. Code is my own reconstruction for practice purposes.
"""

from __future__ import annotations

import tiktoken


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------


def section(title: str) -> None:
    """Print a visible section header."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print("=" * 60)


# ---------------------------------------------------------------------------
# 1. Basic encode / decode round-trip
# ---------------------------------------------------------------------------


def example_basic_encode_decode() -> None:
    """Encode text → token IDs, then decode back to text.

    Why: The model never sees raw text; it sees integers. Being able to
    move between text and IDs fluently is fundamental.
    """
    section("1. Basic encode / decode round-trip")

    tokenizer = tiktoken.get_encoding("gpt2")

    text = "Hello, world! This is a tokenization example."
    token_ids: list[int] = tokenizer.encode(text)
    decoded: str = tokenizer.decode(token_ids)

    print(f"Input  : {text!r}")
    print(f"IDs    : {token_ids}")
    print(f"Decoded: {decoded!r}")
    print(f"Tokens : {len(token_ids)}")

    # Key observation: decoded text should match input exactly
    assert decoded == text, "Round-trip failed — something unexpected happened!"
    print("✓ Round-trip assertion passed")


# ---------------------------------------------------------------------------
# 2. Inspecting individual tokens
# ---------------------------------------------------------------------------


def example_inspect_tokens() -> None:
    """Decode each token ID individually to see sub-word units.

    Why: This makes BPE tangible — you can see exactly how the tokenizer
    splits compound words, contractions, and punctuation.
    """
    section("2. Inspecting individual tokens")

    tokenizer = tiktoken.get_encoding("gpt2")

    # Interesting cases: compound words and contractions
    words = ["unhappiness", "tokenization", "don't", "GPT-2", "2024"]
    for word in words:
        ids = tokenizer.encode(word)
        pieces = [tokenizer.decode([i]) for i in ids]
        print(f"  {word!r:20s} → {ids}  {pieces}")

    # My takeaway: GPT-2 BPE often keeps common words as one token,
    # but splits rare or compound words into multiple pieces.


# ---------------------------------------------------------------------------
# 3. Special tokens
# ---------------------------------------------------------------------------


def example_special_tokens() -> None:
    """Encode text that includes the <|endoftext|> boundary token.

    Why: GPT-2 uses <|endoftext|> to signal document boundaries during
    training. Without allowed_special={'<|endoftext|>'} tiktoken raises
    an error — I burned time debugging this once.
    """
    section("3. Special tokens")

    tokenizer = tiktoken.get_encoding("gpt2")

    text = "First document.<|endoftext|>Second document."
    ids = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
    print(f"Text : {text!r}")
    print(f"IDs  : {ids}")
    print(f"<|endoftext|> token ID: {tokenizer.eot_token}")

    # The special token should appear exactly once in the middle
    assert tokenizer.eot_token in ids
    print("✓ Special token present in encoded output")


# ---------------------------------------------------------------------------
# 4. Vocabulary size
# ---------------------------------------------------------------------------


def example_vocabulary_size() -> None:
    """Check GPT-2 vocabulary size and look up a token ID by string.

    Why: Vocabulary size determines the embedding table shape. For GPT-2
    it's 50,257 — this number will appear repeatedly in model code.
    """
    section("4. Vocabulary size")

    tokenizer = tiktoken.get_encoding("gpt2")

    vocab_size: int = tokenizer.n_vocab
    print(f"GPT-2 vocabulary size: {vocab_size:,}")
    # Should print 50,257
    assert vocab_size == 50_257

    # What ID does the word 'the' get?
    the_id = tokenizer.encode(" the")  # note the leading space matters in BPE
    print(f"Token ID for ' the': {the_id}")


# ---------------------------------------------------------------------------
# 5. Token count varies with phrasing
# ---------------------------------------------------------------------------


def example_token_count_comparison() -> None:
    """Show that phrasing affects token count — useful for prompt engineering.

    Why: Token count determines context window usage and compute cost.
    Knowing how phrasing affects it helps me write more efficient prompts.
    """
    section("5. Token count comparison")

    tokenizer = tiktoken.get_encoding("gpt2")

    phrases = [
        "The quick brown fox",
        "the quick brown fox",  # lowercase
        "TheQuickBrownFox",     # camelCase — likely more tokens
        "T h e q u i c k",     # spaced — many more tokens
    ]

    for phrase in phrases:
        n = len(tokenizer.encode(phrase))
        print(f"  {n:3d} tokens | {phrase!r}")

    # My observation: lowercase and title-case often differ by only 1 token;
    # camelCase and spaced-out text produce many more tokens.


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    print("Tokenization Practice Examples — Chapter 2")
    example_basic_encode_decode()
    example_inspect_tokens()
    example_special_tokens()
    example_vocabulary_size()
    example_token_count_comparison()
    print("\nAll examples completed successfully.")
