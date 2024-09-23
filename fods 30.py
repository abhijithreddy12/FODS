# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
data = {
    'mileage': np.random.uniform(5000, 150000, 500),
    'age': np.random.uniform(1, 20, 500),
    'brand': np.random.choice(['Toyota', 'Honda', 'Ford', 'BMW'], 500),
    'engine_type': np.random.choice(['Diesel', 'Petrol', 'Electric'], 500),
    'price': np.random.uniform(3000, 40000, 500)
}
df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df, columns=['brand', 'engine_type'], drop_first=True)
X = df_encoded.drop('price', axis=1)  # Features (mileage, age, brand, engine type)
y = df_encoded['price'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)
def display_decision_path(model, feature_names, X_new):
    decision_path = model.decision_path([X_new])
    tree_structure = model.tree_
    
    print("\nDecision Path:")
    node_indicator = decision_path.toarray().flatten()
    for node_id in range(tree_structure.node_count):
        if node_indicator[node_id]:
            threshold = tree_structure.threshold[node_id]
            if threshold != -2:  
                feature = feature_names[tree_structure.feature[node_id]]
                print(f"Node {node_id}: {feature} <= {threshold:.2f}")
            else:
                print(f"Node {node_id}: Leaf node with prediction {tree_structure.value[node_id][0][0]:.2ftry:
    mileage = float(input("Enter mileage: "))
    age = float(input("Enter age of the car (in years): "))
    brand = input("Enter car brand (Toyota, Honda, Ford, BMW): ")
    engine_type = input("Enter engine type (Diesel, Petrol, Electric): ")
    new_car = {
        'mileage': mileage,
        'age': age,
        'brand_' + brand: 1 if 'brand_' + brand in X.columns else 0,
        'engine_type_' + engine_type: 1 if 'engine_type_' + engine_type in X.columns else 0
    }
    for col in X.columns:
        if col not in new_car:
            new_car[col] = 0
    new_car_array = np.array([list(new_car.values())])
    predicted_price = model.predict(new_car_array)[0]

    print(f"\nPredicted price for the car: ${predicted_price:.2f}")
    display_decision_path(model, X.columns, new_car_array[0])

except ValueError:
    print("Invalid input! Please enter valid numeric values for mileage and age, and valid choices for brand and engine type.")
plt.figure(figsize=(15, 10))
plot_tree(model, feature_names=X.columns, filled=True, rounded=True)
plt.show()
