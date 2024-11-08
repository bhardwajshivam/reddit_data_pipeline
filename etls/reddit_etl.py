from utils.constants import CLIENT_ID, SECRET
from praw import Reddit
import sys

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id = client_id,
                             client_secret = client_secret,
                             user_agent = user_agent)
        print("connected to reddit!!")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)

def extract_post(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter, limit=limit)

    print(posts)