import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'customer_id': range(1, 101),
    'total_spent': np.random.uniform(100, 10000, 100),
    'items_purchased': np.random.randint(1, 50, 100)
}
df = pd.DataFrame(data)
X = df[['total_spent', 'items_purchased']]
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(range(1, 11), sse, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('SSE')
plt.show()
kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(X)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_spent', y='items_purchased', hue='cluster', data=df, palette='tab10')
plt.title('E-Commerce Customer Segmentation')
plt.xlabel('Total Spent ($)')
plt.ylabel('Items Purchased')
plt.legend(title='Cluster')
plt.show()
