from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
np.random.seed(42)
n_samples = 1000
usage_minutes = np.random.uniform(200, 1500, n_samples)  # Random usage minutes
contract_duration = np.random.uniform(1, 36, n_samples)  # Contract duration in months
age = np.random.uniform(18, 80, n_samples)  # Age of the customer
churn_status = np.random.choice([0, 1], n_samples, p=[0.8, 0.2])
X = np.column_stack((usage_minutes, contract_duration, age))
y = churn_status 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"Accuracy on test set: {accuracy_score(y_test, y_pred) * 100:.2f}%")
try:
    usage_minutes_input = float(input("Enter usage minutes: "))
    contract_duration_input = float(input("Enter contract duration (months): "))
    age_input = float(input("Enter customer's age: "))
    new_customer = np.array([[usage_minutes_input, contract_duration_input, age_input]])
    churn_prediction = model.predict(new_customer)[0]
    
    if churn_prediction == 1:
        print("The customer is likely to churn.")
    else:
        print("The customer is not likely to churn.")
    
except ValueError:
    print("Invalid input! Please enter valid numeric values.")
