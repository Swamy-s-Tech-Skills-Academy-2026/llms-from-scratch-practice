# Chapter 4: Grouped-Query Attention (GQA) Memory Savings
## Reflection Date: March 3, 2026

I'm continuing to refine the architecture of my GPT model. While the standard Multi-Head Attention (MHA) model with a KV Cache dramatically speeds up inference, the KV Cache itself consumes an enormous amount of GPU memory. I'm learning about **Grouped-Query Attention (GQA)** as a highly effective optimization used in models like Llama.

## The Memory Bottleneck of Standard MHA
My understanding is this: in Standard Multi-Head Attention, every single attention head gets its own Query (Q), Key (K), and Value (V) weight matrices.
- This means during inference, I have to cache a unique set of Keys and Values *for every single head* across *every single layer*.
- This scales dreadfully. Memory consumption for the KV Cache becomes massive as context lengths grow.

## How GQA Solves the Problem
Grouped-Query Attention groups multiple Query heads together so they **share** the same Key and Value representations.
- **For example:** If I have 6 attention heads and I create 3 "KV groups", then Heads 1 & 2 will share one set of K and V. Heads 3 & 4 will share the second, and Heads 5 & 6 will share the third.
- **The Result:** I compute and store fewer Keys and Values in my KV Cache, directly reducing memory usage and memory bandwidth during inference. 

## The Extremes
I still need to remember the spectrum of attention mechanisms conceptually:
1. **Multi-Head Attention (MHA):** Every Query head has its own K and V head. (High memory, standard performance).
2. **Multi-Query Attention (MQA):** *All* Query heads share exactly *one* K and V head. (Lowest memory, but modeling performance usually degrades noticeably).
3. **Grouped-Query Attention (GQA):** The sweet spot. Groups of Query heads share K and V heads. (Great balance of memory savings and maintaining modeling high performance).

## Implementation Thought Process
To implement this in PyTorch, my takeaway is that I would split `self.W_kv` to produce fewer heads than `self.W_q`. Then, during the `forward` pass, I'd need to explicitly `repeat` or `expand` the K and V tensors so they match the expected dimensions of the Q tensors before the final attention score multiplications happen. I will add an example estimator to my practice folder and review the dimensions in my notebook.
