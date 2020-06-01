from bs4 import BeautifulSoup

import requests
url = "https://www.reddit.com/r/mac/comments/gtc7p6/im_not_fond_of_macbook_skins_but_this_one_is/"

response = requests.get(url)
print(type(response.content))
soup = BeautifulSoup(response.content)

soup = BeautifulSoup(soup.text)
print(soup)