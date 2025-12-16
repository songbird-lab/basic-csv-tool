# Simple csv summarizer

import pandas as pd

file = input ("Enter CSV file path: ")
df = pd.read_csv(file)

print(f"\nColumns: {list(df.columns)}")
print(f"Number of rows: {len(df)}")
print("\nFirst 5 rows:")
print(df.head())
