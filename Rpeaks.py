import pandas as pd
import matplotlib.pyplot as plt
import biosppy.signals.ecg as ecg

# Load ECG data
df = pd.read_csv("E:/WFDBRecords/WFDBRecords/01/010/JS00001.csv")

# Plot ECG signal
plt.figure(figsize=(10, 6))
plt.plot(df['time'], df['I'], label='ECG Signal (Lead I)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('ECG Signal with R Peak Detection')
plt.legend()
plt.grid(True)

# Perform R peak detection
sampling_rate = 1 / (df['time'].diff().mean())
ecg_signal = df['I'].values
rpeaks = ecg.hamilton_segmenter(ecg_signal, sampling_rate=sampling_rate)['rpeaks']

# Plot R peaks
rpeaks_time = df['time'].iloc[rpeaks]
rpeaks_amplitude = df['I'].iloc[rpeaks]
plt.scatter(rpeaks_time, rpeaks_amplitude, color='r', label='R Peaks')
plt.legend()

plt.show()
