"""Evaluator-only, synthetic fixtures. Usage: python checks.py SNAPSHOT/output"""
import importlib.util, json, pathlib, sys, unittest
sys.dont_write_bytecode = True
WEIGHTS = {"M1": 30, "M2": 25, "M3": 15, "O1": 10, "O2": 10, "O3": 10}
path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "output") / "stock_csv.py"
try:
    spec = importlib.util.spec_from_file_location("candidate", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
except Exception as error:
    print(json.dumps({"total": 0, "categories": {k: 0 for k in WEIGHTS}, "load_error": f"{type(error).__name__}: {error}"}))
    sys.exit(0)
def row(sku, quantity, location): return {"sku": sku, "quantity": quantity, "location": location}
class Checks(unittest.TestCase):
    def test_M1(self):
        self.assertEqual(m.read_stock('\ufeff\r\n location ,sku, quantity\r\n"north, hall", A , +02\r\n"dock\n2",B,-3\r\n,,\r\n'), [row("A", 2, "north, hall"), row("B", -3, "dock\n2")])
        self.assertEqual(m.read_stock(" \n\r\n"), []); self.assertEqual(m.read_stock("sku,quantity,location\nC,0,west\n"), [row("C", 0, "west")])
        for text in [None, "sku,sku,location\nA,1,w\n", "sku,quantity,extra\nA,1,w\n", "sku,quantity,location\nA,1\n", "sku,quantity,location\n,1,w\n", "sku,quantity,location\nA,1, \n", "sku,quantity,location\nA,1.0,w\n", "sku,quantity,location\nA,١,w\n", 'sku,quantity,location\n"A,1,w\n']:
            with self.assertRaises(ValueError): m.read_stock(text)
    def test_M2(self):
        rows = [row("A", 5, "west"), row("A", -2, "west"), row("A", 4, "east"), row("B", 1, "west"), row("B", -1, "west"), row("C", -3, "west")]
        before = [r.copy() for r in rows]
        self.assertEqual(m.totals(iter(rows)), {("A", "west"): 3, ("A", "east"): 4, ("B", "west"): 0, ("C", "west"): -3})
        self.assertEqual(rows, before); self.assertEqual(m.totals([]), {})
    def test_M3(self):
        rows = [row("A", 5, "west"), row("A", -2, "west"), row("A", -8, "east"), row("A", 2, "north"), row("B", 20, "west")]
        before = [r.copy() for r in rows]
        self.assertEqual(m.available(iter(rows), "A"), 5)
        self.assertEqual(m.available(rows, "missing"), 0); self.assertEqual(rows, before)
    def test_O1(self):
        rows = [row("B", -4, "west"), row("A", -2, "east"), row("B", 1, "west"), row("A", 2, "east"), row("A", -1, "west")]
        before = [r.copy() for r in rows]
        self.assertEqual(m.shortages(iter(rows)), [("A", "west", 1), ("B", "west", 3)])
        self.assertEqual(m.shortages([]), []); self.assertEqual(rows, before)
    def test_O2(self):
        rows = [row('A,"x"', -2, "dock\n2"), row("B", 0, "west")]; before = [r.copy() for r in rows]
        self.assertEqual(m.write_stock(iter(rows)), 'sku,quantity,location\n"A,""x""",-2,"dock\n2"\nB,0,west\n')
        self.assertEqual(m.write_stock([]), "sku,quantity,location\n"); self.assertEqual(rows, before)
    def test_O3(self):
        rows = [row("A", 5, "west"), row("A", -2, "west")]; before = [r.copy() for r in rows]
        moved = m.transfer(iter(rows), "A", "west", "east", 3)
        self.assertEqual(moved, before + [row("A", -3, "west"), row("A", 3, "east")])
        moved[0]["quantity"] = 99; self.assertEqual(rows, before)
        for args in [("A", "west", "east", 4), ("A", "west", "west", 1), ("A", "west", "east", 0), ("A", "west", "east", True), ("A", "west", "east", 1.5), ("", "west", "east", 1), ("A", None, "east", 1), ("A", "west", "", 1)]:
            with self.assertRaises(ValueError): m.transfer(rows, *args)
        self.assertEqual(rows, before)
if __name__ == "__main__":
    categories, failures = {}, {}
    for category, points in WEIGHTS.items():
        result = unittest.TestResult(); Checks("test_" + category).run(result)
        categories[category] = points if result.wasSuccessful() else 0
        failures[category] = [trace for _, trace in result.failures + result.errors]
    print(json.dumps({"total": sum(categories.values()), "categories": categories, "failures": failures}, sort_keys=True))
