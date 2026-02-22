# Bonus: Building a BPE Tokenizer From Scratch

**Purpose**: Understanding how Byte Pair Encoding works by implementing it step-by-step.

## Why I Care About This

I want to understand why text like "unhappiness" becomes multiple tokens and what the tokenizer is actually doing when it processes a sentence. Reading about BPE wasn't enough — I needed to build it.

## What's in This Folder

### `bpe-from-scratch-simple.ipynb`

A minimal, readable BPE implementation. I'm prioritizing clarity over completeness here — everything is stepped through slowly so I can trace what's happening at each merge step.

- Starts with a character-level vocabulary
- Counts bigram frequencies iteratively
- Merges the most frequent pair and repeats
- Produces a vocabulary and encoding for short examples

**My takeaway**: BPE is a greedy compression algorithm. The vocabulary is built by repeatedly merging the most common adjacent pair.

### `bpe-from-scratch.ipynb`

A more complete BPE implementation that handles edge cases and loads the official GPT-2 vocabulary. This is harder to follow — I'm working through it after the simple version.

### `tests.py`

Unit tests that verify the BPE implementation produces correct encodings.

## Source Attribution

Concepts derived from *Build a Large Language Model From Scratch* (Raschka), Chapter 2 bonus material.  
Implementation is my own reconstruction — not a copy of the source-material notebooks.
