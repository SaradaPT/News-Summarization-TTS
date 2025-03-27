from flask import Flask, request, jsonify
from myfolder.utils import extract_news_articles, analyze_article_sentiment, perform_comparative_analysis, generate_hindi_speech ,perform_summarization
#from myfolder.utils import analyze_article_sentiment
from myfolder import utils
import os

app = Flask(__name__)

@app.route('/fetch-news', methods=['GET'])
def fetch_news_data():
    """
    API endpoint to fetch news articles, analyze sentiment, and generate a comparative sentiment report.
    """
    company_name = request.args.get('company', '').strip()  

    if not company_name:
        return jsonify({"error": "Company name is required."}), 400  

    news_articles = extract_news_articles(company_name)

    if not news_articles:
        return jsonify({"error": f"No news articles found for {company_name}."}), 404  

    # Perform sentiment analysis on each article
    for article in news_articles:
        article["Article_Sentiment"] = analyze_article_sentiment(article["Article_Summary"])

    # Perform comparative sentiment analysis
    sentiment_comparison = perform_comparative_analysis(news_articles)

    # Generate Hindi text-to-speech output (only if there's valid content)
    combined_summary = " ".join([article["Article_Summary"] for article in news_articles if article["Article_Summary"] != "No Summary Available"])

    hindi_audio_file = generate_hindi_speech(combined_summary) if combined_summary.strip() else None  

    return jsonify({
        "Company": company_name,
        "News_Articles": news_articles,
        "Sentiment_Analysis": sentiment_comparison,
        "Hindi_Audio_File": hindi_audio_file if hindi_audio_file else "No valid summary to generate audio."
    })

# ✅ Use environment variable for safer debug mode
DEBUG_MODE = os.getenv("FLASK_DEBUG", "True") == "True"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=DEBUG_MODE)
