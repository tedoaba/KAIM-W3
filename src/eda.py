import pandas as pd
import matplotlib.pyplot as plt

def handle_missing_values(df):
    # Drop columns with very high missing values
    cols_to_drop = ['NumberOfVehiclesInFleet', 'CrossBorder', 'CustomValueEstimate', 
                    'Converted', 'Rebuilt', 'WrittenOff']
    df = df.drop(columns=cols_to_drop)

    # Impute categorical columns
    categorical_cols = ['NewVehicle', 'AccountType', 'Bank', 'VehicleType', 
                        'make', 'Model', 'mmcode', 'bodytype']
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Impute numerical columns
    numerical_cols = ['cubiccapacity', 'kilowatts', 'Cylinders', 'NumberOfDoors']
    for col in numerical_cols:
        df[col].fillna(df[col].mean(), inplace=True)

    # Drop rows with missing values in a specific column
    df.dropna(subset=['CapitalOutstanding'], inplace=True)
    
    # Drop additional columns
    columns_to_drop = ['NewVehicle', 'VehicleType', 'make', 'Model', 
                       'bodytype', 'Cylinders', 'cubiccapacity', 'RegistrationYear', 
                       'VehicleIntroDate', 'kilowatts', 'NumberOfDoors']
    df = df.drop(columns=columns_to_drop)

    # Remove duplicates
    df = df.drop_duplicates()

    # Reset index
    df = df.reset_index(drop=True)

    return df

def get_numerical_columns(df):
    return df.select_dtypes(include=['float64', 'int64']).columns.tolist()

def summarize_data(df):
    """Generate descriptive statistics for numerical columns."""
    return df.describe()

def check_missing_values(df):
    """Check for missing values in the dataset."""
    return df.isnull().sum()

def correlation_analysis(df):
    """Perform correlation analysis for selected numerical features."""
    return df[['TotalPremium', 'TotalClaims']].corr()

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