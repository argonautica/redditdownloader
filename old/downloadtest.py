import pandas as pd
import requests
import json
import csv
import time
import datetime


def getPushshiftData(query, start, end, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?title=' + str(query) + '&size=1000&end=' + str(
        end) + '&start=' + str(start) + '&subreddit=' + str(sub)
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
    url = subm['url']
    try:
        flair = subm['link_flair_text']
    except KeyError:
        flair = "NaN"
    author = subm['author']
    sub_id = subm['id']
    score = subm['score']
    created = datetime.datetime.fromtimestamp(subm['created_utc'])  # 1520561700.0
    numComms = subm['num_comments']
    permalink = subm['permalink']
    comments = getCommentData(sub_id, limit)
    subData.append((sub_id, title, url, author, score, created, numComms, permalink, flair, comments))
    subStats[sub_id] = subData


print("enter start")
start = input()
temp = False
if start.isnumeric() and len(start) == 10 :
    temp = True

while temp == False:
    print("that is not valid, try again")
    start = input()
    if start.isnumeric() and len(start) == 10:
        temp = True
print("from the subreddit , enter the end date for the "
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


start = str(start)
print(start, end)
sub = 'askreddit'
# start and end dates
#start = "1590971471"  # October 1st
#end = "1590364800"  # January 1st
print(start, end)
query = "Screenshot"
subCount = 0
subStats = {}

data = getPushshiftData(query, start, end, sub)
# Will run until all posts have been gathered
# from the 'end' date up until start date
while len(data) > 0:
    for submission in data:
        collectSubData(submission, 10)
        subCount += 1
    # Calls getPushshiftData() with the created date of the last submission
    print(len(data))
    print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
    end = data[-1]['created_utc']
    data = getPushshiftData(query, end, start, sub)

print(len(data))

print(str(len(subStats)) + " submissions have added to list")
print("1st entry is:")
print(list(subStats.values())[0][0][1] + " created: " + str(list(subStats.values())[0][0][5]))
print("Last entry is:")
print(list(subStats.values())[-1][0][1] + " created: " + str(list(subStats.values())[-1][0][5]))


def updateSubs_file():
    upload_count = 0
    location = "downloaded/"
    print("input filename of submission file, please add .csv")
    filename = input()
    file = location + filename
    with open(file, 'w', newline='', encoding='utf-8') as file:
        a = csv.writer(file, delimiter=',')
        headers = ["Post ID", "Title", "Url", "Author", "Score", "Publish Date", "Total No. of Comments", "Permalink",
                   "Flair", "Comments"]
        a.writerow(headers)
        for sub in subStats:
            a.writerow(subStats[sub][0])
            upload_count += 1

        print(str(upload_count) + " submissions have been uploaded")


updateSubs_file()