import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.data_loader import load_data, preprocess_data
from src.eda import summarize_data, check_missing_values, correlation_analysis
from src.visualization import plot_histogram, plot_scatter

def main():
    # Load and preprocess data
    df = load_data('../data/cleaned_insurance_data.csv')
    df = preprocess_data(df)
    
    # EDA tasks
    summary = summarize_data(df)
    missing = check_missing_values(df)
    correlation = correlation_analysis(df)
    
    # Visualization tasks
    plot_histogram(df, 'TotalPremium')
    plot_scatter(df, 'TotalPremium', 'TotalClaims', 'PostalCode')
    
    print("EDA complete!")
    
if __name__ == '__main__':
    main()
