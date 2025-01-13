import praw
import random
import time
from datetime import datetime

# List of keywords to filter relevant posts you can add more
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
]

chosen_user_agent = random.choice(user_agents)

reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent=chosen_user_agent
)

# List of subreddits to stream from
subreddits = ['subreddit1', 'subreddit2','subreddit3']

# List of keywords to filter relevant posts
keywords = ['keyword1', 'keyword2', 'keyword three','keyword four and so on']

# Stream and print results in real-time
while True:
    for subreddit_name in subreddits:
        try:
            print(f"Streaming from subreddit: {subreddit_name}")
            for submission in reddit.subreddit(subreddit_name).stream.submissions():
                # Check if the submission title contains relevant keywords
                if any(keyword.lower() in submission.title.lower() for keyword in keywords):
                    date_posted = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')
                    print(f"Title: {submission.title}\nSubreddit: {subreddit_name}\nURL: {submission.url}\nDate Posted: {date_posted}\n")
        except Exception as e:
            print(f"Error streaming from subreddit {subreddit_name}: {e}")

    # Sleep for a short time to avoid too frequent requests and hitting rate limits
    time.sleep(10)