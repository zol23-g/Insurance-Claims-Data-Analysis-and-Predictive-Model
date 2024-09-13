# Insurance Claims Data Analysis

This project performs exploratory data analysis (EDA) and visualization on a dataset of 1,000,098 insurance records. The analysis aims to uncover relationships between variables like car details, plan details, total claims, and total premiums to assess insurance performance.

## Dataset Overview
- **Total records**: 1,000,098
- **Columns**: 52 (Categorical and Numerical)
- **Key Features**:
  - **Demographic**: Citizenship, Gender, MaritalStatus, etc.
  - **Car Information**: Make, Model, Cylinders, RegistrationYear, etc.
  - **Plan Information**: SumInsured, CoverType, TermFrequency, etc.
  - **Target Variables**: TotalPremium, TotalClaims

## Project Goals
1. **Data Cleaning**: Handle missing values and inconsistent data.
2. **Exploratory Data Analysis (EDA)**: 
   - Explore relationships between key columns (e.g., Claims vs Premium).
   - Visualize insights using histograms, scatter plots, and bar charts.
3. **Performance Metrics**:
   - Calculate metrics like **Loss Ratio**, **Claims Frequency**, and **Claims Severity**.
   - Group analysis by categories like VehicleType and CoverType.

## Key Metrics
- **Loss Ratio** = Total Claims / Total Premium
- **Claims Frequency** = Total Claims / Number of Policies
- **Claims Severity** = Total Claims / Number of Claims

## Tools Used
- **Python**: pandas, seaborn, matplotlib
- **Jupyter Notebooks** for analysis and visualization
- **Seaborn/Matplotlib** for data visualization

## Visualizations
- Scatter plots for Claims vs Premium
- Bar charts for categorical distribution
- Histograms for numerical feature analysis

## How to Run
1. Clone this repository.
   ```bash
   git clone https://github.com/zol23-g/Insurance-Claims-Data-Analysis-and-Predictive-Model.git
2. Install dependencies
   pip install -r requirements.txt
3. Run the Jupyter Notebook