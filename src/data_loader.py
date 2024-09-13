import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path, delimiter='|')

def preprocess_data(df):
    """Perform basic preprocessing tasks such as handling missing values."""
    df.fillna('Unknown', inplace=True)
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    return df
