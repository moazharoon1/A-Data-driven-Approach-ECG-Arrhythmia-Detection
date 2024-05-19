import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Load ECG data
df = pd.read_csv("E:/WFDBRecords/WFDBRecords/01/010/JS00005.csv")

# Extract relevant features for PCA (exclude 'time' column)
features = df[['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']]

# Perform PCA with 4 components (for example)
pca = PCA(n_components=4)
pca_result = pca.fit_transform(features)

# Convert PCA result to DataFrame
pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2', 'PC3', 'PC4'])

# Compute correlation matrix for PCA components
corr_matrix_pca = pca_df.corr()

# Plot correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix_pca, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of PCA Components')
plt.show()
