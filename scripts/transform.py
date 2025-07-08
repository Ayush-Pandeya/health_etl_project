import pandas as pd

def transform_data(input_path):
    df = pd.read_csv(input_path)
    # Example transform: add BMI column
    df["bmi"] = df["weight"] / ((df["height"] / 100) ** 2)
    transformed_path = "data/transformed_data.csv"
    df.to_csv(transformed_path, index=False)
    print(f" Data transformed and saved to {transformed_path}")
    return transformed_path
