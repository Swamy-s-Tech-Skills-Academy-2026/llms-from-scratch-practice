"""
Practice Examples: Sliding-Window Dataloader (Chapter 2)
=========================================================
Three-Layer Architecture — Layer 3: Practice

I'm practising the sliding-window dataset logic here. It took me a while to
internalize that input_ids and target_ids are the *same window* shifted by one
position. These examples walk through that intuition concretely.

Topics practised here:
  1. Manual sliding-window construction (no PyTorch — numbers only)
  2. The GPTDatasetV1 class re-implemented from memory
  3. DataLoader batch inspection
  4. Effect of stride on dataset size

Attribution: Concepts from *Build a Large Language Model From Scratch* (Raschka),
Chapter 2. Code is my own reconstruction for practice purposes.
"""

from __future__ import annotations

import torch
from torch.utils.data import DataLoader, Dataset


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------


def section(title: str) -> None:
    """Print a visible section header."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print("=" * 60)


# ---------------------------------------------------------------------------
# 1. Manual sliding window — integers only, no tokenizer
# ---------------------------------------------------------------------------


def example_manual_sliding_window() -> None:
    """Build input/target pairs by hand to see the pattern clearly.

    Why: Using integers instead of token IDs removes the tokenizer complexity
    so I can focus purely on the window/stride mechanic. Once this is clear,
    the GPTDatasetV1 class is just the same thing with real text.
    """
    section("1. Manual sliding window (integer sequences)")

    # Pretend these are token IDs
    token_ids = list(range(1, 13))  # [1, 2, 3, ..., 12]
    max_length = 4
    stride = 2

    print(f"Token IDs : {token_ids}")
    print(f"max_length: {max_length}  stride: {stride}")
    print()

    pairs: list[tuple[list[int], list[int]]] = []
    for i in range(0, len(token_ids) - max_length, stride):
        input_chunk = token_ids[i : i + max_length]
        # Target is always input shifted right by 1 — next-token prediction
        target_chunk = token_ids[i + 1 : i + max_length + 1]
        pairs.append((input_chunk, target_chunk))
        print(f"  window {i:2d}: input={input_chunk}  target={target_chunk}")

    print(f"\nTotal samples: {len(pairs)}")
    print("✓ Target is always input shifted right by 1")


# ---------------------------------------------------------------------------
# 2. GPTDatasetV1 — reconstructed from memory
# ---------------------------------------------------------------------------


class GPTDatasetV1(Dataset):
    """Sliding-window next-token-prediction dataset.

    Takes a flat list of token IDs and produces (input_ids, target_ids) pairs
    using a sliding window of size `max_length` with step `stride`.

    Why stride < max_length: Overlapping windows give more training samples
    and help the model see each token in multiple contexts.
    Why stride == max_length: No overlap — maximises independence between samples,
    useful when the dataset is huge and overlap is wasteful.
    """

    def __init__(
        self,
        token_ids: list[int],
        max_length: int,
        stride: int,
    ) -> None:
        self.input_ids: list[torch.Tensor] = []
        self.target_ids: list[torch.Tensor] = []

        for i in range(0, len(token_ids) - max_length, stride):
            self.input_ids.append(torch.tensor(token_ids[i : i + max_length]))
            self.target_ids.append(torch.tensor(token_ids[i + 1 : i + max_length + 1]))

    def __len__(self) -> int:
        return len(self.input_ids)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        return self.input_ids[idx], self.target_ids[idx]


def example_gpt_dataset() -> None:
    """Instantiate GPTDatasetV1 with a small integer sequence.

    Why: I want to confirm my re-implementation matches the expected
    output before plugging in a real tokenizer.
    """
    section("2. GPTDatasetV1 re-implementation")

    token_ids = list(range(1, 21))  # [1..20]
    max_length, stride = 4, 2

    dataset = GPTDatasetV1(token_ids, max_length=max_length, stride=stride)
    print(f"Dataset size: {len(dataset)} samples")

    # Inspect first 3 samples
    for idx in range(min(3, len(dataset))):
        x, y = dataset[idx]
        print(f"  sample[{idx}]: input={x.tolist()}  target={y.tolist()}")

    # Sanity check: target is input shifted right by 1
    x0, y0 = dataset[0]
    assert x0[1:].tolist() == y0[:-1].tolist(), "Shift invariant broken!"
    print("✓ Shift invariant confirmed: target = input[1:] + [next_token]")


# ---------------------------------------------------------------------------
# 3. DataLoader batch inspection
# ---------------------------------------------------------------------------


def example_dataloader_batch() -> None:
    """Wrap GPTDatasetV1 in a DataLoader and inspect one batch.

    Why: I always confuse tensor shapes when batching. This example makes
    the (batch_size, seq_len) shape concrete before I use the real text pipeline.
    """
    section("3. DataLoader batch inspection")

    token_ids = list(range(1, 101))  # 100 'tokens'
    max_length, stride, batch_size = 8, 4, 4

    dataset = GPTDatasetV1(token_ids, max_length=max_length, stride=stride)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False, drop_last=True)

    # Grab first batch
    x_batch, y_batch = next(iter(loader))

    print(f"x_batch shape: {x_batch.shape}")   # (batch_size, max_length)
    print(f"y_batch shape: {y_batch.shape}")
    print(f"\nx_batch:\n{x_batch}")
    print(f"\ny_batch:\n{y_batch}")

    assert x_batch.shape == (batch_size, max_length)
    assert y_batch.shape == (batch_size, max_length)
    print("\n✓ Shape assertions passed")


# ---------------------------------------------------------------------------
# 4. Effect of stride on dataset size
# ---------------------------------------------------------------------------


def example_stride_effect() -> None:
    """Show how stride controls the number of training samples.

    Why: Stride is a hyperparameter I need to tune consciously.
    Small stride → more samples, more overlap.
    Large stride → fewer samples, less overlap, faster epochs.
    """
    section("4. Effect of stride on dataset size")

    token_ids = list(range(1000))  # 1000 tokens
    max_length = 128

    print(f"Token sequence length: {len(token_ids)}")
    print(f"Window size (max_length): {max_length}")
    print()
    print(f"{'Stride':>8}  {'Samples':>8}  {'Overlap':>10}")
    print("-" * 32)

    for stride in [1, 16, 32, 64, 128]:
        dataset = GPTDatasetV1(token_ids, max_length=max_length, stride=stride)
        overlap = max_length - stride if stride < max_length else 0
        print(f"{stride:>8}  {len(dataset):>8}  {overlap:>10}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    print("Sliding-Window Dataloader Practice Examples — Chapter 2")
    example_manual_sliding_window()
    example_gpt_dataset()
    example_dataloader_batch()
    example_stride_effect()
    print("\nAll examples completed successfully.")
