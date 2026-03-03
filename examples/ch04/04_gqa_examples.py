def main():
    """
    Example script demonstrating the core math behind GQA vs MHA cache sizing.
    """
    batch_size = 1
    seq_len = 4096
    n_layers = 32
    emb_dim = 4096
    n_heads = 32
    head_dim = emb_dim // n_heads
    bytes_per_elem = 2  # standard for fp16 or bf16

    # Calculate base memory per head
    mem_per_head = batch_size * seq_len * head_dim * n_layers * 2 * bytes_per_elem

    # MHA: 32 Key/Value heads
    mha_mem = (mem_per_head * 32) / (1024**2)

    # GQA: Assuming 8 KV groups
    gqa_mem = (mem_per_head * 8) / (1024**2)

    print(f"--- MHA vs GQA Memory Cost at Seq_Len {seq_len} ---")
    print(f"MHA KV Cache: {mha_mem:,.2f} MB")
    print(f"GQA KV Cache: {gqa_mem:,.2f} MB")
    print(f"Memory Saved: {mha_mem - gqa_mem:,.2f} MB")


if __name__ == "__main__":
    main()
