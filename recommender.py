from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

# Assuming your combined DataFrame is named combined_df and has columns:
# 'Name', 'Price(INR)', and 'platform'

# Step 1: Normalize product names (lowercase + strip whitespace)
combined_df['Name'] = combined_df['Name'].astype(str).str.lower().str.strip()

# Step 2: TF-IDF vectorization on product names
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(combined_df['Name'])

# Step 3: Product recommender function using cosine similarity
def recommend_products(product_name, df=combined_df, tfidf_matrix=tfidf_matrix, top_n=5):
    product_name = product_name.lower().strip()
    
    # Find the index of the product
    idx = df[df['Name'] == product_name].index

    if len(idx) == 0:
        print(f"❌ Product '{product_name}' not found in the dataset.")
        return pd.DataFrame()
    
    idx = idx[0]

    # Compute similarity scores
    sim_scores = list(enumerate(linear_kernel(tfidf_matrix[idx], tfidf_matrix)[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Skip the first match (it’s the same product)
    sim_scores = sim_scores[1:top_n + 1]
    product_indices = [i[0] for i in sim_scores]

    return df.iloc[product_indices][['Name', 'Price(INR)', 'platform']]


print(f"\n🔍 Recommended Products Similar to: '{product_to_search}'\n")
print(recommendations)
