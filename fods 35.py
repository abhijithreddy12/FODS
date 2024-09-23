import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'customer_id': range(1, 101),
    'total_spent': np.random.uniform(100, 5000, 100),
    'visit_frequency': np.random.randint(1, 50, 100)
}
df = pd.DataFrame(data)
X = df[['total_spent', 'visit_frequency']]

sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(range(1, 11), sse, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('SSE (Sum of Squared Errors)')
plt.show()
kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(X)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_spent', y='visit_frequency', hue='cluster', data=df, palette='tab10')
plt.title('Customer Segmentation using K-Means')
plt.xlabel('Total Amount Spent')
plt.ylabel('Visit Frequency')
plt.legend(title='Cluster')
plt.show()
