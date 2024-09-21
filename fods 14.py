import pandas as pd


data = {'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'age': [25, 30, 22, 40, 25, 30, 35, 40, 25, 22],
        'purchase_amount': [100, 150, 120, 200, 80, 160, 130, 140, 90, 110]}

sales_data = pd.DataFrame(data)

age_frequency_distribution = sales_data['age'].value_counts()

print("Frequency Distribution of Customer Ages:")
print(age_frequency_distribution)

