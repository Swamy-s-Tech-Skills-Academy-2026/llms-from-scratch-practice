from __future__ import annotations

from pathlib import Path
from types import ModuleType
import sys

import nbformat
import pytest
import tiktoken


NOTEBOOK_STEM = "bpe-from-scratch"
REQUIRED_SYMBOLS = ("BPETokenizerSimple", "download_file_if_absent")
VERDICT_URL = (
    "https://raw.githubusercontent.com/rasbt/"
    "LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt"
)
GPT2_ASSET_URLS = {
    "vocab.bpe": "https://openaipublic.blob.core.windows.net/gpt-2/models/124M/vocab.bpe",
    "encoder.json": "https://openaipublic.blob.core.windows.net/gpt-2/models/124M/encoder.json",
}
VERDICT_SEARCH_DIRS = [
    "notebooks/ch02/01_main-chapter-code",
    "../01_main-chapter-code",
    "ch02/01_main-chapter-code",
    ".",
]
GPT2_SEARCH_DIRS = [
    "notebooks/ch02/02_bonus_bytepair-encoder/gpt2_model",
    "ch02/02_bonus_bytepair-encoder/gpt2_model",
    "../02_bonus_bytepair-encoder/gpt2_model",
    ".",
]


def _load_notebook_module(notebook_stem: str, required_symbols: tuple[str, ...]) -> ModuleType:
    notebook_path = Path(__file__).with_name(f"{notebook_stem}.ipynb")
    if not notebook_path.exists():
        raise FileNotFoundError(f"Notebook file not found at: {notebook_path}")

    with notebook_path.open("r", encoding="utf-8") as notebook_file:
        notebook = nbformat.read(notebook_file, as_version=4)

    module = ModuleType(notebook_stem)
    sys.modules[notebook_stem] = module

    for cell in notebook.cells:
        if cell.cell_type == "code":
            exec(cell.source, module.__dict__)

    missing = [name for name in required_symbols if name not in module.__dict__]
    if missing:
        raise ImportError(f"Missing definitions in notebook: {missing}")

    return module


def _build_openai_tokenizer(module: ModuleType, file_paths: dict[str, str]):
    tokenizer_class = module.BPETokenizerSimple
    tokenizer = tokenizer_class()
    tokenizer.load_vocab_and_merges_from_openai(
        vocab_path=file_paths["encoder.json"],
        bpe_merges_path=file_paths["vocab.bpe"],
    )
    return tokenizer


@pytest.fixture(scope="module")
def notebook_module() -> ModuleType:
    return _load_notebook_module(NOTEBOOK_STEM, REQUIRED_SYMBOLS)


@pytest.fixture(scope="module")
def verdict_path(notebook_module: ModuleType) -> str:
    return notebook_module.download_file_if_absent(
        url=VERDICT_URL,
        filename="the-verdict.txt",
        search_dirs=VERDICT_SEARCH_DIRS,
    )


@pytest.fixture(scope="module")
def gpt2_asset_paths(notebook_module: ModuleType) -> dict[str, str]:
    resolved_paths: dict[str, str] = {}
    for filename, url in GPT2_ASSET_URLS.items():
        resolved_paths[filename] = notebook_module.download_file_if_absent(
            url,
            filename,
            GPT2_SEARCH_DIRS,
        )
    return resolved_paths


def test_training_pipeline_creates_expected_vocab(notebook_module: ModuleType, verdict_path: str):
    tokenizer = notebook_module.BPETokenizerSimple()

    with open(verdict_path, "r", encoding="utf-8") as text_file:
        corpus_text = text_file.read()

    tokenizer.train(corpus_text, vocab_size=1000, allowed_special={"<|endoftext|>"})

    assert len(tokenizer.vocab) == 1000
    assert len(tokenizer.bpe_merges) == 742

    sample_text = "Jack embraced beauty through art and life."
    encoded_sample = tokenizer.encode(sample_text)
    # Merge order can vary with corpus / tie-breaking; roundtrip is the invariant.
    assert tokenizer.decode(encoded_sample) == sample_text
    assert all(isinstance(t, int) and 0 <= t < 1000 for t in encoded_sample)

    tokenizer.save_vocab_and_merges(vocab_path="vocab.json", bpe_merges_path="bpe_merges.txt")

    reloaded_tokenizer = notebook_module.BPETokenizerSimple()
    reloaded_tokenizer.load_vocab_and_merges(
        vocab_path="vocab.json",
        bpe_merges_path="bpe_merges.txt",
    )
    assert reloaded_tokenizer.decode(encoded_sample) == sample_text


def test_training_does_not_create_mid_token_space_markers(
    notebook_module: ModuleType,
    verdict_path: str,
):
    tokenizer = notebook_module.BPETokenizerSimple()

    with open(verdict_path, "r", encoding="utf-8") as text_file:
        tokenizer.train(text_file.read(), vocab_size=1000, allowed_special={"<|endoftext|>"})

    invalid_tokens = [
        token
        for token in tokenizer.vocab.values()
        if "Ġ" in token and token != "Ġ" and not token.startswith("Ġ")
    ]
    assert invalid_tokens == []


