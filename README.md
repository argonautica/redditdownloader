# RedditDownloader
A simple CLI tool to download reddit text posts and comments. 

By default, reddit's API has a 1000 post cap on downloads. To get around this I wrote a simple script that queries [PushShift](https://pushshift.io/)  to download as many posts as wanted from a subreddit, between a specified time frame. 

### Prerequisites
For this to work, you will need to have [Python 3+](https://www.python.org/download/releases/3.0/), [PRAW](https://pypi.org/project/praw/) (The Python Reddit API Wrapper) and [prawcore](https://pypi.org/project/prawcore/) (a communication layer used by PRAW) downloaded.These can be downloaded individually using [PIP](https://pypi.org/).

If you have PIP already downloaded, you can use the simple command:
```shell script
pip install -r requirements.txt
```  


### Installation

Git clone this repository, then `cd` into the directory to run. 
```shell script
git clone https://github.com/argonautica/redditdownloader.git && cd redditdownloader
```
### Usage
As of now, the only way to use RedditDownloader is by running [redditdownloader.py](https://github.com/argonautica/redditdownloader/blob/master/redditdownloader.py).
Run it using: 
```shell script
python3 redditdownloader.py
```
You will be prompted to enter the the name of the subreddit you wish to download from, the start and ending dates that you would like to download from in [Unix Timestamp](https://www.unixtimestamp.com/index.php) format. 

After the download is complete, you will be prompted to enter the name of the file, and it will be saved in *.csv* format in the `/downloaded` folder.

### Notes

- tool does not support video, only images and text 
