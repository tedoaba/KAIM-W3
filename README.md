
# KAIM Weak 3 Challenges Task 1

## AlphaCare Insurance Solutions (ACIS) Marketing Analytics Repository

Welcome to the AlphaCare Insurance Solutions (ACIS) Marketing Analytics Repository! This repository contains the code, data, models, and analysis related to our project aimed at optimizing marketing strategies and identifying low-risk targets for potential premium reductions in the South African car insurance market.

## Project Overview

Our primary objective is to leverage historical insurance claim data to perform predictive and risk analytics. By employing statistical modeling, machine learning, and hypothesis testing, we aim to:

- Identify low-risk customer segments for premium optimization.
- Explore geographic and demographic trends.
- Optimize marketing strategies by understanding feature impacts on customer behavior.

This repository is divided into four key branches, each representing a distinct task. Below is an outline of the different branches, tasks, methodologies, and tools used.

## Branch Overview

### 1. `task-1` - Exploratory Data Analysis (EDA)

**Objective**: Conduct thorough exploratory data analysis to understand the distribution and relationships within the data, detect outliers, and identify trends across different regions and customer groups.

**Key Tasks**:
- **Data Summarization**: Descriptive statistics for numerical features such as `TotalPremium`, `TotalClaim`, etc.
- **Data Structure**: Review column formats and check for missing values.
- **Univariate & Bivariate Analysis**: Analyze variable distributions and relationships using visualizations such as histograms, bar charts, scatter plots, and correlation matrices.
- **Geographic Trend Comparison**: Analyze trends by geography, such as premium types and vehicle makes across regions.
- **Outlier Detection**: Use box plots to identify outliers in numerical data.
- **Visualization**: Create three insightful visualizations to highlight key findings.

## Project Structure Overview

```bash

├── .github/
│   └── workflows
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   ├── data_loader.py        # Module to load and preprocess data
│   ├── eda.py                # Module to handle EDA tasks
│   └── visualization.py      # Module for plotting and visualization
├── notebooks/
│   ├── __init__.py
│   └── Kaim_week_3_task-1.ipynb  
├── tests/
│   ├── __init__.py
│   ├── test_data_loader.py   # Unit tests for data_loader.py
│   ├── test_eda.py           # Unit tests for eda.py
│   └── test_visualization.py # Unit tests for visualization.py
└── scripts/
    ├── __init__.py
    └── main.py            # Script to run EDA from command line

```


## How to Get Started

### Prerequisites

- Python 3.8+
- Libraries: `pandas`, `numpy`, `matplotlib`, `scikit-learn`, `xgboost`, `dvc`, `shap`, `lime`, `seaborn`, etc.
- Jupyter Notebook for running the analysis.
- DVC for data version control.

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tedoaba/KAIM-W3.git
   cd KAIM-W3
   git checkout task-1
   ```

2. **Install Dependencies**
3. **Set up DVC (if working on task-2)**
4. **Run Notebooks**

## Key Insights and Recommendations

- **Risk Analysis**: Early insights suggest significant risk differences between provinces and gender groups, which could be used to tailor marketing strategies and adjust premiums.
- **Geographic Trends**: Zipcode-level analysis shows disparities in claim rates and insurance types, suggesting location-based pricing strategies.
- **Predictive Modeling**: Random Forest and XGBoost models showed strong predictive power for total claims, with features such as car age and geographic location being the most important predictors.

## Conclusion

This project provides actionable insights to optimize marketing strategies, improve customer segmentation, and enhance premium pricing models for AlphaCare Insurance Solutions. By leveraging data analytics, statistical testing, and machine learning, we aim to drive business growth and customer satisfaction.

Thank you for using this repository! For any issues or contributions, please feel free to submit a pull request or contact the project maintainers.
