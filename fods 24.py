import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Simulate medical data for patients (you can load real data from a CSV file)
def generate_medical_data(num_samples=100):
    np.random.seed(42)
    # Generate random data with 3 features (symptoms)
    features = np.random.rand(num_samples, 3) * 10  # Simulating 3 symptom features
    # Generate binary labels (0 = no condition, 1 = has condition)
    labels = np.random.randint(0, 2, num_samples)
    return pd.DataFrame(features, columns=['Symptom1', 'Symptom2', 'Symptom3']), labels

def main():
    # Generate or load medical data
    X, y = generate_medical_data(num_samples=100)  # 100 patients, 3 symptoms
    
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Normalize the data (important for KNN)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Get input from the user for a new patient's features
    print("Enter the patient's symptom features:")
    new_patient = []
    for i in range(X.shape[1]):
        feature = float(input(f"Enter value for Symptom {i+1}: "))
        new_patient.append(feature)
    new_patient = np.array(new_patient).reshape(1, -1)
    
    # Normalize the new patient's features
    new_patient = scaler.transform(new_patient)
    
    # Get the value of k from the user
    k = int(input("Enter the value of k (number of neighbors): "))
    
    # Train the KNN classifier
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    
    # Make a prediction for the new patient
    prediction = knn.predict(new_patient)
    
    # Display the result
    if prediction[0] == 1:
        print("The patient is predicted to have the medical condition.")
    else:
        print("The patient is predicted not to have the medical condition.")

if __name__ == "__main__":
    main()
