import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    'engine_size': np.random.uniform(1.0, 6.0, 200),
    'horsepower': np.random.uniform(100, 500, 200),
    'fuel_efficiency': np.random.uniform(10, 50, 200),
    'car_price': np.random.uniform(15000, 80000, 200)
}

df = pd.DataFrame(data)
X = df[['engine_size', 'horsepower', 'fuel_efficiency']]
y = df['car_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print("\nInfluential factors:\n", coefficients)
plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_test, y=y_pred)
plt.title('Actual vs Predicted Car Prices')
plt.xlabel('Actual Car Prices')
plt.ylabel('Predicted Car Prices')
plt.show()
