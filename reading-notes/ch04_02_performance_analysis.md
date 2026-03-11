# Chapter 4: Performance Analysis of the GPT Model (FLOPs & Parameters)
## Reflection Date: March 3, 2026

I'm taking a brief detour to understand how to measure the performance and memory footprint of my GPT model. While I've implemented the `GPTModel` architecture, it's crucial for me to grasp its computational demands before I actually try to train it or deploy it.

## Counting Parameters
My first thought when looking at the architecture is: *how big is this thing?* The "size" of a model (like "124M") generally refers to its total number of trainable parameters.
- **Where are the parameters?** They are mostly stored in the `nn.Linear` layers (Weights and Biases) spanning the Multi-Head Attention blocks and the FeedForward networks, alongside the initial Token and Positional Embeddings.
- My takeaway: If I multiply the shape dimensions of a weight tensor, I get the parameter count for that specific layer. Summing these up across the entire model equals the total parameter count.

## FLOPs (Floating-Point Operations)
I'm learning that FLOPs are a standard metric for measuring the computational cost of a model.
- **MACs (Multiply-Accumulate Operations):** When computing `y = w * x + b`, there is exactly one multiplication and one addition per input scalar. That's one MAC, which maps to generally 2 FLOPs.
- **Why do I care?** When I scale my context length `ctx_len` (e.g., from 1024 to 2048), the self-attention mechanism's complexity grows quadratically $\mathcal{O}(N^2)$. My FLOPs will skyrocket during attention sequence calculations compared to linear layers.

## Memory Estimates (VRAM)
I noticed I need a way to estimate how much GPU memory (VRAM) I'll need.
- A 32-bit float (`fp32`) takes 4 bytes.
- Therefore, a 124 million parameter model takes roughly $124 \times 10^6 \times 4 \approx 500$ MB just to hold the weights!
- During training, I need memory not just for weights, but also for gradients (another 500MB) and optimizer states (Adam needs twice that, so ~1GB). This explains why training LLMs is so incredibly memory intensive.

## My Next Steps
I want to code a simple simulation to calculate the total parameters manually in my `GPTModel` and print out the estimated memory size before moving on to optimizing generation speed.
