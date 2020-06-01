import praw
reddit = praw.Reddit(client_id='2ICu9olD83K6OQ',
                     client_secret='6m4czcAQ7-XrvIyzkiwW0nkY-5Q',
                     user_agent='my user agent')

print(reddit.read_only)

temp = 0
for submission in reddit.subreddit('redditdev').top(limit=2000):
    #print(submission.selftext)
    temp += 1
print(temp)