import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = [
    nbf.v4.new_markdown_cell('# Chapter 4: Implementing a GPT Model from Scratch\n\nI\'m building intuition for the full GPT Architecture by constructing the `GPTModel` class and learning its generative loop piecemeal. Here, I\'ll practice assembling the previously-learned Multi-Head Attention layer alongside new critical components like `LayerNorm` and `FeedForward`.'),
    nbf.v4.new_code_cell('import torch\nimport torch.nn as nn\nimport tiktoken\n\n# Ensures reproducibility per the learning guidelines\ntorch.manual_seed(42)\nprint("Ready to practice PyTorch!")'),
    nbf.v4.new_markdown_cell('## 1. Setting up the GPT Configurations\n\nTo start, I\'ll define a dictionary holding all the hyper-parameters for a GPT-2 Small sized model. This way I can change the overall shape centrally.'),
    nbf.v4.new_code_cell('GPT_CONFIG_124M = {\n    "vocab_size": 50257,    # Vocabulary size\n    "ctx_len": 1024,        # Context length\n    "emb_dim": 768,         # Embedding dimension\n    "n_heads": 12,          # Number of attention heads\n    "n_layers": 12,         # Number of layers\n    "drop_rate": 0.1,       # Dropout rate\n    "qkv_bias": False       # Query-Key-Value bias\n}'),
    nbf.v4.new_markdown_cell('## 2. Implementing the Missing Components\n\nI need a few missing Lego pieces before I assemble the full architecture: `LayerNorm`, `Activate`, and a `FeedForward` loop.'),
    nbf.v4.new_code_cell('''class DummyLayerNorm(nn.Module):
    def __init__(self, emb_dim):
        super().__init__()
        self.eps = 1e-5
        self.scale = nn.Parameter(torch.ones(emb_dim))
        self.shift = nn.Parameter(torch.zeros(emb_dim))

    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)
        norm_x = (x - mean) / torch.sqrt(var + self.eps)
        return self.scale * norm_x + self.shift

# Test it out
test_tensor = torch.rand(2, 5, 768)
ln = DummyLayerNorm(768)
print(ln(test_tensor).shape)'''),
    nbf.v4.new_markdown_cell('## 3. The Generating Function\n\nFinally, let\'s practice simple greedy decoding. My understanding is that we iteratively append the next highest probability token to the context sequence.')
]
nb['cells'] = cells
with open('notebooks/ch04/01_gpt-model-implementation.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print("Notebook generated.")