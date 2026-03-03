import nbformat as nbf
import os

def create_perf_notebook():
    nb = nbf.v4.new_notebook()
    cells = [
        nbf.v4.new_markdown_cell('# Chapter 4: Practice Lab - Performance and Parameters\n\nI want to verify my intuition about how many parameters exist in standard model configurations by writing a script that counts them. This is the hands-on simulation corresponding to my reading notes on FLOPs and parameter counting.'),
        nbf.v4.new_code_cell('import torch\nimport torch.nn as nn\n\n# Ensures reproducibility per the learning guidelines\ntorch.manual_seed(42)\nprint("Ready for performance analysis!")'),
        nbf.v4.new_markdown_cell('## 1. Defining a Tiny Model to Profile\n\nI will create a very basic mock FeedForward layer as a proxy for the GPT network to see how parameters scale.'),
        nbf.v4.new_code_cell('class MockLayer(nn.Module):\n    def __init__(self, emb_dim):\n        super().__init__()\n        self.fc1 = nn.Linear(emb_dim, 4 * emb_dim)\n        self.fc2 = nn.Linear(4 * emb_dim, emb_dim)\n\n    def forward(self, x):\n        return self.fc2(self.fc1(x))\n\nmodel = MockLayer(768)'),
        nbf.v4.new_markdown_cell('## 2. Counting the Parameters\n\nI can loop through `model.parameters()` and multiply the shapes to get the raw parameter count.'),
        nbf.v4.new_code_cell('total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)\nprint(f"Total Parameters in MockLayer: {total_params:,}")\n\n# Memory calculation (fp32 = 4 bytes per parameter)\nmem_bytes = total_params * 4\nmem_mb = mem_bytes / (1024 ** 2)\nprint(f"Memory strictly for weights: {mem_mb:.2f} MB")')
    ]
    nb['cells'] = cells
    with open('d:/STSA-2026/llms-from-scratch-practice/notebooks/ch04/02_performance-analysis-implementation.ipynb', 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

def create_kv_notebook():
    nb = nbf.v4.new_notebook()
    cells = [
        nbf.v4.new_markdown_cell('# Chapter 4: Practice Lab - KV Caching Mechanism\n\nI am extending my Multi-Head Attention intuition to include a Key-Value cache. This will drastically speed up autoregressive decoding.'),
        nbf.v4.new_code_cell('import torch\nimport torch.nn as nn\n\ntorch.manual_seed(42)\nprint("Ready to explore KV Caching!")'),
        nbf.v4.new_markdown_cell('## 1. Simulating the Shapes\n\nIf my Prompt is "Time flies", I have 2 tokens. The context is `B=1, T=2`.'),
        nbf.v4.new_code_cell('batch_size = 1\nseq_len = 2\nhead_dim = 64\n\n# Mocking previous K and V shapes (simulating they have already been computed)\nhistorical_K = torch.rand(batch_size, seq_len, head_dim)\nhistorical_V = torch.rand(batch_size, seq_len, head_dim)\nprint(f"Historical K shape: {historical_K.shape}")'),
        nbf.v4.new_markdown_cell('## 2. Generating the Next Token\n\nWhen calculating generation step 3 ("fast"), I only need to pass the query, key, and value for *that single new token* (`seq_len = 1`). Then I concatenate it to the history.'),
        nbf.v4.new_code_cell('new_token_K = torch.rand(batch_size, 1, head_dim)\nnew_token_V = torch.rand(batch_size, 1, head_dim)\n\n# The crucial KV cache step: concatenation along the sequence dimension (dim=1)\nupdated_K_cache = torch.cat((historical_K, new_token_K), dim=1)\nupdated_V_cache = torch.cat((historical_V, new_token_V), dim=1)\n\nprint(f"New K Cache shape: {updated_K_cache.shape}")\n# See? Now it has 3 tokens! My query will attend to all 3 without having to re-multiply them.')
    ]
    nb['cells'] = cells
    with open('d:/STSA-2026/llms-from-scratch-practice/notebooks/ch04/03_kv-cache-implementation.ipynb', 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

if __name__ == "__main__":
    create_perf_notebook()
    create_kv_notebook()
    print("Notebooks written")
