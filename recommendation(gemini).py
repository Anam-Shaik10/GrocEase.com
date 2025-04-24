import google.generativeai as genai
import pandas as pd

# Configure the Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Load your product data from all platforms into a single dataframe
# Ensure all product names are normalized to lowercase
def load_data():
    # Example - Load your cleaned and matched datasets
    blinkit = pd.read_csv("blinkit.csv")
    dmart = pd.read_csv("dmart.csv")
    bigbasket = pd.read_csv("bigbasket.csv")
    country_delight = pd.read_csv("country delight.csv")

    # Add source column to identify platforms
    blinkit['Source'] = 'Blinkit'
    dmart['Source'] = 'DMart'
    bigbasket['Source'] = 'BigBasket'
    country_delight['Source'] = 'Country Delight'

    # Combine all datasets
    all_products = pd.concat([blinkit, dmart, bigbasket, country_delight], ignore_index=True)
    all_products['Name'] = all_products['Name'].str.lower()

    return all_products

# Function to query Gemini for alternative platform recommendation
def recommend_alternative(product_name, dataset):
    product_name = product_name.lower()
    
    # Check if product exists
    matches = dataset[dataset['Name'].fillna("").str.contains(product_name, case=False, na=False)]
    if not matches.empty:
        available_sources = matches['Source'].unique()
        return f"✅ '{product_name}' is available on: {', '.join(available_sources)}"
    
    # If product not found, ask Gemini to recommend a platform
    prompt = f"""
    A customer is searching for the product '{product_name}', but it is not found in our current dataset.
    The available platforms are: Blinkit, DMart, BigBasket, Zepto, and Country Delight.
    Based on common availability patterns in Indian grocery platforms, suggest which of these platforms are most likely to have this product.
    Respond only with platform names.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    suggestion = response.text.strip()

    return f"❌ '{product_name}' not found in current datasets.\n💡 Try checking on: {suggestion}"

# Example Usage
if __name__ == "__main__":
    data = load_data()
    
    user_input = input("Enter product name: ")
    suggestion = recommend_alternative(user_input, data)
    print(suggestion)

