import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv("C:/Users/shakt/OneDrive/Desktop/Infosys/Stress_prediction_data.csv")

# Define features (X) and target (y)
X = data.drop(columns=["Stress Level"])  # All columns except the target
y = data["Stress Level"]  # The target column (binary: 0 or 1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
