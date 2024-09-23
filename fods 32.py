import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = {
    'house_size': np.random.uniform(500, 5000, 100),
    'house_price': np.random.uniform(50000, 500000, 100)
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
sns.scatterplot(x='house_size', y='house_price', data=df)
plt.title('House Size vs Price')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price ($)')
plt.show()

X = df[['house_size']]  # Feature
y = df['house_price']   # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")
plt.figure(figsize=(8, 5))
sns.scatterplot(x=X_test['house_size'], y=y_test, label='Actual')
sns.lineplot(x=X_test['house_size'], y=y_pred, color='red', label='Predicted')
plt.title('Linear Regression: House Size vs Price')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price ($)')
plt.legend()
plt.show()
