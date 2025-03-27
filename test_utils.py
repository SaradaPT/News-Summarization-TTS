from myfolder.utils import extract_news_articles, analyze_article_sentiment, perform_comparative_analysis, generate_hindi_speech

# Test News Extraction
print("🔍 Testing News Extraction...")
articles = extract_news_articles("Tesla")
print(articles)

# Test Sentiment Analysis
print("\n📊 Testing Sentiment Analysis...")
if articles:
    for article in articles:
        sentiment = analyze_article_sentiment(article["Article_Summary"])
        print(f"Title: {article['Article_Title']} | Sentiment: {sentiment}")

# Test Comparative Sentiment Analysis
print("\n📉 Testing Comparative Analysis...")
sentiment_summary = perform_comparative_analysis(articles)
print(sentiment_summary)

# Test Hindi Text-to-Speech
print("\n🔊 Testing Hindi Text-to-Speech...")
if articles:
    combined_text = " ".join([article["Article_Summary"] for article in articles])
    hindi_audio = generate_hindi_speech(combined_text)
    print(f"Hindi TTS File Generated: {hindi_audio}")
