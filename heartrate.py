import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("E:/WFDBRecords/WFDBRecords/01/010/JS00001.csv")

# Calculate heart rate from RR intervals
rr_intervals = df['time'].diff().fillna(0)
heart_rate = 60 / rr_intervals

import seaborn as sns

# Plot kernel density estimate of heart rate distribution
plt.figure(figsize=(8, 6))
sns.kdeplot(heart_rate, shade=True, color='skyblue')
plt.xlabel('Heart Rate (bpm)')
plt.ylabel('Density')
plt.title('Distribution of Heart Rate (Kernel Density Plot)')
plt.grid(True)
plt.show()