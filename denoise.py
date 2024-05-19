import csv
from biosppy.signals import ecg
import matplotlib.pyplot as plt

# Data points
signal = []

# Read ECG signal from the CSV file (assuming the signal is in the second column)
with open('E:/WFDBRecords/WFDBRecords/01/010/JS00002.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the first row
    for row in reader:
        signal.append(float(row[8])) #Lead V1 (heartbeat)

# Process the ECG signal and plot
out = ecg.ecg(signal=signal, sampling_rate=1000., show=True)

# Plot the ECG signal with R-peaks
plt.figure(figsize=(12, 6))
# Plot the filtered ECG signal with R-peaks
plt.subplot(1, 2, 1)
plt.plot(out['ts'], out['filtered'], label='Filtered ECG')
plt.plot(out['ts'][out['rpeaks']], out['filtered'][out['rpeaks']], 'ro', label='R-peaks')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Filtered ECG Signal with R-peaks')
plt.legend()

# Plot the templates on the right side
plt.subplot(1, 2, 2)
for i, template in enumerate(out['templates']):
    plt.plot(out['templates_ts'], template, label=f'Template {i+1}')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Templates')
plt.legend()

plt.tight_layout()
plt.show()