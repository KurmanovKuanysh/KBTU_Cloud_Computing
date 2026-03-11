import csv

def parse_csv(path: str) -> list[dict]:
    rows = []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(dict(row))
    except (FileNotFoundError, csv.Error):
        return []
    return rows