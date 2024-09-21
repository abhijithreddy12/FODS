import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Downtown', 'Suburb', 'Downtown', 'Suburb', 'Downtown'],
    'number_of_bedrooms': [3, 5, 4, 6, 2],
    'area_in_sqft': [1500, 2500, 1800, 3500, 1200],
    'listing_price': [300000, 450000, 400000, 600000, 250000]
}
property_data = pd.DataFrame(data)

average_price_per_location = property_data.groupby('location')['listing_price'].mean()
print("Average listing price of properties in each location:")
print(average_price_per_location)

properties_with_more_than_4_bedrooms = property_data[property_data['number_of_bedrooms'] > 4]
number_of_properties = properties_with_more_than_4_bedrooms.shape[0]
print(f"\nNumber of properties with more than four bedrooms: {number_of_properties}")

largest_property = property_data.loc[property_data['area_in_sqft'].idxmax()]
print("\nProperty with the largest area:")
print(largest_property)
