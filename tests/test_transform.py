from scripts.transform import transform_data
import os

def test_transform_data():
    raw_path = "data/raw_data.csv"
    path = transform_data(raw_path)
    assert os.path.exists(path)
