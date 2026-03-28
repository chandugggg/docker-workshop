import sys
import pandas as pd

month = int(sys.argv[1])
print(f'Hello pipeline, month={month}')

df = pd.DataFrame({"Day": [1, 2], "num_passengers": [3, 4]}) 
df["month"] = month
print(df.head())

df.to_parquet(f"output_{month}")