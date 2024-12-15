"""Hash helper class."""

import hashlib
from pathlib import Path

BUF_SIZE = 2**16


def calculate_hash(hash_type: str, file: str) -> bytes:
    """Calculate specified hash for a given file."""
    file_path = Path(file)
    if hash_type != "sha256":
        raise NotImplementedError
    if not file_path.exists():
        raise FileNotFoundError

    sha256 = hashlib.sha256()

    with file_path.open("rb") as file_reader:
        while True:
            data = file_reader.read(BUF_SIZE)

            if not data:
                break

            sha256.update(data)
    return sha256.digest()
