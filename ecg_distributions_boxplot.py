import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load ECG data
df = pd.read_csv("E:/WFDBRecords/WFDBRecords/01/010/JS00001.csv")

# Create boxplot of ECG leads
plt.figure(figsize=(12, 8))
sns.boxplot(data=df[['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']], orient='h')
plt.xlabel('Amplitude')
plt.ylabel('ECG Leads')
plt.title('Distribution of ECG Leads')
plt.grid(True)
plt.show()
