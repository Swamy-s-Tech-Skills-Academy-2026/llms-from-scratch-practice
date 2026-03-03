import torch
import torch.nn as nn
import torch.nn.functional as F


def main():
    """
    Example script simulating a standard routing mechanism for MoE.
    """
    d_model = 32
    num_experts = 8
    top_k = 2

    # Simulate 1 token
    x = torch.randn(1, 1, d_model)
    router = nn.Linear(d_model, num_experts)

    logits = router(x)
    probs = F.softmax(logits, dim=-1)

    top_probs, top_indices = torch.topk(probs, top_k, dim=-1)

    print("--- MoE Router Example (8 Experts, Top-2 Routing) ---")
    print(f"Softmax Probabilities: {probs.squeeze().detach().numpy().round(3)}")
    print(f"Selected Expert Indices: {top_indices.squeeze().tolist()}")


if __name__ == "__main__":
    main()
