from src.reddit_scraper import Scraper
from src.sentiment_analysis import SentimentAnalyzer
def main():
    scraper = Scraper('Politics', 'Biden')
    scraper.scrape()
    scraper.batchandStore()
    comments = scraper.comments

    analyzer = SentimentAnalyzer(comments)
    print(analyzer.analyze())
if __name__ == "__main__":
    main()
