from flask import Flask, request, jsonify
from flask_cors import CORS
from src.reddit_scraper import Scraper
from src.sentiment_analysis import SentimentAnalyzer

app = Flask(__name__)
CORS(app)  # ← allow all origins by default

@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.get_json(force=True)
    subreddit   = data.get('subreddit')
    search_term = data.get('search_term')
    if not subreddit or not search_term:
        return jsonify(error="Missing subreddit or search_term"), 400

    # 1) Scrape comments
    scraper = Scraper(subreddit, search_term)
    scraper.scrape()
    comments = scraper.getComments()  # list of (id, text)

    # 2) Analyze and collect scores
    analyzer = SentimentAnalyzer(comments)
    analyzer.analyze()
    scores = analyzer.getScores()     # dict { id: polarity }

    # 3) Return JSON
    return jsonify(scores)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
