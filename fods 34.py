import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
data = {
    'age': np.random.randint(18, 90, 200),
    'blood_pressure': np.random.uniform(80, 180, 200),
    'cholesterol': np.random.uniform(150, 300, 200),
    'outcome': np.random.choice(['Good', 'Bad'], 200)
}

df = pd.DataFrame(data)
df['outcome'] = df['outcome'].map({'Good': 1, 'Bad': 0})
X = df[['age', 'blood_pressure', 'cholesterol']]
y = df['outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
