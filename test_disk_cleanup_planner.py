import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import plan


def row(t, size, days):
    return {"path": "/x", "size_mb": str(size), "last_access_days": str(days), "type": t}


class TestCleanupPlanner(unittest.TestCase):
    def test_stale_files_counted(self):
        self.assertEqual(plan([row("tmp", 100, 120)], 90), [("tmp", 100.0)])

    def test_fresh_files_excluded(self):
        self.assertEqual(plan([row("tmp", 100, 10)], 90), [])

    def test_grouped_by_type(self):
        result = dict(plan([row("log", 50, 200), row("log", 25, 200)], 90))
        self.assertEqual(result["log"], 75.0)

    def test_largest_first(self):
        result = plan([row("a", 10, 200), row("b", 99, 200)], 90)
        self.assertEqual(result[0][0], "b")
