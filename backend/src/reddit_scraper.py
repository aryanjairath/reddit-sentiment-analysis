import praw
import csv
from pathlib import Path
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 

class Scraper:
    def __init__(self, subreddit, searchterm):
        load_dotenv() 
        self.subreddit = subreddit
        self.searchterm = searchterm
        self.reddit = praw.Reddit(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            user_agent="My Example App by u/SceneImportant8866"  
        )
        self.comments = []
    def scrape(self):
        subreddit = self.reddit.subreddit(self.subreddit)
        posts = subreddit.search(self.searchterm, limit=1, sort="new") 
        for post in posts:
            post.comments.replace_more(limit=0)  # Get all top-level comments
            for comment in post.comments.list():
                self.comments.append([
                    comment.body,
                    comment.score
                ])
                
    def getComments(self):
        return self.comments
    
    def batchandStore(self):
        try:
            os.mkdir("./data")
        except OSError as e:
            print("Directory exists")

        with open('./data/comments.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Text", "Score"])
            for comment in self.comments:
                writer.writerow([comment[0], comment[1]])


