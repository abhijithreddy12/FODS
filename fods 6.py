item_prices = [10, 20, 15] 
quantities = [2, 1, 3] 
discount_rate = 10 
tax_rate = 5 

item_totals = [price * quantity for price, quantity in zip(item_prices, quantities)]

subtotal = sum(item_totals)

discount_amount = (discount_rate / 100) * subtotal
total_after_discount = subtotal - discount_amount

tax_amount = (tax_rate / 100) * total_after_discount
total_cost = total_after_discount + tax_amount

print(f"Total cost after discount and tax: ${total_cost:.2f}")

