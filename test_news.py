from gnews import GNews

def test_extract_news_articles(company_name):
    """
    Tests the extraction of the latest news articles using GNews API.

    Args:
        company_name (str): The company name to search for news.

    Returns:
        None
    """
    try:
        print(f"🔍 Fetching news for: {company_name}\n")
        
        # Initialize GNews API
        google_news = GNews(language='en', country='US', max_results=5)
        
        # Fetch news articles
        news_articles = google_news.get_news(company_name)

        if not news_articles:
            print("⚠️ No news articles found. Try another company.\n")
            return

        # Display fetched news articles
        for index, article in enumerate(news_articles, start=1):
            print(f"📰 Article {index}:")
            print(f"Title: {article.get('title', 'No Title Available')}")
            print(f"Summary: {article.get('description', 'No Summary Available')}")
            print(f"URL: {article.get('url', '#')}\n")
    
    except Exception as e:
        print(f"❌ Error fetching news: {e}\n")

# Run test
if __name__ == "__main__":
    company_name = input("Enter a company name: ")
    test_extract_news_articles(company_name)
