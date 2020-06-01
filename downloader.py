import praw
from prawcore import NotFound
import psaw

reddit = praw.Reddit(client_id='2ICu9olD83K6OQ',
                     client_secret='6m4czcAQ7-XrvIyzkiwW0nkY-5Q',
                     user_agent='my user agent')

print(reddit.read_only)
def sub_exists(sub):
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists

print(sub_exists("alkd"))