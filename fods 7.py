import pandas as pd
data = {
    'customer_id': [1, 2, 1, 3, 2, 3],
    'order_date': ['2023-01-10', '2023-02-15', '2023-03-01', '2023-01-20', '2023-04-18', '2023-05-10'],
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A'],
    'order_quantity': [2, 1, 3, 5, 2, 4]
}
order_data = pd.DataFrame(data)
order_data['order_date'] = pd.to_datetime(order_data['order_date'])
customer_order_counts = order_data.groupby('customer_id').size()
print("Total number of orders made by each customer:")
print(customer_order_counts)
average_order_quantity = order_data.groupby('product_name')['order_quantity'].mean()
print("\nAverage order quantity for each product:")
print(average_order_quantity)
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print(f"\nEarliest order date: {earliest_order_date}")
print(f"Latest order date: {latest_order_date}")
