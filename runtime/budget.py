from __future__ import annotations

from pathlib import Path

ESTIMATE_METHOD = "utf8_bytes_div_4"

DEFAULT_MODULE_BUDGETS = {
    "quick": 1200,
    "standard": 5000,
    "deep": 10000,
    "exhaustive": 18000,
}


def estimate_text_tokens(text: str) -> int:
    """Return a transparent tokenizer-free estimate.

    This is deliberately labeled as an estimate. Host adapters may replace it with an
    exact tokenizer, but the portable runtime has no mandatory tokenizer dependency.
    """
    return max(1, round(len(text.encode("utf-8")) / 4))


def estimate_file_tokens(path: Path) -> int:
    return max(1, round(path.stat().st_size / 4))
