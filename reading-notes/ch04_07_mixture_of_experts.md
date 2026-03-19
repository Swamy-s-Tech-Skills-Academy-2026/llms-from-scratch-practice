# Chapter 4: Mixture of Experts (MoE)
## Reflection Date: March 3, 2026

Every optimization I've learned so far has been about shrinking the Attention mechanism. But **Mixture of Experts (MoE)** targets the other massive block in the transformer: the Feed-Forward Network (FFN).

## The MoE Concept
In a standard dense Transformer layer, the FFN contains a huge chunk of the model parameters. 
I'm learning that MoE replaces this single large FFN block with multiple independent FFN blocks (called **"Experts"**).
- **The Router:** A specialized gating network (a linear layer + softmax) analyzes the incoming token and scores which "Experts" are best suited to process it.
- **Sparsity:** Even if my model has 256 experts, the router might only explicitly send the token to the Top-2 experts. 

## Increasing Capacity Without Compute
This is the magic:
- I can increase the *total parameter count* endlessly by adding more experts, giving the model a massive knowledge base ("capacity").
- Because I only route to `K` experts during inference, my active parameter count remains tiny. Gaining massive capacity *without* quadratic increases in FLOPs/latency.

Example I noticed from DeepSeek-V3: It has 671 Billion total parameters, yet during inference, only 37 Billion are active at any one time — 1 shared expert (always active) plus 8 routed experts (selected by the router from 256 total) = 9 active experts in total.

## Shared Experts
Another interesting trick: DeepSeek uses 1 "Shared" expert that processes *every single token*. My takeaway: this prevents redundant learning. Common syntactic patterns go to the shared expert, freezing the other 256 experts to specialize intensely in dense topics like math, coding, or history. 
