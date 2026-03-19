# Chapter 4: Multi-Head Latent Attention (MLA)
## Reflection Date: March 3, 2026

I've learned about Grouped-Query Attention (GQA) to save memory, but I just discovered a newer, fascinating alternative used in models like DeepSeek V2/V3/R1: **Multi-Head Latent Attention (MLA)**.

## Moving Beyond GQA
GQA works by forcing multiple attention heads to explicitly share the exact same Keys and Values. However, studies show this can sometimes degrade modeling performance compared to full Multi-Head Attention (MHA). 

My takeaway on how MLA is different: Instead of arbitrary grouping, MLA **compresses** the Key and Value tensors into a shared, lower-dimensional "latent space" before caching them.

## The MLA Mechanism
1. **During Inference:** I take the full high-dimensional $K$ and $V$ tensors and project them down to a smaller `latent_dim` using a down-projection (a single linear layer).
2. **Caching:** I only store this much smaller compressed vector in my KV Cache. 
3. **During Generation:** When I need to compute attention scores, I read the compressed vector from the cache and use an up-projection (a single linear layer) to restore $K$ and $V$ back to their original size `embed_dim`. 

## The Trade-Off
This changes the dynamics! 
- I am trading **Compute (FLOPs)** for **Memory (VRAM)**. I have to do an extra matrix multiplication (projecting up and down) every generation step.
- But memory savings are drastic. In MHA, I store `embed_dim * 2` (for both $K$ and $V$) bytes per token. In MLA, I only store `latent_dim` bytes per token. 
- Incredibly, the DeepSeek paper shows MLA actually *outperforms* MHA in modeling quality in some contexts, making it a strict upgrade over GQA!

My next step is to run a simulation notebook comparing the KV Cache size of standard MHA vs MLA using standard proxy numbers.
