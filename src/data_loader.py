import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path, delimiter='|')

def display_basic_info(df):
    print("Data Overview")
    print(df.head())
    print(f"Shape: {df.shape}")
    df.info()
    print(df.columns)

def print_unique_values(df):
    for column in df.columns:
        print(f"Unique values for column '{column}':")
        print(df[column].unique())
        print() 