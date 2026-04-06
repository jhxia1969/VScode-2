import csv
from pathlib import Path


def clean_csv(input_path: Path, output_path: Path) -> int:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    cleaned_rows = []
    with input_path.open("r", encoding="utf-8", newline="") as rf:
        reader = csv.reader(rf)
        for row in reader:
            normalized = [cell.strip() for cell in row]
            if any(cell for cell in normalized):
                cleaned_rows.append(normalized)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as wf:
        writer = csv.writer(wf)
        writer.writerows(cleaned_rows)

    return len(cleaned_rows)
