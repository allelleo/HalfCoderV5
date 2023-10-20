"""Тест на пеп-8."""

import unittest
import pycodestyle
from pathlib import Path

def generate_command():
    directory = Path(r"D:\HalfCoder.v5\src")
    line_count = 0
    files = []
    for f in directory.rglob("*.py"):
        if not f.is_file() or not f.exists():
            continue

        files.append(str(f))
    
    return "pycodestyle " + " ".join(map(str, files))

class TestCodeFormat(unittest.TestCase):
    """Базовый класс для тестирования кода на соответсвие."""
    
    def test_conformance(self):
        """Проверка кода на соответсвие PEP-8."""
        #print(generate_command())
        directory = Path(r"D:\HalfCoder.v5\src")
        line_count = 0
        files = []
        for f in directory.rglob("*.py"):
            if not f.is_file() or not f.exists():
                continue

            files.append(str(f))
        
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
