import pandas as pd

def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    # Create a summary dictionary
    summary_data = {
        'Feature Name': df.columns,
        'Data Type': df.dtypes,
        'Number of Unique Values': [df[col].nunique() for col in df.columns],
        'Missing Values': [df[col].isnull().sum() for col in df.columns]
    }
    
    summary_df = pd.DataFrame(summary_data)
    
    summary_df['Has Missing Values'] = summary_df['Missing Values'].apply(lambda x: 'Yes' if x > 0 else 'No')
    
    summary_df.drop(columns='Missing Values', inplace=True)
    
    return summary_df

# Example usage
if __name__ == "__main__":
    filepath = "data/titanic.csv"  
    titanic_data = pd.read_csv(filepath)
    summary_table = create_summary_table(titanic_data)
