"""Evaluator-only, synthetic fixtures. Usage: python checks.py SNAPSHOT/output"""
import importlib.util, json, pathlib, sys, unittest
sys.dont_write_bytecode = True
WEIGHTS = {"M1": 30, "M2": 25, "M3": 15, "O1": 10, "O2": 10, "O3": 10}
path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "output") / "service_windows.py"
try:
    spec = importlib.util.spec_from_file_location("candidate", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
except Exception as error:
    print(json.dumps({"total": 0, "categories": {k: 0 for k in WEIGHTS}, "load_error": f"{type(error).__name__}: {error}"}))
    sys.exit(0)
class Checks(unittest.TestCase):
    def test_M1(self):
        for s, n in [("00:00", 0), ("09:05", 545), ("23:59", 1439)]:
            self.assertEqual(m.parse_minute(s), n)
        for s in ["9:00", "00:60", "24:00", "-1:00", " 09:00", "01:00\n", "٠١:00", "01:٢٣", 9, None]:
            with self.assertRaises(ValueError): m.parse_minute(s)
    def test_M2(self):
        rows = [[60, 90], [10, 30], [0, 20], [5, 10], [90, 100], [10, 30]]
        self.assertEqual(m.merge_windows(rows), [(0, 30), (60, 100)])
        self.assertEqual(rows, [[60, 90], [10, 30], [0, 20], [5, 10], [90, 100], [10, 30]])
        self.assertEqual(m.merge_windows(iter([(0, 1440)])), [(0, 1440)]); self.assertEqual(m.merge_windows([]), [])
        for pair in [(-1, 2), (3, 3), (2, 1441), (True, 3), (1.5, 3), (1,), (1, 2, 3), "12"]:
            with self.assertRaises(ValueError): m.merge_windows([pair])
    def test_M3(self):
        rows = [[20, 40], [10, 30], [40, 50], [22, 25]]
        self.assertEqual(m.total_minutes(iter(rows)), 40)
        self.assertEqual(rows, [[20, 40], [10, 30], [40, 50], [22, 25]])
        self.assertEqual(m.total_minutes([]), 0)
        with self.assertRaises(ValueError): m.total_minutes([(5, 3)])
    def test_O1(self):
        for minute, want in [(0, False), (10, True), (19, True), (20, False)]:
            self.assertIs(m.contains_minute(iter([(10, 20)]), minute), want)
        self.assertIs(m.contains_minute([], 5), False)
        for minute in [True, -1, 1440, 1.5, "10"]:
            with self.assertRaises(ValueError): m.contains_minute([], minute)
        with self.assertRaises(ValueError): m.contains_minute([(0, 20), (5, 3)], 10)
    def test_O2(self):
        self.assertEqual(m.gap_windows(iter([(0, 8), (12, 15), (14, 25), (35, 40)]), 5, 30), [(8, 12), (25, 30)])
        self.assertEqual(m.gap_windows([], 0, 1440), [(0, 1440)])
        self.assertEqual(m.gap_windows([(0, 1440)], 50, 50), [])
        for bounds in [(-1, 10), (11, 10), (0, 1441), (True, 10), (0, 1.5)]:
            with self.assertRaises(ValueError): m.gap_windows([], *bounds)
        with self.assertRaises(ValueError): m.gap_windows([(5, 3)], 50, 50)
    def test_O3(self):
        for minute, want in [(0, "00:00"), (545, "09:05"), (1439, "23:59"), (1440, "24:00")]:
            self.assertEqual(m.format_minute(minute), want)
        for minute in [True, -1, 1441, 1.5, "10"]:
            with self.assertRaises(ValueError): m.format_minute(minute)
if __name__ == "__main__":
    categories, failures = {}, {}
    for category, points in WEIGHTS.items():
        result = unittest.TestResult(); Checks("test_" + category).run(result)
        categories[category] = points if result.wasSuccessful() else 0
        failures[category] = [trace for _, trace in result.failures + result.errors]
    print(json.dumps({"total": sum(categories.values()), "categories": categories, "failures": failures}, sort_keys=True))
