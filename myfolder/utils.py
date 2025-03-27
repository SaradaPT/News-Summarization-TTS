import requests
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from transformers import pipeline
from gtts import gTTS
from gnews import GNews

# Download required NLTK resources
nltk.download("vader_lexicon", quiet=True)

def extract_news_articles(company_name):
    """
    Extracts the latest news articles related to the given company name using GNews API.

    Args:
        company_name (str): The name of the company to search for news.

    Returns:
        list: A list of dictionaries containing article titles, summaries, and URLs.
    """
    try:
        print(f"🔍 Fetching news for: {company_name}")

        google_news = GNews(language='en', country='US', max_results=5)
        news_articles = google_news.get_news(company_name)

        print(f"✅ Found {len(news_articles)} articles.")

        if not news_articles:
            return []

        news_list = []
        for article in news_articles:
            title = article.get("title", "No Title")
            summary = article.get("description", "No Summary Available")
            url = article.get("url", "#")

            print(f"📌 Title: {title}")  # Debugging output
            news_list.append({
                "Article_Title": title,
                "Article_Summary": summary,
                "Article_URL": url
            })

        return news_list
    except Exception as e:
        print(f"❌ Error fetching news: {e}")
        return []

def analyze_article_sentiment(text):
    """
    Analyzes the sentiment of the given text using NLTK's VADER.

    Args:
        text (str): The article's text.

    Returns:
        str: Sentiment category ('Positive', 'Negative', 'Neutral').
    """
    try:
        sia = SentimentIntensityAnalyzer()
        sentiment_score = sia.polarity_scores(text)["compound"]

        if sentiment_score >= 0.05:
            return "Positive 😊"
        elif sentiment_score <= -0.05:
            return "Negative 😡"
        else:
            return "Neutral 😐"
    except Exception as e:
        print(f"❌ Error analyzing sentiment: {e}")
        return "Unknown 😶"

def perform_summarization(text):
    """
    Summarizes the given text using a pre-trained Transformer model.

    Args:
        text (str): The article's text.

    Returns:
        str: Summarized version of the text.
    """
    try:
        if len(text.split()) < 50:
            return "⚠️ Text too short for summarization!"
        
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"❌ Error summarizing text: {e}")
        return "Summarization Failed!"

def perform_comparative_analysis(news_articles):
    """
    Performs comparative sentiment analysis across multiple news articles.

    Args:
        news_articles (list): List of articles with titles and summaries.

    Returns:
        dict: Sentiment analysis summary.
    """
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for article in news_articles:
        sentiment = analyze_article_sentiment(article["Article_Summary"])
        sentiment_counts[sentiment.split()[0]] += 1  # Extract sentiment type

    return sentiment_counts

def generate_hindi_speech(text):
    """
    Converts text to Hindi speech using Google Text-to-Speech (gTTS).

    Args:
        text (str): The text to convert.

    Returns:
        str: The file path of the generated audio file.
    """
    try:
        tts = gTTS(text=text, lang="hi")
        output_audio_file = "news_summary_audio.mp3"
        tts.save(output_audio_file)
        return output_audio_file
    except Exception as e:
        print(f"❌ Error generating speech: {e}")
        return None
