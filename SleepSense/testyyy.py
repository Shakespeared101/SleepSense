import pandas as pd

# Load the data
file_path = "SaYoPillow.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows to understand the structure
print(df.head())
print(df.info())
