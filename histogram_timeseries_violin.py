import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load ECG data
df = pd.read_csv("E:/WFDBRecords/WFDBRecords/01/010/JS00001.csv")

# Data Distribution
plt.figure(figsize=(12, 8))
for col in df.columns[1:]:  # Exclude 'time'
    plt.hist(df[col], bins=30, alpha=0.5, label=col)
plt.xlabel('Attribute Value')
plt.ylabel('Frequency')
plt.title('Histograms of ECG Data Attributes')
plt.legend()
plt.grid(True)
plt.show()


# Time Series Analysis
plt.figure(figsize=(10, 6))
for col in df.columns[1:]:  # Exclude 'time'
    plt.plot(df['time'], df[col], label=col)
plt.xlabel('Time')
plt.ylabel('Attribute Value')
plt.title('Time Series Analysis of ECG Data')
plt.legend()
plt.grid(True)
plt.show()



plt.figure(figsize=(10, 6))
sns.violinplot(data=df.iloc[:, 1:])
plt.xlabel('Attribute')
plt.ylabel('Attribute Value')
plt.title('Violin Plot of ECG Data Attributes')
plt.grid(True)
plt.show()

# Statistical Analysis
df_stats = df.describe()
print(df_stats)
