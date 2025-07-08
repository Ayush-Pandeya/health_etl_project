from scripts.validate import validate_data

def test_validate_data():
    transformed_path = "data/transformed_data.csv"
    assert validate_data(transformed_path) is True
