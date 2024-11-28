# Step 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Step 2: Load and Inspect the Dataset
# Replace "path/to/your/dataset.csv" with the path to your dataset file
data = pd.read_csv("C:/Users/shakt/OneDrive/Desktop/Infosys/Stress_prediction_data.csv")

# Print dataset information
print(data.head())
print(data.info())

# Step 3: Prepare the Data
# Define features (X) and target (y)
X = data.drop(columns=["Stress Level"])  # Exclude the target column
y = data["Stress Level"]  # Target column

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Standardize the Data
# Initialize the scaler
scaler = StandardScaler()

# Fit the scaler on the training set and transform both training and test sets
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 5: Define the ANN Model Architecture
model = Sequential()

# Input layer and first hidden layer
model.add(Dense(units=64, activation='relu', input_shape=(X_train.shape[1],)))

# Second hidden layer
model.add(Dense(units=32, activation='relu'))

# Output layer (binary classification, so use sigmoid activation)
model.add(Dense(units=1, activation='sigmoid'))

# Step 6: Compile the Model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 7: Train the Model
# Train the model on the training data
model.fit(X_train, y_train, epochs=500, batch_size=16, validation_split=0.2)

# Step 8: Evaluate the Model
# Evaluate the model's accuracy on the test data
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy}")

# Step 9: Save the Model
# Save the trained model to a .h5 file for use in Django
model.save("stress_detection_model.h5")
print("Model saved as stress_detection_model.h5")
