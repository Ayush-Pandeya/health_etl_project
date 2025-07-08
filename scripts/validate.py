import pandas as pd

def validate_data(input_path):
    df = pd.read_csv(input_path)
    # Simple validation: check no nulls
    if df.isnull().sum().sum() > 0:
        raise ValueError("Validation failed: null values found")
    print(" Data validation passed")
    return True
