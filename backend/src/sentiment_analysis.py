import csv
import re
from textblob import TextBlob



class SentimentAnalyzer:
    def __init__(self, comments):
        self.comments = comments
        self.scores = {}
    
    def getScores(self):
        return self.scores
     
    def analyze(self):
        for comment in self.comments:
            self.cleanse(comment[0])
            self.scores[comment[0]] = TextBlob(comment[0]).sentiment.polarity
        
    def cleanse(self, comment):
        comment = re.sub(r'\[.*?\]\(.*?\)', '', comment)
        comment = re.sub(r'https?://\S+|www\.\S+', '', comment)

        comment = re.split(r'[^a-zA-Z]+',comment)
        # print(comment)
        
