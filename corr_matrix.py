import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load ECG data
df = pd.read_csv("E:/WFDBRecords/WFDBRecords/01/010/JS00001.csv")

# Compute correlation matrix
corr_matrix = df[['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']].corr()

# Plot correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of ECG Leads')
plt.show()
