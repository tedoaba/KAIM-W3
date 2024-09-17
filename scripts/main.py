import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pandas as pd
from data_loader import load_data, preprocess_data, display_basic_info, print_unique_values
from eda import summarize_data, check_missing_values, correlation_analysis, handle_missing_values, get_numerical_columns, correlation_analysis, data_compression
from visualization import plot_histogram, plot_scatter, plot_missing_values, plot_histograms, plot_categorical_bars, plot_correlation_matrix, plot_postalcode_premium, plot_premium_vs_claims

def main():
    # Data Collection
    file_path = '../data/cleaned_insurance_data.csv'
    df = load_data(file_path)
    
    #df = preprocess_data(df)
    
    # EDA tasks
    #summary = summarize_data(df)
    #missing = check_missing_values(df)
    #correlation = correlation_analysis(df)
    
    # Visualization tasks
    #plot_histogram(df, 'TotalPremium')
    #plot_scatter(df, 'TotalPremium', 'TotalClaims', 'PostalCode')
    
    #print("EDA complete!")
    
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
    
if __name__ == '__main__':
    main()
