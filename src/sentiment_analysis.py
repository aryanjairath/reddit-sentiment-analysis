import csv
import re
class SentimentAnalyzer:
    def __init__(self, comments):
        self.comments = comments
    
    
    def analyze(self):
        for comment in self.comments:
                self.cleanse(comment[1])
                
    def cleanse(self, comment):
        comment = re.sub(r'\[.*?\]\(.*?\)', '', comment)
        comment = re.sub(r'https?://\S+|www\.\S+', '', comment)

        comment = re.split(r'[^a-zA-Z]+',comment)
        print(comment)
        
