import matplotlib.pyplot as plt
import seaborn as sns

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
