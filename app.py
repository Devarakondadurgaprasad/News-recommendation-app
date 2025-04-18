import streamlit as st
import pandas as pd
import random

# Expanded news dataset
news_df = pd.DataFrame({
    'headline': [
        # POLITICS
        "Election 2024 updates", "Senate debates bill", "New tax reforms announced",
        "Mayor's speech on education", "Government budget passed",
        "Opposition criticizes healthcare plan", "Policy reforms for rural development",
        "Defense budget increased", "President meets foreign delegates",
        "Campaign rallies across the nation",

        # ENTERTAINMENT
        "Hollywood awards night", "Celebrity wedding", "New Netflix series released",
        "Top 10 Bollywood blockbusters", "Music festival highlights",
        "Famous director announces new film", "Actor wins lifetime achievement",
        "Oscars 2025 predictions", "Box office hits of the year", "Upcoming K-drama trailers",

        # SPORTS
        "Champions League Final", "Olympics preview", "Cricket World Cup qualifiers",
        "NBA season kickoff", "Tennis Grand Slam upsets",
        "Formula 1 race results", "FIFA rankings updated", "Young stars in football",
        "Athlete sets new world record", "India wins hockey series",

        # WORLD NEWS
        "UN summit coverage", "Global economy crisis", "Peace talks in the Middle East",
        "Climate change agreements", "Elections in Europe",
        "Wildfire disaster in Australia", "Border tensions ease", "New trade agreement signed",
        "Refugee crisis in Africa", "COVID-19 updates worldwide",

        # TECH
        "AI chip launches", "New iPhone reveal", "SpaceX Mars mission updates",
        "Quantum computing breakthrough", "Meta unveils VR headset",
        "OpenAI releases new model", "Google announces Pixel 9", "Cybersecurity threats rise",
        "Apple Vision Pro reviews", "Robots entering the workforce"
    ],
    'category': (
        ["POLITICS"] * 10 +
        ["ENTERTAINMENT"] * 10 +
        ["SPORTS"] * 10 +
        ["WORLD NEWS"] * 10 +
        ["TECH"] * 10
    )
})

# Simulate popularity (random)
news_df['popularity'] = [random.randint(50, 500) for _ in range(len(news_df))]

top_categories = ["POLITICS", "ENTERTAINMENT", "SPORTS", "WORLD NEWS", "TECH"]

def recommend_by_interest(interests):
    filtered = news_df[news_df['category'].isin(interests)]
    return filtered.sample(n=min(10, len(filtered)))['headline'].tolist()

def get_most_popular(n=5):
    return news_df.sort_values(by='popularity', ascending=False).head(n)[['headline', 'popularity']]

# Random news feature
def get_random_news(n=3):
    return news_df.sample(n=n)['headline'].tolist()

# Streamlit UI
st.title("🗞️ News Recommendation for New Users")

# 🌟 Most Popular News
st.subheader("🔥 Most Popular News")
for i, row in get_most_popular().iterrows():
    st.write(f"**{row['headline']}** (🔥 {row['popularity']} views)")

# 🔍 Search news by keyword
search_query = st.text_input("🔎 Search news by keyword:")
if search_query:
    filtered_news = news_df[news_df['headline'].str.contains(search_query, case=False)]
    if not filtered_news.empty:
        st.subheader(f"Results for '{search_query}':")
        for i, row in filtered_news.iterrows():
            st.write(f"{i + 1}. {row['headline']}")
    else:
        st.warning(f"No news found for '{search_query}'.")

# 🧠 Interest-based News (Multiple Categories)
st.subheader("🎯 Get News Based on Your Interests")
selected_interests = st.multiselect("Select one or more interests:", top_categories, default=["TECH"])

if st.button("Show Recommendations"):
    recommendations = recommend_by_interest(selected_interests)
    if recommendations:
        st.subheader("📰 Top News for You:")
        for i, article in enumerate(recommendations, 1):
            st.write(f"{i}. {article}")
    else:
        st.info("No articles found for the selected categories.")

# 🌍 Random News Section
st.subheader("🎲 Discover Random News")
random_news = get_random_news()
for i, article in enumerate(random_news, 1):
    st.write(f"{i}. {article}")

# 📊 Category-wise News Count
st.subheader("📈 Category News Count")
category_counts = news_df['category'].value_counts()
for category, count in category_counts.items():
    st.write(f"{category}: {count} articles")
