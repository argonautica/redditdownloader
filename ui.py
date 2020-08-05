# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import requests
import json
import csv
import time
import praw
from prawcore import NotFound


from PyQt5 import QtCore, QtGui, QtWidgets


# initialize reddit instance


reddit = praw.Reddit(client_id='2ICu9olD83K6OQ',
                     client_secret='6m4czcAQ7-XrvIyzkiwW0nkY-5Q',
                     user_agent='my user agent')


# check if subreddit exists, return true or false
def sub_exists(sub):
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists


#downloader functions

def getPushshiftData(query, after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?title='+str(query)+'&size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    r = requests.get(url)
    data = json.loads(r.text)
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
    subData.append((sub_id, title, created, url, author, score, numComms, permalink, flair, comments))
    subStats[sub_id] = subData









# class
class Ui_RedditDownloader(object):
    def setupUi(self, RedditDownloader):
        # if subreddit exists
        RedditDownloader.setObjectName("RedditDownloader")
        RedditDownloader.resize(611, 479)
        self.centralwidget = QtWidgets.QWidget(RedditDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label.setObjectName("label")
        self.SubredditName = QtWidgets.QLineEdit(self.centralwidget)
        self.SubredditName.setGeometry(QtCore.QRect(170, 20, 421, 21))
        self.SubredditName.setObjectName("SubredditName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 141, 16))
        self.label_2.setObjectName("label_2")
        self.StartDate = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.StartDate.setGeometry(QtCore.QRect(170, 50, 131, 22))
        self.StartDate.setObjectName("StartDate")
        self.EndDate = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.EndDate.setGeometry(QtCore.QRect(170, 80, 131, 22))
        self.EndDate.setObjectName("EndDate")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 141, 16))
        self.label_3.setObjectName("label_3")
        self.commentcount = QtWidgets.QSpinBox(self.centralwidget)
        self.commentcount.setGeometry(QtCore.QRect(260, 110, 42, 22))
        self.commentcount.setObjectName("commentcount")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 141, 16))
        self.label_4.setObjectName("label_4")
        self.results = QtWidgets.QTextBrowser(self.centralwidget)
        self.results.setGeometry(QtCore.QRect(20, 190, 571, 231))
        self.results.setObjectName("results")
        self.URLBox = QtWidgets.QCheckBox(self.centralwidget)
        self.URLBox.setGeometry(QtCore.QRect(330, 80, 86, 20))
        self.URLBox.setObjectName("URLBox")
        self.AuthorBox = QtWidgets.QCheckBox(self.centralwidget)
        self.AuthorBox.setGeometry(QtCore.QRect(440, 50, 86, 20))
        self.AuthorBox.setObjectName("AuthorBox")
        self.ScoreBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ScoreBox.setGeometry(QtCore.QRect(540, 50, 86, 20))
        self.ScoreBox.setObjectName("ScoreBox")
        self.PermalinkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.PermalinkBox.setGeometry(QtCore.QRect(440, 80, 86, 20))
        self.PermalinkBox.setObjectName("PermalinkBox")
        self.CommentBox = QtWidgets.QCheckBox(self.centralwidget)
        self.CommentBox.setGeometry(QtCore.QRect(330, 110, 86, 20))
        self.CommentBox.setObjectName("CommentBox")
        self.FlairBox = QtWidgets.QCheckBox(self.centralwidget)
        self.FlairBox.setGeometry(QtCore.QRect(540, 80, 86, 20))
        self.FlairBox.setObjectName("FlairBox")
        self.CommentCountBox = QtWidgets.QCheckBox(self.centralwidget)
        self.CommentCountBox.setGeometry(QtCore.QRect(440, 110, 121, 20))
        self.CommentCountBox.setObjectName("CommentCountBox")
        self.includeheader = QtWidgets.QLabel(self.centralwidget)
        self.includeheader.setGeometry(QtCore.QRect(330, 50, 121, 16))
        self.includeheader.setObjectName("includeheader")
        self.DownloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadButton.setGeometry(QtCore.QRect(250, 420, 112, 32))
        self.DownloadButton.setObjectName("DownloadButton")



        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 171, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 140, 411, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.WarningLabel = QtWidgets.QLabel(self.centralwidget)
        self.WarningLabel.setGeometry(QtCore.QRect(20, 170, 571, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.WarningLabel.setFont(font)
        self.WarningLabel.setText("")
        self.WarningLabel.setObjectName("WarningLabel")


        self.DownloadButton.clicked.connect(self.commencedownload)


        RedditDownloader.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RedditDownloader)
        self.statusbar.setObjectName("statusbar")
        RedditDownloader.setStatusBar(self.statusbar)


        self.retranslateUi(RedditDownloader)
        app.processEvents()

        # actions here





        QtCore.QMetaObject.connectSlotsByName(RedditDownloader)

    def retranslateUi(self, RedditDownloader):
        _translate = QtCore.QCoreApplication.translate
        RedditDownloader.setWindowTitle(_translate("RedditDownloader", "RedditDownloader"))
        self.label.setText(_translate("RedditDownloader", "Subreddit Name:"))
        self.label_2.setText(_translate("RedditDownloader", "Start Date/Time (UTC):"))
        self.label_3.setText(_translate("RedditDownloader", "End Date/Time (UTC):"))
        self.label_4.setText(_translate("RedditDownloader", "Number of Comments:"))
        self.URLBox.setText(_translate("RedditDownloader", "URL"))
        self.AuthorBox.setText(_translate("RedditDownloader", "Author"))
        self.ScoreBox.setText(_translate("RedditDownloader", "Score"))
        self.PermalinkBox.setText(_translate("RedditDownloader", "Permalink"))
        self.CommentBox.setText(_translate("RedditDownloader", "Comments"))
        self.FlairBox.setText(_translate("RedditDownloader", "Flair"))
        self.CommentCountBox.setText(_translate("RedditDownloader", "Comment Count"))
        self.includeheader.setText(_translate("RedditDownloader", "Include:"))
        self.DownloadButton.setText(_translate("RedditDownloader", "Download"))
        self.label_5.setText(_translate("RedditDownloader", "Download Path:"))


# functions go here





    def commencedownload(self):
        warning = ""
        sub = self.SubredditName.text()
        cc = self.commentcount.text()
        if not sub_exists(sub):
            warning += sub + " is not a valid subreddit"
            self.WarningLabel.setText(warning)
            self.WarningLabel.hide()
            self.WarningLabel.show()


            print("broken")
        else:

            start = 0
            end = 0
            self.StartDate.update()
            self.EndDate.update()
            start = time.mktime(self.StartDate.dateTime().toPyDateTime().timetuple())
            end = time.mktime(self.EndDate.dateTime().toPyDateTime().timetuple())



            ## check if start < end
            if start >= end:
                self.WarningLabel.setText("your start date should be before your end date!")
                self.WarningLabel.hide()
                self.WarningLabel.show()
            else:
                self.WarningLabel.setText("")
                self.WarningLabel.hide()
                self.WarningLabel.show()
            #  comment count is cc, subreddit name is name, start is start and end is end
            temp = self.URLBox.isChecked()
            print(temp)
            headers = [ "URL", "Comments", "Author", "Permalink", "Comment Count", "Score", "Flair"]
            checked = []
            checked.append(self.URLBox.isChecked())
            checked.append(self.CommentBox.isChecked())
            checked.append(self.AuthorBox.isChecked())
            checked.append(self.PermalinkBox.isChecked())
            checked.append(self.CommentCountBox.isChecked())
            checked.append(self.ScoreBox.isChecked())
            checked.append(self.FlairBox.isChecked())
            contains = []
            for h in range(len(headers)):
                print(str(headers[h]) + " has the status" + str(checked[h]))
                if checked[h]:
                    contains.append(headers[h])

            self.results.append("commencing download between" +time.ctime(int(start)) + " and " + time.ctime(int(end)))
            self.results.append("the download will contain all " + str(contains))
            self.results.hide()
            self.results.show()
            before = end
            after = start
            query = ""
            subCount = 0
            subStats = {}
            try:

                data = getPushshiftData(query, after, before, sub)
                # Will run until all posts have been gathered
                # from the 'after' date up until before date
                while len(data) > 0:
                    for submission in data:
                        collectSubData(submission, cc)
                        subCount += 1
                        print("Post Number " + str(subCount) + " has been downloaded.")
                    # Calls getPushshiftData() with the created date of the last submission
                    print(len(data))
                    print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
                    after = data[-1]['created_utc']
                    data = getPushshiftData(query, after, before, sub)
            except:
                print("oops, the download has accidentally failed at " + str(
                    datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
                print("The downloads so far will be saved , please restart the application at " + str(
                    data[-1]['created_utc']))















   # print(sub_exists(text))
    # print("okt")


def datetimetounix(str):
    year = str[-4:]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RedditDownloader = QtWidgets.QMainWindow()
    ui = Ui_RedditDownloader()
    ui.setupUi(RedditDownloader)
    RedditDownloader.show()
    app.exec_()
