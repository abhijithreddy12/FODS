import pandas as pd
data = {
    'date': pd.date_range(start='2024-01-01', periods=365),
    'closing_price': np.random.uniform(100, 500, 365)
}
df = pd.DataFrame(data)
mean_price = df['closing_price'].mean()
std_dev = df['closing_price'].std()
max_price = df['closing_price'].max()
min_price = df['closing_price'].min()
price_range = max_price - min_price
print(f"Mean Closing Price: {mean_price:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Price Range: {price_range:.2f}")

df.set_index('date')['closing_price'].plot(title='Stock Price Variability Over Time', figsize=(10, 6))
plt.ylabel('Closing Price')
plt.show()
