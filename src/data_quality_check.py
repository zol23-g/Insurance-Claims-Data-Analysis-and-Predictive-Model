import pandas as pd

class DataQualityCheck:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    
    def load_data(self):
        self.data = pd.read_csv(self.file_path, sep='|', low_memory=False)
        return self.data
    
    def basic_info(self):
        if self.data is not None:
            print(self.data.info())
            print(self.data.describe())
        else:
            print("Data not loaded. Call the `load_data` method first.")
    
def missing_values_summary(df):
    """
    This function takes a pandas DataFrame and returns a summary of missing values,
    sorted by the percentage of missing values in descending order.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to check for missing values.
    
    Returns:
    pd.DataFrame: A DataFrame with the count and percentage of missing values for each column, sorted by percentage.
    """
    # Calculate the number of missing values for each column
    missing_count = df.isnull().sum()
    
    # Calculate the percentage of missing values for each column
    missing_percentage = (missing_count / len(df)) * 100
    
    # Create a summary DataFrame
    missing_summary = pd.DataFrame({
        'Missing Values': missing_count,
        'Percentage': missing_percentage
    })
    
    # Sort the summary DataFrame by the percentage of missing values in descending order
    missing_summary = missing_summary.sort_values(by='Percentage', ascending=False)
    
    return missing_summary