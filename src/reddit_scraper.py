import praw
import csv
from pathlib import Path
import os

class Scraper:
    def __init__(self, subreddit, searchterm):
        self.subreddit = subreddit
        self.searchterm = searchterm
        self.reddit = praw.Reddit(
            client_id="4H3os77d01qGsBXbfl7cUA",
            client_secret="UnpeSghMrqMsROz0wtuAAdYsRnfkOA",
            user_agent="My Example App by u/SceneImportant8866"  
        )
        self.comments = []
    def scrape(self):
        subreddit = self.reddit.subreddit(self.subreddit)
        posts = subreddit.search(self.searchterm, limit=1, sort="new") 
        for post in posts:
            post.comments.replace_more(limit=0)  # Get all top-level comments
            for comment in post.comments.list():
                self.comments.append([post.title,
                    comment.body,
                    comment.score
                ])

    def batchandStore(self):
        try:
            os.mkdir("./data")
        except OSError as e:
            print("Directory exists")



        with open('./data/comments.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["PostTitle", "Text", "Score"])
            for comment in self.comments:
                writer.writerow([comment[0], comment[1], comment[2]])


