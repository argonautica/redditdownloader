import requests
import json
import csv
import time
import datetime
import praw
from prawcore import NotFound
import datetime




reddit = praw.Reddit(client_id='2ICu9olD83K6OQ',
                     client_secret='6m4czcAQ7-XrvIyzkiwW0nkY-5Q',
                     user_agent='my user agent')



def sub_exists(sub):
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists

def getPushshiftData(query, after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?title='+str(query)+'&size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']


def getCommentData(id, limit):
    url = 'https://api.pushshift.io/reddit/comment/search/?link_id=' + str(id) + '&limit=' + str(limit)
    r = requests.get(url)
    data = json.loads(r.text)['data']
    collected = []
    for comment in data:
        collected.append(comment['body'])
    return collected


    return data['data']




def collectSubData(subm, limit):
    subData = list()  # list to store data points
    title = subm['title']
    sub_id = subm['id']


    subData.append((title))
    subStats[sub_id] = subData


if reddit.read_only:
    print("reddit has loaded, welcome to reddit-downloader")

temp = False
print("Enter the name of the subreddit that you would like to search from :")
print("eg: for r/askreddit you would enter \"askreddit\"")
t = input()
temp = sub_exists(t)
while temp is False:
    print("such a subreddit does not exist! try again: ")
    t = input()
    temp = sub_exists(t)

print("from the subreddit " + t + " , enter the start date for the "
                                  "posts you would like to download, in unix timestamp format")
start = input()
temp = False
if start.isnumeric() and len(start) == 10 :
    temp = True

while temp == False:
    print("that is not valid, try again")
    start = input()
    if start.isnumeric() and len(start) == 10:
        temp = True
print("from the subreddit " + t + ", enter the end date for the "
                                  "posts you would like to download, in unix timestamp format")
end = input()
temp = False
if end.isnumeric() and len(end) == 10 :
    temp = True

while temp == False:
    print("that is not valid, try again")
    end = input()
    if end.isnumeric() and len(end) == 10:
        temp = True


print("enter the number of comments that you would like to download from each post")
cc = input()
temp = False
if cc.isnumeric()  :
    temp = True

while temp == False:
    print("that is not valid, try again")
    cc = input()
    if cc.isnumeric():
        temp = True

print("commencing download from " + t + " in between " + time.ctime(int(start)) + " and " + time.ctime(int(end)))
sub= t
#before and after dates


before = end
after = start
#after = "1590364800"  #January 1st

#before = "1590971471" #October 1st
query = ""
subCount = 0
subStats = {}


data = getPushshiftData(query, after, before, sub)
# Will run until all posts have been gathered
# from the 'after' date up until before date
while len(data) > 0:
    for submission in data:
        collectSubData(submission, 10)
        subCount += 1
    # Calls getPushshiftData() with the created date of the last submission
    print(len(data))
    print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
    after = data[-1]['created_utc']
    data = getPushshiftData(query, after, before, sub)

print(len(data))

print(str(len(subStats)) + " submissions have added to list")
print("1st entry is:")
print(list(subStats.values())[0][0][1] + " created: " + str(list(subStats.values())[0][0][5]))
print("Last entry is:")
print(list(subStats.values())[-1][0][1] + " created: " + str(list(subStats.values())[-1][0][5]))



