import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import welch

# Load ECG data
df = pd.read_csv("E:/WFDBRecords/WFDBRecords/01/010/JS00002.csv")

# Example: Create dynamic visualization using interactive plots or animations
# (Code for interactive plots or animations will depend on the chosen library, e.g., Plotly, Bokeh)
# Here's a simple example using Plotly:
import plotly.graph_objects as go

fig = go.Figure()
for lead in ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']:
    fig.add_trace(go.Scatter(x=df['time'], y=df[lead], mode='lines', name=lead))

fig.update_layout(
    title='Dynamic Visualization of ECG Waveforms',
    xaxis_title='Time',
    yaxis_title='Amplitude',
    legend_title='ECG Leads',
    hovermode='closest',
)

fig.show()



