import torch
import torch.nn as nn


def main():
    """
    Example script demonstrating the core Gating principle in DeltaNet.
    """
    d_in = 16
    d_out = 16
    x = torch.randn(1, 1, d_in)

    query_layer = nn.Linear(d_in, d_out)
    gate_layer = nn.Linear(d_in, d_out)

    q = query_layer(x)
    gate = torch.sigmoid(gate_layer(x))

    gated_q = q * gate

    print("--- Gated Attention Demo ---")
    print(f"Original Q snippet (first 3): {q.squeeze()[:3].detach().numpy()}")
    print(f"Gate scalar multiplier: {gate.squeeze()[:3].detach().numpy()}")
    print(f"Gated Q outcome: {gated_q.squeeze()[:3].detach().numpy()}")


if __name__ == "__main__":
    main()
