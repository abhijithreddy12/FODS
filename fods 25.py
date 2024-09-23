from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
iris = load_iris()
X = iris.data 
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
def predict_iris_species():
    sepal_length = float(input("Enter sepal length (cm): "))
    sepal_width = float(input("Enter sepal width (cm): "))
    petal_length = float(input("Enter petal length (cm): "))
    petal_width = float(input("Enter petal width (cm): "))
    new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
     prediction = clf.predict(new_flower)
    species = iris.target_names[prediction][0]
     print(f"The predicted species is: {species}")
predict_iris_species()
