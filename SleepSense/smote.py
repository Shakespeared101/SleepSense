import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE

# Load the data
file_path = "SaYoPillow.csv"
df = pd.read_csv(file_path)

# Function to add random noise for extrapolation
def add_noise(data, noise_level=0.05):
    """Add random noise to the data to generate new samples."""
    noise = np.random.normal(loc=0.0, scale=noise_level, size=data.shape)
    return data + noise

# Extract features and target
X = df.drop('sl', axis=1)  # Continuous features
y = df['sl']  # Categorical target

# Step 1: Apply SMOTE to oversample minority class
smote = SMOTE(sampling_strategy='auto', random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Step 2: Extrapolate data by adding random noise
X_extrapolated = add_noise(X_resampled, noise_level=0.02)

# Combine the extrapolated features with the target labels
df_new = pd.DataFrame(X_extrapolated, columns=X.columns)
df_new['sl'] = y_resampled

# Save the new dataset to a CSV file
output_path = "SaYoPillow_extrapolated.csv"
df_new.to_csv(output_path, index=False)

print(f"New dataset saved to {output_path}")
