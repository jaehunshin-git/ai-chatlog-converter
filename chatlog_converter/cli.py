import argparse
from pathlib import Path

from .parser import convert_file_to_json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert conversation HTML to JSON (scheme.json format)")
    parser.add_argument("-i", "--input", required=True, help="Path to input HTML file")
    parser.add_argument("-o", "--output", required=True, help="Path to output JSON file")
    args = parser.parse_args(args=argv)

    in_path = Path(args.input)
    out_path = Path(args.output)
    if not in_path.exists():
        parser.error(f"Input file not found: {in_path}")

    convert_file_to_json(in_path, out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
