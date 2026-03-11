# Source-Material Migration Tracker

## Purpose

This tracker records the current migration state of content under `source-material/` into learner-owned artifacts in `reading-notes/`, `notebooks/`, `examples/`, `docs/`, and `src/`.

## Status Legend

- `migrated-exact`: a clearly corresponding destination file exists with the same role.
- `migrated-renamed`: the source appears migrated, but the learner-owned destination uses a different name.
- `partial-synthesized`: the topic is represented in learner-owned artifacts, but not as a one-to-one migrated file.
- `source-only`: no clear learner-owned destination exists yet.
- `reference-asset`: raw reference data or vendor material kept in `source-material/`.

## Summary

- `ch01`: 2 files
- `ch02`: 20 files
- `ch03`: 11 files
- `ch04`: 37 files
- Total: 70 files

## Chapter 1

| Source file | Status | Verified synthesized destination | Notes |
| --- | --- | --- | --- |
| `source-material/ch01/reading-recommendations.md` | `partial-synthesized` | `reading-notes/ch01_reading-strategy.md` | The learner-owned note captures study process rather than a direct rewrite. |
| `source-material/ch01/README.md` | `partial-synthesized` | `reading-notes/ch01_reading-strategy.md` | Chapter context is present, but not as a one-to-one migrated README. |

## Chapter 2

| Source file | Status | Verified synthesized destination | Notes |
| --- | --- | --- | --- |
| `source-material/ch02/README.md` | `partial-synthesized` | `notebooks/ch02/`, `examples/ch02/`, `reading-notes/ch02_decoder_only_transformer_flow.md` | Chapter material is distributed across the three learning layers. |
| `source-material/ch02/01_main-chapter-code/ch02.ipynb` | `migrated-renamed` | `notebooks/ch02/01_main-chapter-code/01_ch02.ipynb` | Same main chapter role, learner-owned naming. |
| `source-material/ch02/01_main-chapter-code/dataloader.ipynb` | `migrated-exact` | `notebooks/ch02/01_main-chapter-code/dataloader.ipynb` | Direct learner-owned notebook counterpart exists. |
| `source-material/ch02/01_main-chapter-code/exercise-solutions.ipynb` | `migrated-exact` | `notebooks/ch02/01_main-chapter-code/exercise-solutions.ipynb` | Direct learner-owned notebook counterpart exists. |
| `source-material/ch02/01_main-chapter-code/README.md` | `source-only` | None yet | No learner-owned README exists in the same subfolder. |
| `source-material/ch02/01_main-chapter-code/the-verdict.txt` | `migrated-exact` | `notebooks/ch02/01_main-chapter-code/the-verdict.txt` | Shared raw text asset is intentionally mirrored for the notebook workflow. |
| `source-material/ch02/02_bonus_bytepair-encoder/bpe_openai_gpt2.py` | `source-only` | None yet | Raw reference implementation still only exists in source-material. |
| `source-material/ch02/02_bonus_bytepair-encoder/compare-bpe-tiktoken.ipynb` | `migrated-renamed` | `notebooks/ch02/02_bonus_bytepair-encoder/01_understanding_bpe_implementations.ipynb` | Same learning topic under a learner-owned name. |
| `source-material/ch02/02_bonus_bytepair-encoder/README.md` | `migrated-exact` | `notebooks/ch02/02_bonus_bytepair-encoder/README.md` | Direct learner-owned counterpart exists. |
| `source-material/ch02/02_bonus_bytepair-encoder/requirements-extra.txt` | `source-only` | None yet | Optional dependency note remains source-only. |
| `source-material/ch02/02_bonus_bytepair-encoder/gpt2_model/encoder.json` | `reference-asset` | None required yet | Raw tokenizer artifact kept only as reference material. |
| `source-material/ch02/02_bonus_bytepair-encoder/gpt2_model/vocab.bpe` | `reference-asset` | None required yet | Raw tokenizer artifact kept only as reference material. |
| `source-material/ch02/03_bonus_embedding-vs-matmul/embeddings-and-linear-layers.ipynb` | `migrated-exact` | `notebooks/ch02/03_bonus_embedding-vs-matmul/embeddings-and-linear-layers.ipynb` | Direct learner-owned counterpart exists. |
| `source-material/ch02/03_bonus_embedding-vs-matmul/README.md` | `migrated-exact` | `notebooks/ch02/03_bonus_embedding-vs-matmul/README.md` | Direct learner-owned counterpart exists. |
| `source-material/ch02/04_bonus_dataloader-intuition/dataloader-intuition.ipynb` | `migrated-exact` | `notebooks/ch02/04_bonus_dataloader-intuition/dataloader-intuition.ipynb` | Direct learner-owned counterpart exists. |
| `source-material/ch02/04_bonus_dataloader-intuition/README.md` | `migrated-exact` | `notebooks/ch02/04_bonus_dataloader-intuition/README.md` | Direct learner-owned counterpart exists. |
| `source-material/ch02/05_bpe-from-scratch/bpe-from-scratch-simple.ipynb` | `migrated-exact` | `notebooks/ch02/05_bpe-from-scratch/bpe-from-scratch-simple.ipynb` | Direct learner-owned counterpart exists. |
| `source-material/ch02/05_bpe-from-scratch/bpe-from-scratch.ipynb` | `migrated-exact` | `notebooks/ch02/05_bpe-from-scratch/bpe-from-scratch.ipynb` | Direct learner-owned counterpart exists. |
| `source-material/ch02/05_bpe-from-scratch/README.md` | `migrated-exact` | `notebooks/ch02/05_bpe-from-scratch/README.md` | Direct learner-owned counterpart exists. |
| `source-material/ch02/05_bpe-from-scratch/tests.py` | `migrated-exact` | `notebooks/ch02/05_bpe-from-scratch/tests.py` | Direct learner-owned counterpart exists. |

