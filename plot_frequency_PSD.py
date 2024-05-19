import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import welch

# Load ECG data
df = pd.read_csv("E:/WFDBRecords/WFDBRecords/01/010/JS00002.csv")

# Perform Fourier transform for frequency analysis
fs = 1 / (df['time'].diff().mean())  # Sampling frequency
frequencies, power_spectrum = welch(df['I'], fs=fs)

# Plot power spectral density
plt.figure(figsize=(10, 6))
plt.semilogy(frequencies, power_spectrum)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density')
plt.title('Power Spectral Density of ECG Signal (Lead I)')
plt.grid(True)
plt.show()