import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """
    df = pd.read_csv(filepath)
    return df

# Test function execution
if __name__ == "__main__":
    filepath = "data/titanic.csv"
    titanic_data = load_titanic_data(filepath)
    print(titanic_data.head())  # Display the first few rows of the dataset