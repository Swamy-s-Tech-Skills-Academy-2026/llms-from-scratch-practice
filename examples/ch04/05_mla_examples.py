def main():
    """
    Example script showcasing the math for Multi-Head Latent Attention compression.
    """
    batch_size = 1
    seq_len = 4096
    n_layers = 32
    emb_dim = 4096
    bytes_per_elem = 2  # fp16
    latent_dim = 512

    # MHA Calculation (Stores K and V full embed dimensions)
    mha_bytes = batch_size * seq_len * n_layers * emb_dim * 2 * bytes_per_elem
    mha_mb = mha_bytes / (1024**2)

    # MLA Calculation (Stores compressed projection)
    mla_bytes = batch_size * seq_len * n_layers * latent_dim * bytes_per_elem
    mla_mb = mla_bytes / (1024**2)

    print("--- Memory Comparison: Standard MHA vs MLA ---")
    print(f"MHA Cost: {mha_mb:,.2f} MB")
    print(f"MLA Cost: {mla_mb:,.2f} MB")
    percentage = (mla_mb / mha_mb) * 100
    print(f"MLA uses only {percentage:.1f}% of the original cache memory!")


if __name__ == "__main__":
    main()
