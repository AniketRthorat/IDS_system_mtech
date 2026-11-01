from pathlib import Path
import pandas as pd

data_dir = Path(__file__).resolve().parent.parent / "data"
train_file = data_dir / "KDDTrain+.txt"

# Read the first row only to count the fields.
first_row = pd.read_csv(train_file, header=None, nrows=1)

print("Number of fields in each record:", first_row.shape[1])
print("\nValues in the first record:\n")

for index, value in enumerate(first_row.iloc[0], start=1):
    print(f"Field {index}: {value}")