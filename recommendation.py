import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Load dataset
df = pd.read_csv('D:/Python Project/ebay_womens_perfume.csv')

# Fill NaN values with empty strings in relevant columns
df['title'] = df['title'].fillna('')
df['type'] = df['type'].fillna('')
df['combined'] = df['title'] + ' ' + df['type']
df['availableText'] = df['availableText'].fillna('')
df['itemLocation'] = df['itemLocation'].fillna('')
df['brand'] = df['brand'].fillna('')
df['price'] = df['price'].fillna(0)

# TF-IDF Vectorizer to analyze 'combined' column
tfidf = TfidfVectorizer(stop_words='english')
df['combined'] = df['combined'].fillna('')
tfidf_matrix = tfidf.fit_transform(df['combined'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get perfume recommendations
def get_recommendations(title, df, cosine_sim=cosine_sim):
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    perfume_indices = [i[0] for i in sim_scores]
    return df.iloc[perfume_indices]

# Streamlit frontend
st.title('Perfume Recommendation System')

# Sidebar for filters
st.sidebar.header('Filter Options')

# Filter by Brand
selected_brand = st.sidebar.selectbox('Select a brand:', ['All'] + list(df['brand'].unique()))

# Filter by Price Range
min_price, max_price = st.sidebar.slider('Select price range:', int(df['price'].min()), int(df['price'].max()), (int(df['price'].min()), int(df['price'].max())))

# Filter by Item Location
selected_location = st.sidebar.selectbox('Select item location:', ['All'] + list(df['itemLocation'].unique()))

# Create a filtered dataframe based on the filter options
filtered_df = df.copy()

# Apply brand filter
if selected_brand != 'All':
    filtered_df = filtered_df[filtered_df['brand'] == selected_brand]

# Apply price range filter
filtered_df = filtered_df[(filtered_df['price'] >= min_price) & (filtered_df['price'] <= max_price)]

# Apply item location filter
if selected_location != 'All':
    filtered_df = filtered_df[filtered_df['itemLocation'] == selected_location]

# Ensure that there are perfumes in the filtered dataset
if not filtered_df.empty:
    # Dropdown to select a perfume title (use filtered dataframe)
    selected_perfume = st.selectbox('Select a perfume title:', filtered_df['title'])
    
    # Recommendation Button
    if st.button('Get Recommendations'):
        # Get recommendations from the full dataset (not the filtered one)
        recommendations = get_recommendations(selected_perfume, df=df)
        
        st.write('Top 5 similar perfumes:')
        for i in range(len(recommendations)):
            st.write(f"**Title**: {recommendations.iloc[i]['title']}")
            st.write(f"**Brand**: {recommendations.iloc[i]['brand']}")
            st.write(f"**Type**: {recommendations.iloc[i]['type']}")
            st.write(f"**Price**: {recommendations.iloc[i]['priceWithCurrency']}")
            st.write(f"**Availability**: {recommendations.iloc[i]['availableText']}")
            st.write(f"**Item Location**: {recommendations.iloc[i]['itemLocation']}")
            st.write('---')
else:
    st.write("No perfumes match your filters. Please adjust the filters and try again.")
