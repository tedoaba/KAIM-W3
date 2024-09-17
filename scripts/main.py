import os
import sys
import pandas as pd

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from data_loader import load_data, display_basic_info, print_unique_values, handle_missing_values, get_numerical_columns
from eda import check_missing_values, data_compression
from visualization import plot_postalcode_premium, plot_categorical_bars, plot_premium_vs_claims, plot_missing_values, plot_histograms, plot_categorical_bars, plot_correlation_matrix

def main():
    # Data Collection
    file_path = '../data/cleaned_insurance_data.csv'
    df = load_data(file_path)
    
    # Display basic information about the dataset
    display_basic_info(df)
    print_unique_values(df)

    # EDA
    check_missing_values(df)
    plot_missing_values(df)
    plot_histograms(df)
    plot_categorical_bars(df)
    plot_correlation_matrix(df)

    # Data Preprocessing
    df = handle_missing_values(df)
    numerical_cols = get_numerical_columns(df)
    print("Updated Numerical Columns List:")
    print(numerical_cols)

    data_compression(df)

    # Visualizations
    plot_postalcode_premium(df)
    plot_premium_vs_claims(df)

if __name__ == "__main__":
    main()