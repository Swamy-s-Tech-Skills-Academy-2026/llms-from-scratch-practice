import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = [
    nbf.v4.new_markdown_cell('# Chapter 4: Practice Lab - Multi-Head Latent Attention (MLA)\n\nI want to calculate the theoretical memory savings of MLA caching vs standard MHA caching.'),
    nbf.v4.new_code_cell('print("Ready to analyze MLA compression!")'),
    nbf.v4.new_markdown_cell('## 1. Comparing Equations\n\n- **MHA Bytes:** `batch_size * seq_len * n_layers * emb_dim * 2 * bytes_per_elem`\n- **MLA Bytes:** `batch_size * seq_len * n_layers * latent_dim * bytes_per_elem`\n\nI will use dummy Llama parameters to benchmark the difference.'),
    nbf.v4.new_code_cell('''b_size = 1
seq = 4096
emb_dim = 4096
n_layers = 32
bytes_elem = 2 # fp16

# The magic compression integer
latent_dim = 512

# 1. Standard MHA Calculation
mha_total = b_size * seq * n_layers * emb_dim * 2 * bytes_elem
mha_mb = mha_total / (1024 ** 2)

# 2. MLA Calculation
mla_total = b_size * seq * n_layers * latent_dim * bytes_elem
mla_mb = mla_total / (1024 ** 2)

print(f"MHA KV Cache Storage: {mha_mb:,.2f} MB")
print(f"MLA Compressed Storage: {mla_mb:,.2f} MB")
print(f"Memory Saved: {mha_mb - mla_mb:,.2f} MB")'''),
    nbf.v4.new_markdown_cell('## Summary\n\nMy takeaway from this simulation: I effectively reduce the stored footprint from `2 * 4096` to just `512` per token. That is a massive 16x reduction in cache memory at the cost of a few extra linear projections at generation time!')
]
nb['cells'] = cells
with open('d:/STSA-2026/llms-from-scratch-practice/notebooks/ch04/05_mla-implementation.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print("MLA Notebook written")
