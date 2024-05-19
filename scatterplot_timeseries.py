import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Load ECG data
df = pd.read_csv("E:/WFDBRecords/WFDBRecords/01/010/JS00005.csv")

# Extract relevant features for PCA (exclude 'time' column)
features = df[['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']]

# Perform PCA with 4 components
pca = PCA(n_components=4)  # Example: 4 components for visualization
pca_result = pca.fit_transform(features)

# Convert PCA result to DataFrame
pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2', 'PC3', 'PC4'])

# Concatenate PCA DataFrame with time column from original data
pca_df['time'] = df['time']

# Data Distribution using PCA components
plt.figure(figsize=(10, 8))
sns.scatterplot(x='PC1', y='PC2', hue='time', data=pca_df)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Scatter Plot of PCA Components (PC1 vs. PC2)')
plt.legend(title='Time')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 8))
sns.scatterplot(x='PC3', y='PC4', hue='time', data=pca_df)
plt.xlabel('Principal Component 3')
plt.ylabel('Principal Component 4')
plt.title('Scatter Plot of PCA Components (PC3 vs. PC4)')
plt.legend(title='Time')
plt.grid(True)
plt.show()

# Time Series Analysis using PCA components
plt.figure(figsize=(10, 6))
plt.plot(pca_df['time'], pca_df['PC1'], label='PC1')
plt.plot(pca_df['time'], pca_df['PC2'], label='PC2')
plt.plot(pca_df['time'], pca_df['PC3'], label='PC3')
plt.plot(pca_df['time'], pca_df['PC4'], label='PC4')
plt.xlabel('Time')
plt.ylabel('Principal Component Value')
plt.title('Time Series Analysis of PCA Components')
plt.legend()
plt.grid(True)
plt.show()
