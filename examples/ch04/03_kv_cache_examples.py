import torch


def main():
    """
    Example script capturing the core underlying logic of the KV Cache concatenation.
    It demonstrates how we avoid recomputing entire sequence histories.
    """
    print("--- KV Cache Array Shape Management ---\\n")

    torch.manual_seed(42)

    # Let's say batch=1, seq_len=4 (current context), head_dim=64
    k_history = torch.randn(1, 4, 64)
    v_history = torch.randn(1, 4, 64)

    print(f"Current K Cache shape: {k_history.shape}")

    # Generating the new 5th token, producing 1 new vector for K and V
    k_new_token = torch.randn(1, 1, 64)
    v_new_token = torch.randn(1, 1, 64)

    # The KV Cache algorithm:
    # Instead of recalculating all 5, just append the 1 new one to the existing 4.
    updated_k_cache = torch.cat((k_history, k_new_token), dim=1)
    updated_v_cache = torch.cat((v_history, v_new_token), dim=1)

    print(
        f"Updated K Cache shape (after dim=1 concat): {updated_k_cache.shape}")
    print("\\nSuccess! This structure avoids quadratic recalculation.")


if __name__ == "__main__":
    main()
