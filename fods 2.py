import numpy as np

sales_data = np.array([
    [10, 50, 500],  
    [15, 40, 600],  
    [20, 30, 600]  
])
price_per_unit = sales_data[:, 1]
average_price = np.mean(price_per_unit)
print(f"The average price of all the products sold is: ${average_price:.2f}")
