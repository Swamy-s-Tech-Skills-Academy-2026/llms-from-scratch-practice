import torch
import torch.nn as nn
import time


def main():
    """
    Example script demonstrating the shell of a GPT layer.
    This fulfills the simulation/practice component of the 3-Layer Architecture.
    """
    print("Testing a single simple FeedForward network...\\n")

    # Define simple parameters
    emb_dim = 768
    
    # Implementing the FeedForward module directly in Python practice
    class FeedForward(nn.Module):
        def __init__(self, emb_dim):
            super().__init__()
            self.layers = nn.Sequential(
                nn.Linear(emb_dim, 4 * emb_dim),
                nn.GELU(),
                nn.Linear(4 * emb_dim, emb_dim)
            )

        def forward(self, x):
            return self.layers(x)
            
    # Initialize and mock tensor
    torch.manual_seed(42)
    ffn = FeedForward(emb_dim)
    
    # Imagine a sequence of 5 tokens in a batch of 2
    mock_input = torch.rand(2, 5, emb_dim)
    print(f"Shape of mock input (Batch, Seq_Len, Emb_Dim): {mock_input.shape}")
    
    start_time = time.time()
    mock_output = ffn(mock_input)
    end_time = time.time()
    
    print(f"Shape of FeedForward output: {mock_output.shape}")
    print(f"Processed in {(end_time - start_time) * 1000:.2f} ms")
    print("\\nThis perfectly preserves the tensor dimensions!")

if __name__ == "__main__":
    main()
