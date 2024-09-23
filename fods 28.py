from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
np.random.seed(42)
n_customers = 500
annual_spending = np.random.uniform(1000, 10000, n_customers)  # Annual spending in dollars
frequency_of_purchases = np.random.uniform(1, 50, n_customers)  # Number of purchases per year
average_cart_value = np.random.uniform(20, 500, n_customers)
X = np.column_stack((annual_spending, frequency_of_purchases, average_cart_value))
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
n_clusters = 4
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X_scaled)
customer_segments = kmeans.predict(X_scaled)

try:
    annual_spending_input = float(input("Enter annual spending (in dollars): "))
    frequency_of_purchases_input = float(input("Enter frequency of purchases (per year): "))
    average_cart_value_input = float(input("Enter average cart value (in dollars): "))
    new_customer = np.array([[annual_spending_input, frequency_of_purchases_input, average_cart_value_input]])
    new_customer_scaled = scaler.transform(new_customer)
    new_customer_segment = kmeans.predict(new_customer_scaled)[0]
    
    print(f"The new customer belongs to segment: {new_customer_segment}")
    
except ValueError:
    print("Invalid input! Please enter valid numeric values.")
