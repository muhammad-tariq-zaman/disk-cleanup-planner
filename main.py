"""Plan disk cleanup from a file scan CSV.

Usage: python3 main.py scan.csv [--stale-days 90]
CSV columns: path,size_mb,last_access_days,type.
Files not accessed for more than stale-days are reclaimable. Report
reclaimable space per type, largest first, plus the grand total.
"""
import argparse, csv, sys
from collections import defaultdict


def plan(rows, stale_days):
    totals = defaultdict(float)
    for row in rows:
        if int(row["last_access_days"]) > stale_days:
            totals[row["type"].strip()] += float(row["size_mb"])
    return sorted(totals.items(), key=lambda kv: -kv[1])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--stale-days", type=int, default=90)
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        result = plan(list(csv.DictReader(f)), args.stale_days)
    total = 0.0
    for ftype, size in result:
        total += size
        print(f"{ftype}: {size:.0f} MB reclaimable")
    print(f"Total reclaimable: {total:.0f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
