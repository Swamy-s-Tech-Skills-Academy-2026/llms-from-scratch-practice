# Chapter 4: Gated DeltaNet and Linear Attention
## Reflection Date: March 3, 2026

I've finally reached the limits of modifying standard attention. To solve the $\mathcal{O}(N^2)$ context-length scaling problem once and for all, I'm reviewing **Linear Attention mechanisms**, specifically the **Gated DeltaNet** and **Kimi Linear** architectures.

## Linear Attention
Regular attention computes a matrix of size $N \times N$, which explodes as $N$ (the sequence length) grows to 100k+ tokens. Linear Attention changes the order of operations mathematically, leveraging the associative property of matrix multiplication, so it scales linearly $\mathcal{O}(N)$. 
My takeaway: the core problem with basic linear attention has traditionally been poor generation quality compared to MHA.

## Gated DeltaNet
To fix the quality drop, modern hybrid architectures pull inspiration from RNNs (like LSTMs) and State-Space Models (like Mamba).
- Gated DeltaNet introduces an explicit **gating mechanism** to the attention layer. 
- The gate acts similarly to a memory decay rate. It controls what the network "forgets" and "remembers" as it progresses linearly through a very long sequence.

## Hybrid Models (Kimi Linear/Qwen3-Next)
I noticed that nobody has completely thrown away full attention yet. 
- Models like Qwen3-Next and Kimi Linear use a 3:1 ratio.
- Out of 4 transformer layers, 3 will use highly-efficient Gated DeltaNet linear attention, and 1 will use standard full attention (or MLA).
- This creates the best of both worlds: ultra-long context windows that don't fry GPU memory, anchored periodically by exact global attention retrieval.

I'm adding an implementation check in my examples and wrapping up my core concepts for the GPT architecture!
