import torch
import torch.nn as nn


def main():
    """
    Example script demonstrating how to calculate basic parameter
    counts and memory footprint for a model block.
    """
    print("--- Performance Analysis Execution ---")

    class SimpleBlock(nn.Module):
        def __init__(self, d_model):
            super().__init__()
            self.linear1 = nn.Linear(d_model, d_model * 4)
            self.linear2 = nn.Linear(d_model * 4, d_model)

        def forward(self, x):
            return self.linear2(self.linear1(x))

    model = SimpleBlock(768)

    total_params = sum(p.numel() for p in model.parameters())

    print(f"Total Parameters: {total_params:,}")
    # 4 bytes per 32-bit float
    print(f"Estimated Weights VRAM: {total_params * 4 / (1024 ** 2):.2f} MB")


if __name__ == "__main__":
    main()
