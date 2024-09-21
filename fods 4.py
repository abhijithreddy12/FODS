import numpy as np

sales_data = np.array([50000, 60000, 70000, 100000])  
total_sales = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print(f"Total sales for the year: ${total_sales:.2f}")
print(f"Percentage increase from Q1 to Q4: {percentage_increase:.2f}%")
