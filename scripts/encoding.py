import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
def encode_categorical_data(df, columns, encoding_type='onehot'):
    """
    Encodes the categorical columns in the dataframe using one-hot encoding or label encoding.

    Parameters:
    df (pd.DataFrame): The input dataframe.
    columns (list): List of column names to encode.
    encoding_type (str): Type of encoding to apply, either 'onehot' or 'label'. Default is 'onehot'.

    Returns:
    pd.DataFrame: Dataframe with encoded categorical columns.
    """
    df_encoded = df.copy()

    if encoding_type == 'onehot':
        # Apply one-hot encoding without dropping the first category
        df_encoded = pd.get_dummies(df_encoded, columns=columns,prefix='ohe',prefix_sep='_',drop_first=True,dtype=int)
        return df_encoded
    elif encoding_type == 'label':
        # Apply label encoding
        label_encoder = LabelEncoder()
        for col in columns:
            df_encoded[col] = label_encoder.fit_transform(df_encoded[col])
        return df_encoded
    else:
        raise ValueError("encoding_type must be either 'onehot' or 'label'")
    
    




def split_train_test(data, features, target, test_size=0.3, random_state=None):
    """
    Splits the data into training and test sets.
    
    Parameters:
    - data (pd.DataFrame): The full dataset.
    - features (list): List of feature column names.
    - target (str): The target column name.
    - test_size (float): Proportion of the dataset to include in the test split (default is 0.3 for 70:30 split).
    - random_state (int, optional): Controls the shuffling applied to the data before applying the split.
    
    Returns:
    - X_train, X_test, y_train, y_test: Split feature and target data.
    """
    X = data[features]
    y = data[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    return X_train, X_test, y_train, y_test

# Example usage:
# features = ['feature1', 'feature2', 'feature3']
# target = 'target_column'
# X_train, X_test, y_train, y_test = split_train_test(df_encoded, features, target, test_size=0.2, random_state=42)
