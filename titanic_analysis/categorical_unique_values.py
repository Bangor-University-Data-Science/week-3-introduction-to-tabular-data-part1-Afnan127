import pandas as pd

def display_unique_values(df, categorical_features):
    unique_values = {}
    
    for feature in categorical_features:
    
        unique_values[feature] = df[feature].unique().tolist()
    
    
    return unique_values

# function execution test
if __name__ == "__main__":
    # Load the Titanic dataset
    df = pd.read_csv('data/titanic.csv') 

    categorical_features = ['Sex', 'Embarked']  
    
    unique_values = display_unique_values(df, categorical_features)