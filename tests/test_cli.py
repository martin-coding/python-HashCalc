"""Tests for the cli module."""

from pathlib import Path

from hash_calc.hash_calc import calculate_hash


def test_hash_calculation() -> None:
    """Tests function used for hash calculation of files."""
    test_file_path = Path(__file__).parent / "data" / "example_input.txt"

    assert test_file_path.exists()

    assert calculate_hash("sha256", test_file_path).hex() == "c98c24b677eff44860afea6f493bbaec5bb1c4cbb209c6fc2bbb47f66ff2ad31"
