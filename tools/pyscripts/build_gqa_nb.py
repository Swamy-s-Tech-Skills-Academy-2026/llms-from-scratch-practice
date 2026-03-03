import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = [
    nbf.v4.new_markdown_cell('# Chapter 4: Practice Lab - Grouped-Query Attention (GQA)\n\nI want to see the exact memory differences conceptually between Multi-Head Attention (MHA) and Grouped-Query Attention (GQA) when caching keys and values.'),
    nbf.v4.new_code_cell('import math\nprint("Ready for GQA Analysis!")'),
    nbf.v4.new_markdown_cell('## 1. Defining the Equation\n\nI learned that KV Cache Size follows this formula:\n`bytes = batch_size * seq_len * head_dim * n_layers * 2 (K&V) * bytes_per_elem * kv_heads`'),
    nbf.v4.new_code_cell('''def calc_kv_cache_mb(batch_size, seq_len, head_dim, n_layers, bytes_per_elem, kv_heads):
    total_bytes = batch_size * seq_len * head_dim * n_layers * 2 * bytes_per_elem * kv_heads
    return total_bytes / (1024 ** 2)

# Llama 2 7B proxy numbers
b_size = 1
seq = 4096
emb_dim = 4096
n_heads = 32
n_layers = 32
bytes_elem = 2 # fp16
h_dim = emb_dim // n_heads'''),
    nbf.v4.new_markdown_cell('## 2. Comparing MHA to GQA\n\nMHA has 32 KV heads. GQA (say, with 8 groups) has only 8 KV heads.'),
    nbf.v4.new_code_cell('''# MHA
mha_mb = calc_kv_cache_mb(b_size, seq, h_dim, n_layers, bytes_elem, kv_heads=32)
print(f"Standard MHA KV Cache Size: {mha_mb:.2f} MB")

# GQA
gqa_mb = calc_kv_cache_mb(b_size, seq, h_dim, n_layers, bytes_elem, kv_heads=8)
print(f"GQA (8 groups) KV Cache Size: {gqa_mb:.2f} MB")
print(f"Memory Saved: {mha_mb - gqa_mb:.2f} MB ({100 - (gqa_mb/mha_mb)*100:.1f}%)")''')
]
nb['cells'] = cells
with open('d:/STSA-2026/llms-from-scratch-practice/notebooks/ch04/04_gqa-implementation.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print("Notebook written")
