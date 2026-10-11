"""Minimal public smoke/regression tests for a synthetic fixture."""
import importlib.util
from pathlib import Path
import unittest

path = Path("output/stock_csv.py")
if not path.exists():
    path = Path(__file__).with_name("stock_csv.py")
spec = importlib.util.spec_from_file_location("stock_csv", path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class VisibleTests(unittest.TestCase):
    def test_csv(self):
        self.assertEqual(m.read_stock("sku,quantity,location\nA,2,west\n"),
                         [{"sku": "A", "quantity": 2, "location": "west"}])

    def test_missing_sku(self):
        self.assertEqual(m.available([], "A"), 0)

    def test_duplicate_adjustments(self):
        rows = [{"sku": "A", "quantity": 5, "location": "west"},
                {"sku": "A", "quantity": -2, "location": "west"}]
        self.assertEqual(m.totals(rows), {("A", "west"): 3})


if __name__ == "__main__":
    unittest.main()
