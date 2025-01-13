import praw
import random
from datetime import datetime

# List of user-agent strings
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
]

# Randomly choose a user agent
chosen_user_agent = random.choice(user_agents)

# PRAW setup
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent=chosen_user_agent
)

# Fetch submissions and print details
print(f"Using User-Agent: {chosen_user_agent}\n")

search_results = reddit.subreddit('all').search('keyword', sort='new', limit=10)
submissions = []

# Collect submissions
for submission in search_results:
    submissions.append({
        "title": submission.title,
        "url": submission.url,
        "created_utc": submission.created_utc
    })

# Sort submissions by date (latest first)
submissions.sort(key=lambda x: x['created_utc'], reverse=True)

# Print results
for submission in submissions:
    date_posted = datetime.utcfromtimestamp(submission['created_utc']).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Title: {submission['title']}\nURL: {submission['url']}\nDate Posted: {date_posted}\n")