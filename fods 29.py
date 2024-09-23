from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np
data = load_iris()
X = data.data  # Features
y = data.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
feature_names = list(data.feature_names)
target_variable = 'species'
print("Feature Names: ", feature_names)
print("Target Variable: ", target_variable)
chosen_features = input("Enter the names of the features you want to use (comma-separated): ").split(',')
chosen_features = [feature.strip() for feature in chosen_features]

if not set(chosen_features).issubset(set(feature_names)):
    print("Invalid feature names! Please check the names and try again.")
else:
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')
    print(f"\nEvaluation Metrics for {target_variable}:")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"Precision: {precision * 100:.2f}%")
    print(f"Recall: {recall * 100:.2f}%")
    print(f"F1-score: {f1 * 100:.2f}%")
