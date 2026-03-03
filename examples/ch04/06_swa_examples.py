import torch


def main():
    """
    Example script simulating Sliding Window masking logic.
    """
    seq_len = 8
    window_size = 3
    mask = torch.tril(torch.ones(seq_len, seq_len))

    for i in range(seq_len):
        mask[i, :max(0, i - window_size + 1)] = 0

    print("--- SWA Mask Example (W=3) ---")
    print(mask)
    print("\nNotice how elements outside the window are zeroed out!")


if __name__ == "__main__":
    main()