## Chapter 3

| Source file | Status | Verified synthesized destination | Notes |
| --- | --- | --- | --- |
| `source-material/ch03/README.md` | `partial-synthesized` | `notebooks/ch03/`, `examples/ch03/`, `reading-notes/ch03_attention_mechanisms.md` | Chapter topic is represented across the three learning layers. |
| `source-material/ch03/01_main-chapter-code/ch03.ipynb` | `migrated-renamed` | `notebooks/ch03/01_attention_mechanisms.ipynb` | Main attention notebook exists under learner-owned naming. |
| `source-material/ch03/01_main-chapter-code/exercise-solutions.ipynb` | `migrated-exact` | `notebooks/ch03/exercise-solutions.ipynb` | Direct learner-owned counterpart exists. |
| `source-material/ch03/01_main-chapter-code/multihead-attention.ipynb` | `migrated-renamed` | `notebooks/ch03/02_multihead-attention.ipynb` | Same topic under learner-owned naming. |
| `source-material/ch03/01_main-chapter-code/README.md` | `source-only` | None yet | No chapter-subfolder README exists in learner-owned form. |
| `source-material/ch03/01_main-chapter-code/small-text-sample.txt` | `migrated-exact` | `notebooks/ch03/small-text-sample.txt` | Shared raw text asset is intentionally mirrored for the notebook workflow. |
| `source-material/ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb` | `migrated-exact` | `notebooks/ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb` | Direct learner-owned counterpart exists. |
| `source-material/ch03/02_bonus_efficient-multihead-attention/README.md` | `migrated-exact` | `notebooks/ch03/02_bonus_efficient-multihead-attention/README.md` | Direct learner-owned counterpart exists. |
| `source-material/ch03/02_bonus_efficient-multihead-attention/tests/test_mha_implementations.py` | `source-only` | None yet | Raw test asset has not been migrated. |
| `source-material/ch03/03_understanding-buffers/README.md` | `migrated-exact` | `notebooks/ch03/03_understanding-buffers/README.md` | Direct learner-owned counterpart exists. |
| `source-material/ch03/03_understanding-buffers/understanding-buffers.ipynb` | `migrated-exact` | `notebooks/ch03/03_understanding-buffers/understanding-buffers.ipynb` | Direct learner-owned counterpart exists. |

## Chapter 4

