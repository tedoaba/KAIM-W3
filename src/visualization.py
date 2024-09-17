import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_histogram(df, column_name):
    """Plot a histogram for a numerical column."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column_name], bins=30, kde=True)
    plt.title(f'Distribution of {column_name}')
    plt.show()

def plot_scatter(df, x_col, y_col, hue_col):
    """Plot a scatter plot between two numerical variables."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col)
    plt.title(f'{x_col} vs {y_col} by {hue_col}')
    plt.show()

def plot_missing_values(df):
    missing_counts = df.isnull().sum()
    columns_with_missing = missing_counts[missing_counts > 0]
    
    if len(columns_with_missing) == 0:
        print("No missing values.")
        return
    
    missing_values_df = pd.DataFrame({
        'Column': columns_with_missing.index,
        'Missing Values': columns_with_missing.values
    })

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    table = ax.table(
        cellText=missing_values_df.values,
        colLabels=['Column', 'Missing Values'],
        cellLoc='center',
        loc='center',
        cellColours=[['lightgrey'] * 2] * len(missing_values_df),
        colColours=['#d9d9d9'] * 2
    )
    plt.title('Columns with Missing Values', fontsize=14)
    plt.show()

def plot_histograms(df):
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    plt.figure(figsize=(16, 12))
    for i, col in enumerate(numerical_cols):
        plt.subplot(4, 4, i + 1)
        sns.histplot(df[col].dropna(), bins=20, kde=False)
        plt.title(col)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def plot_categorical_bars(df):
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col].value_counts().plot(kind='bar', figsize=(10, 5))
        plt.title(f'Distribution of {col}')
        plt.show()

def plot_correlation_matrix(df):
    correlation_matrix = df[['TotalPremium', 'TotalClaims', 'PostalCode']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def plot_postalcode_premium(df):
    premium_by_postalcode = df.groupby('PostalCode')['TotalPremium'].mean().sort_values()
    plt.figure(figsize=(10, 15))
    premium_by_postalcode.plot(kind='barh', color='skyblue')
    plt.title('Average Total Premium by Postal Code')
    plt.xlabel('Average Premium')
    plt.ylabel('PostalCode')
    plt.yticks(fontsize=8)
    plt.tight_layout()
    plt.show()

def plot_premium_vs_claims(df):
    plt.figure(figsize=(10, 6))
    sns.regplot(x='TotalPremium', y='TotalClaims', data=df, scatter_kws={'alpha':0.3})
    plt.title('Correlation Between Premium and Claims')
    plt.xlabel('Total Premium')
    plt.ylabel('Total Claims')
    plt.show()