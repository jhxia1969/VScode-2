import argparse
from pathlib import Path

from bar_chart_demo import generate_bar_chart
from core.calculator import calculate
from core.data_cleaner import clean_csv
from core.file_automation import batch_rename


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="All-in-One Python Toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    calc_parser = subparsers.add_parser("calc", help="Run basic arithmetic")
    calc_parser.add_argument("--op", choices=["add", "sub", "mul", "div"], required=True)
    calc_parser.add_argument("--a", type=float, required=True)
    calc_parser.add_argument("--b", type=float, required=True)

    clean_parser = subparsers.add_parser("clean-csv", help="Clean CSV rows")
    clean_parser.add_argument("--input", required=True)
    clean_parser.add_argument("--output", required=True)

    rename_parser = subparsers.add_parser("batch-rename", help="Batch rename files")
    rename_parser.add_argument("--dir", required=True)
    rename_parser.add_argument("--prefix", required=True)
    rename_parser.add_argument("--start", type=int, default=1)
    rename_parser.add_argument("--ext", default="")
    rename_parser.add_argument("--dry-run", action="store_true")

    subparsers.add_parser("chart", help="Generate a bar chart image")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "calc":
        result = calculate(args.op, args.a, args.b)
        print(result)
        return

    if args.command == "clean-csv":
        in_path = Path(args.input)
        out_path = Path(args.output)
        rows = clean_csv(in_path, out_path)
        print(f"cleaned_rows={rows}")
        return

    if args.command == "batch-rename":
        renamed = batch_rename(
            directory=Path(args.dir),
            prefix=args.prefix,
            start_index=args.start,
            extension_filter=args.ext,
            dry_run=args.dry_run,
        )
        for old_name, new_name in renamed:
            print(f"{old_name} -> {new_name}")
        return

    if args.command == "chart":
        output_file = generate_bar_chart()
        print(f"Bar chart saved to: {output_file}")
        return


if __name__ == "__main__":
    main()
