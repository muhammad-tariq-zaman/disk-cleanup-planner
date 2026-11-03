# disk-cleanup-planner

Turn a file-scan CSV into a cleanup plan: reclaimable space per file type for files untouched longer than the stale threshold, largest first.

## How to run

```sh
python3 main.py scan.csv --stale-days 90
```

## Example output

```
log: 750 MB reclaimable
tmp: 120 MB reclaimable
Total reclaimable: 870 MB
```

Standard library only. Run the tests with `python3 -m unittest discover`.
