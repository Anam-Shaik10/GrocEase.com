import pandas as pd

# Load and standardize all datasets
blinkit_df = pd.read_json("Blinkit.json")
dmart_df = pd.read_json("Dmart.json")
bigbasket_df = pd.read_json("BigBasket.json")
country_delight_df = pd.read_json("country delight.json")


# Add platform column
blinkit_df['platform'] = 'Blinkit'
dmart_df['platform'] = 'Dmart'
bigbasket_df['platform'] = 'BigBasket'
country_delight_df['platform'] = 'country delight'

# Keep only necessary columns
blinkit_df = blinkit_df[['Name', 'Price(INR)', 'platform']]
dmart_df = dmart_df[['Name', 'Price(INR)', 'platform']]
bigbasket_df = bigbasket_df[['Name', 'price(INR)', 'platform']]
#country_delight_df = bigbasket_df[['Name', 'Price(INR)', 'platform']]

# Combine all into one DataFrame
combined_df = pd.concat([blinkit_df, dmart_df, bigbasket_df, country_delight_df], ignore_index=True)

# Clean names
combined_df['Name'] = combined_df['Name'].astype(str).str.lower().str.strip()

print("Combined Dataset Preview:")
display(combined_df)

print("\nShape of Combined Dataset:", combined_df.shape)

# Save the combined dataset as a .csv file
combined_df.to_csv("combined_dataset.csv", index=False)

# Save the combined dataset as a .json file
combined_df.to_json("combined_dataset.json", orient="records", lines=True)