from src.reddit_scraper import Scraper
from src.sentiment_analysis import SentimentAnalyzer
def main():
    scraper = Scraper('Sports', 'Lebron')
    scraper.scrape()
    scraper.batchandStore()
    comments = scraper.getComments()

    analyzer = SentimentAnalyzer(comments)
    analyzer.analyze()
    print(analyzer.getScores())
if __name__ == "__main__":
    main()
