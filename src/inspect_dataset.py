from pathlib import Path

# Project's data folder
data_dir = Path(__file__).resolve().parent.parent / "data"

files = [
    data_dir / "KDDTrain+.txt",
    data_dir / "KDDTest+.txt",
]

for file_path in files:
    print(f"\nFile: {file_path.name}")

    if not file_path.exists():
        print("ERROR: File not found!")
        continue

    print(f"Size: {file_path.stat().st_size:,} bytes")

    with file_path.open("r", encoding="utf-8") as file:
        for i in range(3):
            line = file.readline()
            if not line:
                break
            print(f"Record {i + 1}: {line[:180].strip()} ...")