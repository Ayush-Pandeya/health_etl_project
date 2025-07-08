import os
import pandas as pd

def save_to_parquet(input_path):
    df = pd.read_csv(input_path)
    os.makedirs("data", exist_ok=True)
    parquet_path = "data/final_data.parquet"
    df.to_parquet(parquet_path)
    print(f" Parquet file saved to {parquet_path}")
    return parquet_path
