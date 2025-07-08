from scripts.extract import extract_data
import os

def test_extract_data():
    path = extract_data()
    assert os.path.exists(path)
