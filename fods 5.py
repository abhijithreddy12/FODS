import numpy as np
fuel_efficiency = np.array([20, 25, 30, 22, 35, 40, 18, 24])
average_efficiency = np.mean(fuel_efficiency)
model_1_efficiency = fuel_efficiency[1] 
model_2_efficiency = fuel_efficiency[5]
percentage_improvement = ((model_2_efficiency - model_1_efficiency) / model_1_efficiency) * 100

# Print the results
print(f"Average fuel efficiency: {average_efficiency:.2f} mpg")
print(f"Percentage improvement from model 2 to model 6: {percentage_improvement:.2f}%")
