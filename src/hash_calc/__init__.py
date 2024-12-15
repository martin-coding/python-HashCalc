"""hash-calc package."""

import argparse

from hash_calc import hash_calc


def main() -> None:
    """Jump in point."""
    parser = argparse.ArgumentParser(description="Calculate hash of a given file.")
    parser.add_argument("hash", type=str, help="Type of hash to use.")
    parser.add_argument("path", type=str, help="Path to the file to hash.")
    args = parser.parse_args()

    hash_type: str = args.hash
    file_path: str = args.path

    try:
        hash_data = hash_calc.calculate_hash(hash_type, file_path)
    except NotImplementedError:
        print("Only sha256 is currently implemented")
        return
    except FileNotFoundError:
        print("File not found")
        return

    print(hash_data.hex())


if __name__ == "__main__":
    main()
