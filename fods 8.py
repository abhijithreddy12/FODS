import pandas as pd
data = {
    'product_name': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product C', 'Product A'],
    'order_quantity': [3, 5, 2, 4, 1, 7, 6],
    'order_date': ['2023-08-01', '2023-08-05', '2023-08-10', '2023-08-15', '2023-08-20', '2023-08-25', '2023-08-30']
}
sales_data = pd.DataFrame(data)
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])
start_date = '2023-08-01'
end_date = '2023-08-31'
monthly_sales = sales_data[(sales_data['order_date'] >= start_date) & (sales_data['order_date'] <= end_date)]

product_sales = monthly_sales.groupby('product_name')['order_quantity'].sum()

top_5_products = product_sales.sort_values(ascending=False).head(5)

print("Top 5 products sold in the past month:")
print(top_5_products)
