import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
data = {
    'age': np.random.randint(18, 65, 500),
    'annual_income': np.random.randint(30000, 150000, 500),
    'spending_score': np.random.randint(1, 100, 500),  # Score from 1 to 100 (higher score indicates higher spending)
    'purchase_frequency': np.random.randint(1, 50, 500),
    'average_cart_value': np.random.uniform(50, 1000, 500)
}
df = pd.DataFrame(data)
print("Customer Data:\n", df.head())
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
sse = []  # Sum of squared distances
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    sse.append(kmeans.inertia_)
plt.figure(figsize=(8, 5))
plt.plot(k_range, sse, marker='o')
plt.title('Elbow Method to Determine Optimal Clusters')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Sum of Squared Distances (SSE)')
plt.grid(True)
plt.show()
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_scaled)
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=df.columns[:-1])
print("\nCluster Centers:\n", cluster_centers_df)
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)
df['PCA1'] = df_pca[:, 0]
df['PCA2'] = df_pca[:, 1]

plt.figure(figsize=(10, 7))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=df, palette='Set1', s=100, alpha=0.8)
plt.title('Customer Segments Visualized in 2D PCA Space')
plt.show()
cluster_summary = df.groupby('Cluster').mean()
print("\nCluster Summary:\n", cluster_summary)
