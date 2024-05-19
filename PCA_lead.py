import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
df = pd.read_csv('E:/WFDBRecords/WFDBRecords/01/010/JS00001.csv')
# Extract features (e.g., leads I, II, III, aVR, aVL, aVF, V1-V6)
features = df[['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']]

# Initialize PCA with desired number of components (e.g., 2 for visualization)
pca = PCA(n_components=12)

# Fit and transform the data
pca_result = pca.fit_transform(features)
selected_components = pca.components_

# Create a DataFrame for the loadings
loadings_df = pd.DataFrame(selected_components, columns=features.columns)

# Get the feature names with highest absolute loadings for each principal component
feature_names = {}
for component in loadings_df.index:
    highest_loading_idx = loadings_df.loc[component].abs().idxmax()
    highest_loading_value = loadings_df.loc[component, highest_loading_idx]
    feature_names[f'Principal Component {component + 1}'] = (highest_loading_idx, highest_loading_value)

# Print the feature names with highest loadings for each principal component
for component, (feature_name, loading_value) in feature_names.items():
    print(f'Principal Component {component}: {feature_name} (Loading: {loading_value:.2f})')


