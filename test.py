import html2text
from bs4 import BeautifulSoup
import requests

url = "https://www.reddit.com/r/mac/comments/gtc7p6/im_not_fond_of_macbook_skins_but_this_one_is/"
response = requests.get(url)
soup = BeautifulSoup(response.content)
print(html2text.html2text(soup.textpr))
