import csv
import tempfile
import unittest
from pathlib import Path

from src.core.data_cleaner import clean_csv


class TestDataCleaner(unittest.TestCase):
    def test_clean_csv(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = base / "input.csv"
            target = base / "out" / "output.csv"

            with source.open("w", encoding="utf-8", newline="") as wf:
                writer = csv.writer(wf)
                writer.writerow([" name ", " age "])
                writer.writerow([" alice ", " 20 "])
                writer.writerow(["", ""])

            count = clean_csv(source, target)
            self.assertEqual(count, 2)

            with target.open("r", encoding="utf-8", newline="") as rf:
                reader = list(csv.reader(rf))
                self.assertEqual(reader, [["name", "age"], ["alice", "20"]])


if __name__ == "__main__":
    unittest.main()
