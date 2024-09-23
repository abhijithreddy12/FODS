import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data = np.array([
    [1500, 3, 300000],
    [1600, 3, 320000],
    [1700, 4, 350000],
    [1800, 4, 360000],
    [1900, 5, 400000],
    [2000, 5, 450000],
])
X = data[:, :-1]  # Features (area, bedrooms)
y = data[:, -1]  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
def predict_house_price():
    area = float(input("Enter the area of the house in square feet: "))
    bedrooms = int(input("Enter the number of bedrooms: "))
    new_house = np.array([[area, bedrooms]])
    predicted_price = model.predict(new_house)
    print(f"The predicted price for the house is: ${predicted_price[0]:,.2f}")
predict_house_price()
