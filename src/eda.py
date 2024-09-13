import pandas as pd

def summarize_data(df):
    """Generate descriptive statistics for numerical columns."""
    return df.describe()

def check_missing_values(df):
    """Check for missing values in the dataset."""
    return df.isnull().sum()

def correlation_analysis(df):
    """Perform correlation analysis for selected numerical features."""
    return df[['TotalPremium', 'TotalClaims']].corr()
