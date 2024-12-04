import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the extrapolated dataset
file_path = "Stress_Dataset.csv"
df = pd.read_csv(file_path)

# Convert 'sl' into binary classification: 0 (low) vs. 1 (high)
df['sl_binary'] = df['sl'].apply(lambda x: 1 if x > 0 else 0)

# Ensure the save directory exists
save_path = "output_visuals/"
os.makedirs(save_path, exist_ok=True)

# Set global Seaborn style
sns.set(style="whitegrid")

# 1. Scatter Plot: Snoring Rate vs. Binary Stress Level
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sr', y='sl_binary', data=df, hue='sl_binary', palette='cool', s=50)
plt.title('Scatter Plot of Snoring Rate vs. Binary Stress Level')
plt.xlabel('Snoring Rate (sr)')
plt.ylabel('Binary Stress Level (sl_binary)')
plt.legend(title='Stress Level', loc='upper right')
plt.savefig(save_path + 'scatter_sr_vs_sl_binary.png')
plt.close()

# 2. Bar Chart: Mean Respiratory Rate for each Binary Stress Level
plt.figure(figsize=(8, 6))
df.groupby('sl_binary')['rr'].mean().plot(kind='bar', color='skyblue')
plt.title('Mean Respiratory Rate by Binary Stress Level')
plt.xlabel('Binary Stress Level (sl_binary)')
plt.ylabel('Mean Respiratory Rate (rr)')
plt.savefig(save_path + 'bar_rr_vs_sl_binary.png')
plt.close()

# 3. Heatmap: Correlation between Features (Binary Stress Level)
plt.figure(figsize=(10, 8))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Features (Binary Stress Level)')
plt.savefig(save_path + 'heatmap_correlation_binary.png')
plt.close()

# 4. Box Plot: Limb Movements across Binary Stress Levels
plt.figure(figsize=(8, 6))
sns.boxplot(x='sl_binary', y='lm', data=df, palette='pastel')
plt.title('Box Plot of Limb Movements by Binary Stress Level')
plt.xlabel('Binary Stress Level (sl_binary)')
plt.ylabel('Limb Movements (lm)')
plt.savefig(save_path + 'boxplot_lm_vs_sl_binary.png')
plt.close()

# 5. Scatter Plot: Heart Rate vs. Blood Oxygen Level colored by Binary Stress Level
plt.figure(figsize=(8, 6))
sns.scatterplot(x='bo', y='hr', hue='sl_binary', data=df, palette='viridis', s=50)
plt.title('Scatter Plot of Heart Rate vs. Blood Oxygen Level (Binary Stress Level)')
plt.xlabel('Blood Oxygen Level (bo)')
plt.ylabel('Heart Rate (hr)')
plt.legend(title='Stress Level', loc='upper right')
plt.savefig(save_path + 'scatter_hr_vs_bo_binary.png')
plt.close()

print(f"Visualizations saved in {save_path}")
