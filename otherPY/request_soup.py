import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?q=NightCore+Shape+Of+You")
content = request.content
soup = BeautifulSoup(content, "html.parser")
print(soup)