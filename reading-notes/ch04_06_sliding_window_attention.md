# Chapter 4: Sliding Window Attention (SWA)
*Reflection Date: March 3, 2026*

I'm continuing my journey through attention optimization. I just reviewed Grouped-Query and Latent Attention, but **Sliding Window Attention (SWA)** explores a completely different approach. Instead of compressing the matrices, it compresses the *context*.

## The Concept: Local vs. Global Attention
Standard Multi-Head Attention (MHA) is *global*. Every single token attends to every other previous token. My takeaway: this is why the context length matrix multiplication scales quadratically ($\mathcal{O}(N^2)$).

**Sliding Window Attention** is *local*. 
- A token is only allowed to attend to a fixed-size local window (e.g., 1024 tokens) directly preceding it.
- This creates a diagonal band in the attention matrix. Everything outside the window is masked out completely. 
- During generation inference, this means my KV Cache only needs to store the last `W` tokens, dramatically bounding memory usage no matter how long the conversation gets.

## Hybrid Architectures
I learned that Google's Gemma models use SWA brilliantly:
- **Gemma 2:** Uses a 1:1 ratio. Every alternating layer alternates between Local SWA and Global MHA.
- **Gemma 3:** Pushes this further to a 5:1 ratio (5 SWA layers for every 1 Global layer) and shrinks the window size to 1024. 
- *Why does this work?* It turns out that local context is sufficient for immediate grammar/syntax, while only a few global layers are needed to integrate the overarching conversational topic. 

My next task in my practice code will be to prove mathematically how much memory this saves relative to vanilla MHA.
