from pathlib import Path
from pydocstyle import check

def test_conformance():
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
    if count ==  0:
        print(f"[ Code Docs ] : OK")
    else:
        print(f"[ Code Docs ] : NO ({count} errors)")