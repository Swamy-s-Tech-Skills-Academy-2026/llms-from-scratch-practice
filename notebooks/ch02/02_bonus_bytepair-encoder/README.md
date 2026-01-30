# Bonus Section: Understanding Byte Pair Encoding (BPE)

**Purpose**: Deepening my understanding of BPE tokenization through hands-on exploration

## What's in This Folder

This bonus section is where I'm exploring different BPE implementations to understand:

- How modern tokenizers like tiktoken work
- Why BPE is used in GPT-2 and similar models
- Performance differences between implementations
- Practical considerations for using tokenizers

## Learning Notebooks

### 01_understanding_bpe_implementations.ipynb

**What I'm learning**: Comparing different BPE implementations (tiktoken, transformers, original OpenAI code)

**Key concepts covered**:

- Using tiktoken for modern, fast BPE encoding
- Understanding token IDs and decoding
- How BPE handles special characters and emojis
- Performance characteristics of different implementations
- When to use each tokenizer implementation

**Personal learning goals**:

- Build intuition for how BPE breaks down text
- Understand why BPE is better than simple word splitting
- Learn practical tokenizer usage for LLM projects

## Source Material

This educational content was synthesized from:

- **Book**: *Build a Large Language Model From Scratch* by Sebastian Raschka
- **Reference**: Author's BPE comparison code in `../../source-material/ch02_bonus_bpe_from_author/`
- **Original implementation**: OpenAI's GPT-2 encoder.py (Modified MIT License)

**Important**: Following the repository's zero-copy policy, all content here is written in my own words to demonstrate understanding, not copied from sources.

## Why This is "Bonus" Content

This folder is marked as "bonus" because:

1. **Core learning is in main chapter** - The essential tokenization concepts are in `01_main-chapter-code/`
2. **Comparative exploration** - This dives deeper into implementation details and comparisons
3. **Optional dependencies** - Some experiments require transformers library (not in core deps)
4. **Performance analysis** - Includes benchmarking which is beyond basic learning needs

## Learning Progression

I recommend following this order:

1. **First**: Complete `../01_main-chapter-code/01_ch02.ipynb` - Basic tokenization fundamentals
2. **Then**: Work through `01_understanding_bpe_implementations.ipynb` - Compare different BPE tools
3. **Next** (planned): Implement simple BPE from scratch to understand the algorithm deeply

## Dependencies

### Core dependencies (already installed)

- tiktoken - Modern BPE tokenizer (in pyproject.toml)
- torch, numpy - Standard deps

### Optional dependencies (for comparisons)
If you want to run transformers comparisons, install the `bpe-experiments` group:
```powershell
uv sync --group bpe-experiments
```

This will install:
- transformers>=4.33.2
- requests>=2.31.0
- tqdm>=4.66.0

**Note**: Using `uv sync` with dependency groups is the recommended approach for this repository, ensuring proper environment management.

## My Learning Status

- ✅ **Completed**: Understanding tiktoken basics and practical usage
- ✅ **Completed**: Compared different implementations conceptually  
- 🔄 **In Progress**: Building intuition for the BPE merge algorithm
- ⏳ **Next**: Implement simple BPE from scratch (planned)

## Notes to Self

**What I've learned**:

- BPE balances vocabulary size and sequence length
- tiktoken is the modern, fast way to use GPT-2 BPE
- Subword tokenization handles rare words and emojis gracefully
- Different implementations have different speed/feature tradeoffs

**What I still need to clarify**:

- Exactly how merge rules are learned from training data
- How to train a BPE vocabulary on custom corpus
- Impact of vocabulary size on model performance

**Questions I'm exploring**:

- Can I build a minimal BPE tokenizer to understand the algorithm?
- How do different vocabularies affect tokenization quality?
- What's the relationship between vocabulary size and model capacity?

---

**Date created**: January 27, 2026  
**Last updated**: January 27, 2026  
**Status**: Active learning in progress 🚀
