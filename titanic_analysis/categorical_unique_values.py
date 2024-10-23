import pandas as pd

def display_unique_values(filepath, categorical_features):
    # Load the DataFrame from the CSV file
    df = pd.read_csv(filepath)
    unique_values = {}
    
    for feature in categorical_features:
        # If the feature exists in the DataFrame columns
        if feature in df.columns:
            # Get unique values list
            unique_values[feature] = df[feature].unique().tolist()
        else:
            # Print a warning if the feature is not found
            print(f"Warning: {feature} is not in the DataFrame columns.")
    
    return unique_values

# Test function execution and output
if __name__ == "__main__":
    filepath = "data/titanic.csv"  # Adjust the path as needed
    categorical_features = ['Sex', 'Embarked']  # Example features
    unique_values = display_unique_values(filepath, categorical_features)
    print(unique_values)