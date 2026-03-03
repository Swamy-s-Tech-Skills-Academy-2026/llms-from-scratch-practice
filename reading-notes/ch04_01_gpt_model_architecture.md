# Chapter 4: Implementing a GPT Model from Scratch - Architecture Notes
*Reflection Date: March 3, 2026*

I'm building intuition for the complete GPT architecture by assembling the pieces I learned in previous chapters (tokenization and attention) into a functional cohesive model. My goal here is to bridge the gap between individual components and the full generative loop.

## My High-Level Understanding of the GPT Architecture
At its core, a GPT model is a decoder-only transformer. It predicts the next token in a sequence. 
Here are the core components I need to build:
1. **Embedding Layer**: A combination of token embeddings (the meaning of the word) and positional embeddings (where the word is in the sequence).
2. **Transformer Blocks**: The "meat" of the network. A stack of identical blocks, each containing:
   - Layer Normalization
   - Masked Multi-Head Self-Attention
   - More Layer Normalization
   - A Feed-Forward Neural Network
3. **Output Head**: A final layer normalization followed by a linear layer to map the hidden states back to the vocabulary size (logits).

## Deep Dive into the New Components

### 1. Layer Normalization (`LayerNorm`)
My takeaway: Batch Normalization (which I'm familiar with from CNNs) normalizes across the batch dimension. But in NLP, sequences have variable lengths and batch sizes can be small. **Layer Normalization** normalizes across the *feature* dimension (the embedding size) for each token individually.
- **Why?** It stabilizes training and allows for deeper networks by ensuring the inputs to layers don't explode or vanish.
- **Math mapping**: We subtract the mean and divide by the variance across the feature vector, then scale and shift using learnable parameters ($\gamma$ and $\beta$). 

### 2. GELU Activation (`GELU`)
I noticed GPT uses GELU (Gaussian Error Linear Unit) instead of standard ReLU. 
- ReLU is strictly zero for negative values, which can cause "dead neurons".
- GELU is a smooth, differentiable approximation that allows a small gradient for negative numbers, weighted by their probability under a Gaussian distribution. This smoothness helps the model train better in deep transformer networks.

### 3. Feed-Forward Network (`FeedForward`)
After the attention mechanism figures out *how tokens relate to each other*, the Feed Forward network processes *each token individually*. 
- It usually consists of two linear layers with a GELU activation in between.
- The inner dimension typically expands by a factor of 4 (e.g., if `emb_dim` is 768, inner dimension expands to 3072, then compresses back to 768). My understanding is this acts as a "memory" or "knowledge" bank where complex transformations happen.

### 4. The `TransformerBlock` and Shortcut Connections
One thing I still need to keep top of mind: **Shortcut Connections** (also called residual connections). 
- We add the input of a sub-layer to its output: `x = x + sublayer(x)`.
- **Reason**: In deep networks, gradients tend to vanish during backpropagation. Shortcut connections give gradients an "express lane" backwards through the network.

### 5. Final Output and Text Generation
The model outputs logits. To actually generate text, I need to:
1. Take the logits of the *last* token in the sequence.
2. Apply `softmax` to get probabilities (optional if just using `argmax`, but required for sampling).
3. Pick the token with the highest logit (Greedy Decoding).
4. Append this token to the input and repeat!

## Next Steps for My Practice
I want to code this from scratch. I will construct each of these distinct Lego blocks in PyTorch, bring them together into `GPTModel`, and see if it can generate some (albeit random and untrained) text. My immediate next step is to head over to the lab notebook and implement this.
