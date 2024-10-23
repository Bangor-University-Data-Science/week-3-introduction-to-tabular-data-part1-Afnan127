import pandas as pd

def get_numerical_df(df, numerical_features):
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    numerical_df = df[numerical_features].copy()
    
    return numerical_df

# Example usage
if __name__ == "__main__":
    
    filepath = "data/titanic.csv" 
    titanic_data = pd.read_csv(filepath)

    numerical_features = ['Age', 'Fare']

    numerical_df = get_numerical_df(titanic_data, numerical_features)
    print(numerical_df.head())