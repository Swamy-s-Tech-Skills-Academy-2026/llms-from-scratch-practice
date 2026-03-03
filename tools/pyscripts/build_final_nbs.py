import nbformat as nbf

def build_swa():
    nb = nbf.v4.new_notebook()
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# Chapter 4: Practice Lab - Sliding Window Attention\n\nI want to visualize the constraints of SWA vs Global Attention by creating dummy attention score matrices.'),
        nbf.v4.new_code_cell('import torch\nimport matplotlib.pyplot as plt\n\n# Ensures reproducibility\ntorch.manual_seed(42)\nprint("Ready for SWA Visualization!")'),
        nbf.v4.new_markdown_cell('## Creating the Mask\n\nUnlike global attention where the lower triangle is all `1`s, I will restrict the `1`s to only the last $W$ tokens.'),
        nbf.v4.new_code_cell('''seq_len = 10
window_size = 3

# Start with standard autoregressive lower triangular mask
mask = torch.tril(torch.ones(seq_len, seq_len))

# Apply the sliding window
for i in range(seq_len):
    # Zero out anything older than the window
    mask[i, :max(0, i - window_size + 1)] = 0

fig, ax = plt.subplots(figsize=(5,5))
ax.imshow(mask, cmap="viridis")
ax.set_title(f"Sliding Window Attention Mask (W={window_size})")
plt.show()'''),
        nbf.v4.new_markdown_cell('My takeaway: Only the sequence elements hitting the green diagonal band will be loaded into the KV Cache during forward passes. This puts a hard ceiling on memory!')
    ]
    with open('d:/STSA-2026/llms-from-scratch-practice/notebooks/ch04/06_swa-implementation.ipynb', 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

def build_moe():
    nb = nbf.v4.new_notebook()
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# Chapter 4: Practice Lab - Mixture of Experts\n\nI will create a dummy `Router` to see how tokens actually get steered to sparse experts.'),
        nbf.v4.new_code_cell('import torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nprint("Ready to route tokens!")'),
        nbf.v4.new_code_cell('''num_experts = 4
top_k = 2
d_model = 16

# Dummy token representations (Batch=1, Seq=3, Dim=16)
x = torch.randn(1, 3, d_model)

# The classic Gating network
router = nn.Linear(d_model, num_experts)
logits = router(x)
routing_probs = F.softmax(logits, dim=-1)

# Pick the top-k experts
top_probs, top_indices = torch.topk(routing_probs, top_k, dim=-1)

print("For 3 tokens, here are the indices of the experts they are routed to:")
print(top_indices)'''),
        nbf.v4.new_markdown_cell('My takeaway: The router tells the model to completely ignore experts not in those `top_indices`, drastically reducing FLOPs!')
    ]
    with open('d:/STSA-2026/llms-from-scratch-practice/notebooks/ch04/07_moe-implementation.ipynb', 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

def build_delta():
    nb = nbf.v4.new_notebook()
    nb['cells'] = [
        nbf.v4.new_markdown_cell('# Chapter 4: Practice Lab - Gated DeltaNet Idea\n\nI want to look at how the gating scalar manipulates the standard QKV representation.'),
        nbf.v4.new_code_cell('import torch\nimport torch.nn as nn\nprint("Loading gating mechanisms!")'),
        nbf.v4.new_code_cell('''d_in = 64
d_out = 64

# Dummy input token layer
x = torch.randn(1, 4, d_in)

# Standard Query
W_query = nn.Linear(d_in, d_out)
queries = W_query(x)

# The DeltaNet Gate Addition
W_gate = nn.Linear(d_in, d_out)
gate = torch.sigmoid(W_gate(x))

# Apply the gate to queries (simulating memory decay)
gated_queries = queries * gate
print(f"Shape of Gated Queries: {gated_queries.shape}")
print("Values are modulated completely by the sigmoid scalar!")''')
    ]
    with open('d:/STSA-2026/llms-from-scratch-practice/notebooks/ch04/08_deltanet-implementation.ipynb', 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

if __name__ == '__main__':
    build_swa()
    build_moe()
    build_delta()
    print("Final Notebooks built!")
