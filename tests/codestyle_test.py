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

def test_conformance():
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
    if result.total_errors == 0:
        print(f"[ Code Style ] : OK")
    else:
        print(f"[ Code Style ] : NO ({result.total_errors} errors)")

if __name__ == "__main__":
    test_conformance()
    