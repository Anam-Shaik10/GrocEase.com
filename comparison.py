import pandas as pd

# Load the CSV files into dataframes
dmart_df = pd.read_csv('Dmart.csv')
blinkit_df = pd.read_csv('Blinkit.csv')
country_delight_df = pd.read_csv('country delight.csv')

# Prompt the user to input a product name
product_name = input("Enter the product name you want to search for: ")

# Check the product price, quantity, and other details in each shop
dmart_product = dmart_df[dmart_df['Name'].str.contains(product_name, case=False, na=False)][['Name', 'Price(INR)', 'DiscountedPrice', 'Quantity']]
blinkit_product = blinkit_df[blinkit_df['Name'].str.contains(product_name, case=False, na=False)][['Name', 'Price(INR)', 'market_price', 'type']]
country_delight_product = country_delight_df[country_delight_df['Name'].str.contains(product_name, case=False, na=False)][['Name', 'Price(INR)', 'Rating', 'Delivery Time']]

# Print the product details in each shop
print(product_name + " details in Dmart:")
print(dmart_product)

print("\n" + product_name + " details in Blinkit:")
print(blinkit_product)

print("\n" + product_name + " details in Country Delight:")
print(country_delight_product)

# Check if the product is available in all shops before proceeding
if dmart_product.empty and blinkit_product.empty and country_delight_product.empty:
    print("\nThe product '" + product_name + "' is not available in any shop.")
else:
    # Determine which shop has the lowest price for the product
    lowest_price_shop = None
    lowest_price = float('inf')

    if not dmart_product.empty:
        lowest_price = min(lowest_price, dmart_product['Price(INR)'].min())
        if lowest_price == dmart_product['Price(INR)'].min():
            lowest_price_shop = "Dmart"

    if not blinkit_product.empty:
        lowest_price = min(lowest_price, blinkit_product['Price(INR)'].min())
        if lowest_price == blinkit_product['Price(INR)'].min():
            lowest_price_shop = "Blinkit"

    if not country_delight_product.empty:
        lowest_price = min(lowest_price, country_delight_product['Price(INR)'].min())
        if lowest_price == country_delight_product['Price(INR)'].min():
            lowest_price_shop = "Country Delight"

    print("\n" + lowest_price_shop + " has the lowest price for " + product_name + " at INR " + str(lowest_price))