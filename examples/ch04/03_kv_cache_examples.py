import torch


def main():
    """
    Example script capturing the core logic of the KV Cache concat.
    Demonstrates how we avoid recomputing entire sequence histories.
    """
    print("--- KV Cache Array Shape Management ---\n")

    torch.manual_seed(42)

    k_history = torch.randn(1, 4, 64)
    v_history = torch.randn(1, 4, 64)

    print(f"Current K Cache shape: {k_history.shape}")

    k_new_token = torch.randn(1, 1, 64)
    v_new_token = torch.randn(1, 1, 64)

    updated_k_cache = torch.cat((k_history, k_new_token), dim=1)
    updated_v_cache = torch.cat((v_history, v_new_token), dim=1)

    print(f"Updated K shape (after dim=1 concat): {updated_k_cache.shape}")
    print(f"Updated V shape: {updated_v_cache.shape}")
    print("\nSuccess! This structure avoids quadratic recalculation.")


if __name__ == "__main__":
    main()
