import re

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?q=NightCore+Shape+Of+You")
content = request.content
soup = BeautifulSoup(content, "html.parser")
for time in soup.find_all("span", {"class": "video-time"}):
    print(time.text)
