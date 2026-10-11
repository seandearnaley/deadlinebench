"""Minimal public smoke/regression tests for a synthetic fixture."""
import importlib.util
from pathlib import Path
import unittest

path = Path("output/service_windows.py")
if not path.exists():
    path = Path(__file__).with_name("service_windows.py")
spec = importlib.util.spec_from_file_location("service_windows", path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class VisibleTests(unittest.TestCase):
    def test_clock(self):
        self.assertEqual(m.parse_minute("09:05"), 545)

    def test_separate_windows(self):
        self.assertEqual(m.merge_windows([(30, 40), (10, 20)]), [(10, 20), (30, 40)])

    def test_union_regression(self):
        self.assertEqual(m.total_minutes([(10, 30), (20, 40)]), 30)


if __name__ == "__main__":
    unittest.main()
