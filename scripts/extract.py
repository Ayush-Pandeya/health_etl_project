import pandas as pd

def extract_data():
    # Simulate extracting raw CSV data
    data = {
        "id": [1, 2, 3],
        "age": [25, 30, 45],
        "weight": [70, 80, 90],
        "height": [175, 180, 178]
    }
    df = pd.DataFrame(data)
    raw_path = "data/raw_data.csv"
    df.to_csv(raw_path, index=False)
    print(f" Data extracted to {raw_path}")
    return raw_path
