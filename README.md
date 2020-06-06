# RedditDownloader
A simple CLI tool to download reddit text posts and comments. 

### Prerequisites
For this to work, you will need to have [Python 3+](https://www.python.org/download/releases/3.0/), [PRAW](https://pypi.org/project/praw/) (The Python Reddit API Wrapper) and [prawcore](https://pypi.org/project/prawcore/) (a communication layer used by PRAW) downloaded.These can be downloaded individually using [PIP](https://pypi.org/).

If you have PIP already downloaded, you can use the simple command:
```shell script
pip install -r requirements.txt
```  


###Installation

Git clone this repository, then `cd` into the directory to run
```shell script
git clone https://github.com/argonautica/redditdownloader.git && cd redditdownloader
```
###Usage
As of now, the only way to use RedditDownloader is by running [redditdownloader.py](https://github.com/argonautica/redditdownloader/blob/master/redditdownloader.py).
Run it using: 
```shell script
python3 redditdownloader.py
```