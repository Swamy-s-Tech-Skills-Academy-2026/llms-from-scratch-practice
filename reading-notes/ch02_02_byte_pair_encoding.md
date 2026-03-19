# Chapter 2: Byte Pair Encoding — How Tokenizers Are Built
## Reflection Date: March 19, 2026

I've been running `tiktoken` without fully understanding what's happening inside it. The BPE notebooks finally answered that. My goal here is to cement what I now understand about how BPE works and why GPT-2 and later models use it.

## Why Not Just Split on Spaces?

My first instinct for tokenisation was character-level splitting or whitespace splitting. But these break down fast:
- Character-level: the sequence `"unhappiness"` becomes 12 separate tokens, each carrying almost no meaning. The model has to learn to piece them back together.
- Whitespace: rare words like `"Schifffahrt"` appear so rarely the model may never see them enough to learn anything.

BPE is the smart middle ground — it starts at characters and learns to merge the **most frequent adjacent pairs** until it hits a target vocabulary size.

## The BPE Algorithm (My Understanding)

1. Start with a corpus split into **individual characters** (plus a special end-of-word marker).
2. Count all adjacent character pairs in the corpus.
3. Merge the **most frequent pair** into a new single token.
4. Repeat steps 2–3 until you've made exactly `num_merges` merges.

Each merge is recorded in a **merge table**. At inference time, the same merges are applied to new text in the same order — that's how tokenisation is deterministic.

## What I Noticed About tiktoken's GPT-2 Tokeniser

- GPT-2 uses a vocabulary of **50,257** tokens (50,000 BPE + 256 byte tokens + 1 `<|endoftext|>` special token).
- The 256 raw byte tokens ensure the tokeniser can **handle any arbitrary Unicode input** — even if a substring was never seen during vocabulary training.
- Merges are applied greedily (left-to-right), which explains why the same word tokenises differently depending on its context (spacing before a word triggers different byte-level rules).

## My Takeaway: BPE Balances Vocabulary Size and Coverage

> Too small a vocabulary → many tokens per word (slow, less semantic meaning per token)
> Too large a vocabulary → very sparse embeddings; rare tokens almost never trained

The BPE algorithm finds a data-driven middle ground. I noticed that after ~40,000 merges, common English words are single tokens, while rare compound words get split at morpheme boundaries — which actually makes sense semantically.

## Comparing Implementations

I worked through two approaches in the notebooks:

| Approach | Description | My takeaway |
|:---------|:------------|:------------|
| Reference: `bpe_openai_gpt2.py` | OpenAI's original Python regex-based BPE | Complex regex handles whitespace/punctuation boundaries |
| From scratch: `bpe-from-scratch.ipynb` | Character-pair counting loop | Shows the algorithm clearly, but the regex subtlety is hidden |

My next question: why does the regex in GPT-2 tokenisation split on apostrophes and contractions specially? That seems like a deliberate linguistics choice.
