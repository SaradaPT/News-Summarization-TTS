import streamlit as st
from myfolder.utils import (
    extract_news_articles, 
    analyze_article_sentiment, 
    perform_comparative_analysis, 
    generate_hindi_speech, 
    perform_summarization
)

# Streamlit App Title
st.title("📰 News Summarization & Text-to-Speech Application")

# User Input: Company Name
company_name = st.text_input("Enter a company name", placeholder="Tesla") 

if st.button("Analyze News"):
    if not company_name:
        st.error("❌ Please enter a company name.")
    else:
        st.write(f"🔍 **Fetching news for:** `{company_name}`...")  # Debugging output

        # Extract News Articles
        news_articles = extract_news_articles(company_name)

        # Debugging: Print article count in UI
        st.write(f"✅ **Articles received:** `{len(news_articles)}`")  

        if not news_articles:
            st.error("❌ No news articles found. Try another company.")
        else:
            # Display Articles
            st.subheader("📌 Extracted News Articles")
            for article in news_articles:
                st.write(f"**Title:** {article.get('Article_Title', 'No Title')}")
                st.write(f"**Summary:** {article.get('Article_Summary', 'No Summary Available')}")
                st.write(f"**URL:** [Read more]({article.get('Article_URL', '#')})")

                # Analyze Sentiment
                sentiment = analyze_article_sentiment(article['Article_Summary'])
                st.write(f"**Sentiment:** {sentiment}")
                st.write("---")

            # Perform Comparative Sentiment Analysis
            st.subheader("📊 Comparative Sentiment Analysis")
            sentiment_summary = perform_comparative_analysis(news_articles)
            st.json(sentiment_summary)

            # Generate Hindi Speech
            st.subheader("🔊 Hindi Text-to-Speech Output")
            combined_summary = " ".join([article["Article_Summary"] for article in news_articles])
            audio_filepath = generate_hindi_speech(combined_summary)

            if audio_filepath and isinstance(audio_filepath, str):  
                st.audio(audio_filepath)
            else:
                st.error("❌ Error generating Hindi audio.")
