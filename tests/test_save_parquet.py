from scripts.save_parquet import save_to_parquet
import os

def test_save_to_parquet():
    transformed_path = "data/transformed_data.csv"
    path = save_to_parquet(transformed_path)
    assert os.path.exists(path)
