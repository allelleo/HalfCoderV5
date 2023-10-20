import unittest
from pathlib import Path
from pydocstyle import check

class TestCodeFormat(unittest.TestCase):
    def test_conformance(self):
        directory = Path(r"D:\HalfCoder.v5\src")
        line_count = 0
        files = []
        for f in directory.rglob("*.py"):
            if not f.is_file() or not f.exists():
                continue

            files.append(str(f))

        checks = check(files)
        count = 0
        for i in checks:
            print(i)
            count += 1
        self.assertEqual(count, 0, "Found document style errors (and warnings).")

if __name__ == "__main__":
    unittest.main()