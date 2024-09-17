import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def check_missing_values(df):
    print(df.isnull().sum())
    return df.isnull().sum()

def describe_data(df):
    return df.describe()
    
def data_compression(df):
    """Compress the DataFrame to reduce memory usage."""
    initial_memory = df.memory_usage().sum() / (1024 ** 2)
    print(f"Initial memory usage: {initial_memory:.2f} MB")
    
    for col in df.columns:
        col_type = df[col].dtype
        if col_type == 'object':
            df[col] = df[col].astype('category')
        elif col_type in ['int64', 'float64']:
            df[col] = pd.to_numeric(df[col], downcast='integer' if col_type == 'int64' else 'float')
    
    final_memory = df.memory_usage().sum() / (1024 ** 2)
    print(f"Final memory usage: {final_memory:.2f} MB")
    print(f"Reduced memory usage by: {initial_memory - final_memory:.2f} MB")