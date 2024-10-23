import pandas as pd

def display_unique_values(filepath, categorical_features):
    df = pd.read_csv(filepath)
    unique_values = {}
    
    for feature in categorical_features:
        if feature in df.columns:
            unique_values[feature] = df[feature].unique().tolist()
    
    return unique_values

if __name__ == "__main__":
    filepath = "data/titanic.csv"  
    categorical_features = ['Sex', 'Embarked']  
    unique_values = display_unique_values(filepath, categorical_features)
    print(unique_values)