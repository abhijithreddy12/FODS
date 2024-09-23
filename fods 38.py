import pandas as pd
import numpy as np
data = {
    'city': np.random.choice(['CityA', 'CityB', 'CityC', 'CityD'], 365),
    'temperature': np.random.uniform(0, 40, 365)
}
df = pd.DataFrame(data)
mean_temp = df.groupby('city')['temperature'].mean()
print("Mean Temperature for each city:")
print(mean_temp)
std_temp = df.groupby('city')['temperature'].std()
print("\nStandard Deviation of Temperature for each city:")
print(std_temp)
temp_range = df.groupby('city')['temperature'].apply(lambda x: x.max() - x.min())
print("\nTemperature Range for each city:")
print(temp_range)
highest_range_city = temp_range.idxmax()
consistent_city = std_temp.idxmin()

print(f"\nCity with highest temperature range: {highest_range_city}")
print(f"City with most consistent temperature: {consistent_city}")
