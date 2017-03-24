import re

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?q=NightCore+Shape+Of+You")
content = request.content
soup = BeautifulSoup(content, "html.parser")
for element in soup.find_all('a', {"rel": "spf-prefetch"}):
    img_value = element.get("href").split("=")[1]
    #print(img_value)
    all_img = soup.find_all("img", {"alt": True, "width": True, "height": True, "onload": ";window.__ytRIL && __ytRIL(this)", "data-ytimg": "1"})
    #print(all_img)
    img = str(re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_value), str(all_img))[0]).strip("[\"\']")
    video_img = img.replace("&amp;", "&")
    print(video_img)