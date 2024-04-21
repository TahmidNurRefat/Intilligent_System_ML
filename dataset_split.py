import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset from the file path
dataset = pd.read_csv("preprocessed_data.csv")  

# Extracting labels and features
labels = dataset['type']
features = dataset.drop(columns=['Unnamed: 0', 'type'])  # Dropping unnecessary columns and the label column to get features

# Splitting the dataset into training, validation, and test sets
X_train_val, X_test, y_train_val, y_test = train_test_split(features, labels, test_size=0.1, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.1111, random_state=42)

# Save the datasets to separate files
train_data = pd.concat([X_train, y_train], axis=1)
val_data = pd.concat([X_val, y_val], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

train_data.to_csv("train_data.csv", index=False)
val_data.to_csv("val_data.csv", index=False)
test_data.to_csv("test_data.csv", index=False)