def test_openai_vocab_load_matches_basic_gpt2_example(
    notebook_module: ModuleType,
    gpt2_asset_paths: dict[str, str],
):
    tokenizer = _build_openai_tokenizer(notebook_module, gpt2_asset_paths)
    assert len(tokenizer.vocab) == 50257
    assert tokenizer.encode("This is some text") == [1212, 318, 617, 2420]


def test_openai_vocab_matches_reference_tokenizer_on_edge_cases(
    notebook_module: ModuleType,
    gpt2_asset_paths: dict[str, str],
):
    tokenizer = _build_openai_tokenizer(notebook_module, gpt2_asset_paths)
    reference_tokenizer = tiktoken.get_encoding("gpt2")

    expectations = {
        "Hello,": [15496, 11],
        "Implementations": [3546, 26908, 602],
        "asdf asdfasdf a!!, @aba 9asdf90asdfk": [
            292,
            7568,
            355,
            7568,
            292,
            7568,
            257,
            3228,
            11,
            2488,
            15498,
            860,
            292,
            7568,
            3829,
            292,
            7568,
            74,
        ],
        "Hello, world. Is this-- a test?": [15496, 11, 995, 13, 1148, 428, 438, 257, 1332, 30],
    }

    mismatches: list[str] = []
    for sample_text, expected_token_ids in expectations.items():
        reference_ids = reference_tokenizer.encode(sample_text)
        learner_ids = tokenizer.encode(sample_text)

        if reference_ids != expected_token_ids:
            mismatches.append(
                f"Reference tokenizer mismatch for {sample_text!r}: expected {expected_token_ids}, got {reference_ids}"
            )
        if learner_ids != expected_token_ids:
            mismatches.append(
                f"Notebook tokenizer mismatch for {sample_text!r}: expected {expected_token_ids}, got {learner_ids}"
            )

    if mismatches:
        pytest.fail("\n".join(mismatches))


def test_newline_and_eot_ids_are_preserved(
    notebook_module: ModuleType,
    gpt2_asset_paths: dict[str, str],
):
    tokenizer = _build_openai_tokenizer(notebook_module, gpt2_asset_paths)

    assert tokenizer.inverse_vocab["Ċ"] == 198
    assert tokenizer.inverse_vocab["<|endoftext|>"] == 50256

    if "\n" not in tokenizer.inverse_vocab:
        tokenizer.inverse_vocab["\n"] = tokenizer.inverse_vocab["Ċ"]

    assert tokenizer.inverse_vocab["\n"] == 198
    assert tokenizer.vocab[198] == "Ċ"
    assert tokenizer.vocab[50256] == "<|endoftext|>"


def test_endoftext_handling_matches_tiktoken(
    notebook_module: ModuleType,
    gpt2_asset_paths: dict[str, str],
):
    tokenizer = _build_openai_tokenizer(notebook_module, gpt2_asset_paths)
    reference_tokenizer = tiktoken.get_encoding("gpt2")
    sample_text = "Hello<|endoftext|>\nworld"

    with pytest.raises(ValueError):
        tokenizer.encode(sample_text)

    learner_ids = tokenizer.encode(sample_text, allowed_special={"<|endoftext|>"})
    reference_ids = reference_tokenizer.encode(sample_text, allowed_special={"<|endoftext|>"})
    assert learner_ids == reference_ids


@pytest.mark.parametrize("sample_text", ["a\nb", "a\n\nb", "\nHello", "Hello\n", "a\r\nb"])
def test_newline_cases_roundtrip_cleanly(
    notebook_module: ModuleType,
    gpt2_asset_paths: dict[str, str],
    sample_text: str,
):
    tokenizer = _build_openai_tokenizer(notebook_module, gpt2_asset_paths)
    reference_tokenizer = tiktoken.get_encoding("gpt2")

    learner_ids = tokenizer.encode(sample_text)
    reference_ids = reference_tokenizer.encode(sample_text)

    assert learner_ids == reference_ids
    assert learner_ids.count(198) == sample_text.count("\n")
    assert tokenizer.decode(learner_ids) == sample_text


def test_space_and_newline_boundary_cases_match_tiktoken(
    notebook_module: ModuleType,
    gpt2_asset_paths: dict[str, str],
):
    tokenizer = _build_openai_tokenizer(notebook_module, gpt2_asset_paths)
    reference_tokenizer = tiktoken.get_encoding("gpt2")

    for sample_text in ["Hello \nworld", "Hello\n world"]:
        assert tokenizer.encode(sample_text) == reference_tokenizer.encode(sample_text)


def test_leading_spaces_survive_roundtrip(
    notebook_module: ModuleType,
    gpt2_asset_paths: dict[str, str],
):
    tokenizer = _build_openai_tokenizer(notebook_module, gpt2_asset_paths)
    sample_text = "  Hello World."
    assert tokenizer.decode(tokenizer.encode(sample_text)) == sample_text