| Source file | Status | Verified synthesized destination | Notes |
| --- | --- | --- | --- |
| `source-material/ch04/README.md` | `partial-synthesized` | `reading-notes/ch04_01_gpt_model_architecture.md` to `reading-notes/ch04_08_deltanet.md`, `notebooks/ch04/`, `examples/ch04/` | Chapter material exists across theory, implementation, and practice layers. |
| `source-material/ch04/01_main-chapter-code/ch04.ipynb` | `migrated-renamed` | `notebooks/ch04/01_gpt-model-implementation.ipynb` | Main chapter notebook exists under learner-owned naming. |
| `source-material/ch04/01_main-chapter-code/exercise-solutions.ipynb` | `migrated-exact` | `notebooks/ch04/exercise-solutions.ipynb` | Direct learner-owned counterpart exists. |
| `source-material/ch04/01_main-chapter-code/gpt.py` | `partial-synthesized` | `src/model/ch04_core.py` | Learner-owned reusable GPT components now exist in `src/model`. |
| `source-material/ch04/01_main-chapter-code/previous_chapters.py` | `partial-synthesized` | `src/model/ch04_core.py` | Cross-chapter reusable transformer pieces are now learner-owned under `src/model`. |
| `source-material/ch04/01_main-chapter-code/README.md` | `source-only` | None yet | No chapter-subfolder README exists in learner-owned form. |
| `source-material/ch04/01_main-chapter-code/tests.py` | `partial-synthesized` | `tests/test_ch04_model_components.py` | Learner-owned validation now exists, but not as a one-to-one migrated test file. |
| `source-material/ch04/02_performance-analysis/flops-analysis.ipynb` | `migrated-renamed` | `notebooks/ch04/02_performance-analysis-implementation.ipynb` | Notebook topic is present under learner-owned naming. |
| `source-material/ch04/02_performance-analysis/README.md` | `partial-synthesized` | `reading-notes/ch04_02_performance_analysis.md`, `examples/ch04/02_performance_examples.py` | Topic is represented across theory and practice layers. |
| `source-material/ch04/02_performance-analysis/requirements-extra.txt` | `source-only` | None yet | Optional dependency note remains source-only. |
| `source-material/ch04/03_kv-cache/gpt_ch04.py` | `partial-synthesized` | `src/model/ch04_core.py` | Core GPT implementation now exists in learner-owned reusable form. |
| `source-material/ch04/03_kv-cache/gpt_with_kv_cache_optimized.py` | `partial-synthesized` | `src/model/ch04_variants.py` | Learner-owned cached attention implementation now exists. |
| `source-material/ch04/03_kv-cache/gpt_with_kv_cache.py` | `partial-synthesized` | `src/model/ch04_variants.py`, `examples/ch04/03_kv_cache_examples.py` | Topic is now represented in both reusable code and practice examples. |
| `source-material/ch04/03_kv-cache/README.md` | `partial-synthesized` | `reading-notes/ch04_03_kv_cache.md`, `notebooks/ch04/03_kv-cache-implementation.ipynb`, `examples/ch04/03_kv_cache_examples.py` | Topic is represented across the three learning layers. |
| `source-material/ch04/03_kv-cache/tests.py` | `partial-synthesized` | `tests/test_ch04_model_components.py` | Learner-owned validation exists, but not as a one-to-one migrated test file. |
| `source-material/ch04/04_gqa/gpt_with_kv_gqa.py` | `partial-synthesized` | `src/model/ch04_variants.py` | Learner-owned GQA implementation now exists. |
| `source-material/ch04/04_gqa/gpt_with_kv_mha.py` | `partial-synthesized` | `src/model/ch04_variants.py` | Learner-owned MHA baseline for comparison now exists in reusable form. |
| `source-material/ch04/04_gqa/memory_estimator_gqa.py` | `partial-synthesized` | `src/model/ch04_variants.py`, `examples/ch04/04_gqa_examples.py` | Learner-owned estimator function and practice example now exist. |
| `source-material/ch04/04_gqa/plot_memory_estimates_gqa.py` | `source-only` | None yet | No learner-owned plotting script exists yet. |
| `source-material/ch04/04_gqa/README.md` | `partial-synthesized` | `reading-notes/ch04_04_grouped_query_attention.md`, `notebooks/ch04/04_gqa-implementation.ipynb`, `examples/ch04/04_gqa_examples.py` | Topic is represented across the three learning layers. |
| `source-material/ch04/05_mla/gpt_with_kv_mha.py` | `partial-synthesized` | `src/model/ch04_variants.py` | Learner-owned MHA baseline exists in reusable form. |
| `source-material/ch04/05_mla/gpt_with_kv_mla.py` | `partial-synthesized` | `src/model/ch04_variants.py` | Learner-owned MLA implementation now exists. |
| `source-material/ch04/05_mla/memory_estimator_mla.py` | `partial-synthesized` | `src/model/ch04_variants.py`, `examples/ch04/05_mla_examples.py` | Learner-owned estimator function and practice example now exist. |
| `source-material/ch04/05_mla/plot_memory_estimates_mla.py` | `source-only` | None yet | No learner-owned plotting script exists yet. |
| `source-material/ch04/05_mla/README.md` | `partial-synthesized` | `reading-notes/ch04_05_multi_head_latent_attention.md`, `notebooks/ch04/05_mla-implementation.ipynb`, `examples/ch04/05_mla_examples.py` | Topic is represented across the three learning layers. |
| `source-material/ch04/06_swa/gpt_with_kv_mha.py` | `partial-synthesized` | `src/model/ch04_variants.py` | Learner-owned MHA baseline exists in reusable form. |
| `source-material/ch04/06_swa/gpt_with_kv_swa.py` | `partial-synthesized` | `src/model/ch04_variants.py` | Learner-owned SWA implementation now exists. |
| `source-material/ch04/06_swa/memory_estimator_swa.py` | `partial-synthesized` | `src/model/ch04_variants.py`, `examples/ch04/06_swa_examples.py` | Learner-owned estimator function and practice example now exist. |
| `source-material/ch04/06_swa/plot_memory_estimates_swa.py` | `source-only` | None yet | No learner-owned plotting script exists yet. |
| `source-material/ch04/06_swa/README.md` | `partial-synthesized` | `reading-notes/ch04_06_sliding_window_attention.md`, `notebooks/ch04/06_swa-implementation.ipynb`, `examples/ch04/06_swa_examples.py` | Topic is represented across the three learning layers. |
| `source-material/ch04/07_moe/gpt_with_kv_ffn.py` | `partial-synthesized` | `src/model/ch04_core.py`, `src/model/ch04_variants.py` | Learner-owned dense and sparse feed-forward blocks now exist. |
| `source-material/ch04/07_moe/gpt_with_kv_moe.py` | `partial-synthesized` | `src/model/ch04_variants.py` | Learner-owned MoE feed-forward implementation now exists. |
| `source-material/ch04/07_moe/memory_estimator_moe.py` | `source-only` | None yet | No learner-owned MoE memory estimator exists yet. |
| `source-material/ch04/07_moe/plot_memory_estimates_moe.py` | `source-only` | None yet | No learner-owned plotting script exists yet. |
| `source-material/ch04/07_moe/README.md` | `partial-synthesized` | `reading-notes/ch04_07_mixture_of_experts.md`, `notebooks/ch04/07_moe-implementation.ipynb`, `examples/ch04/07_moe_examples.py` | Topic is represented across the three learning layers. |
| `source-material/ch04/08_deltanet/plot_memory_estimates_gated_deltanet.py` | `partial-synthesized` | `src/model/ch04_variants.py`, `examples/ch04/08_deltanet_examples.py` | Learner-owned DeltaNet state estimator now exists, but not yet as a plotting script. |
| `source-material/ch04/08_deltanet/README.md` | `partial-synthesized` | `reading-notes/ch04_08_deltanet.md`, `notebooks/ch04/08_deltanet-implementation.ipynb`, `examples/ch04/08_deltanet_examples.py` | Topic is represented across the three learning layers. |

## Immediate Action Queue

1. Migrate the remaining Chapter 4 `source-only` plotting and estimator scripts into learner-owned assets.
2. Decide whether raw dependency notes like `requirements-extra.txt` should remain source-only or be documented in learner-facing READMEs.
3. Decide whether reference assets like `encoder.json` and `vocab.bpe` should remain only in `source-material/` or be mirrored into a clearly marked learner-facing reference folder.
4. Revisit each `partial-synthesized` item after notebook-by-notebook review and mark it `migrated-renamed` or `migrated-exact` where justified.