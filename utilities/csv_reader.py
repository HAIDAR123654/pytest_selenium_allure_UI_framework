import csv
from pathlib import Path
from typing import List, Dict

def read_csv(path : Path) -> List[Dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: path={path}")

    with open(path, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)   # Reads rows into dicts using headers
        data = [row for row in reader]
    return data
