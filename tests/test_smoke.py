"""
Smoke tests to verify basic package structure and imports.

These tests ensure the package can be imported and basic
dependencies are available. They serve as a CI health check.
"""

import sys


def test_python_version():
    """Verify Python version is 3.12+."""
    assert sys.version_info >= (3, 12), "Python 3.12+ required"


def test_core_package_import():
    """Verify the src package can be imported."""
    import src

    assert hasattr(src, "__file__"), "src package should be importable"


def test_pytorch_available():
    """Verify PyTorch is installed and importable."""
    import torch

    assert torch.__version__, "PyTorch should be available"


def test_numpy_available():
    """Verify NumPy is installed and importable."""
    import numpy as np

    assert np.__version__, "NumPy should be available"


def test_tiktoken_available():
    """Verify tiktoken tokenizer is installed."""
    import tiktoken

    assert tiktoken.__version__, "tiktoken should be available"
