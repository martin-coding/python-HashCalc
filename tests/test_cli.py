"""Tests for the cli module."""

from pathlib import Path

from hash_calc.hash_calc import calculate_hash


def test_hash_calculation() -> None:
    """Tests function used for hash calculation of files."""
    test_file_path = Path(__file__).parent / "data" / "example_input.bin"

    assert test_file_path.exists()

    assert calculate_hash("sha256", test_file_path).hex() == "3332af3a8d42d4a5eacd0f0bf0d8fa28813df1bd5317ec0522d5265f4a5eb6de"
