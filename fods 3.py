import numpy as np


house_data = np.array([
    [3, 2000, 250000],
    [5, 3000, 450000],
    [4, 2200, 300000],
    [6, 3500, 550000],
    [7, 4000, 700000]
])

houses_with_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]

sale_prices = houses_with_more_than_4_bedrooms[:, 2]
average_sale_price = np.mean(sale_prices)
print(f"The average sale price of houses with more than 4 bedrooms is: ${average_sale_price:.2f}")
