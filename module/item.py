import re

import requests
import youtube_dl
from bs4 import BeautifulSoup


def find_search_content(search):
    request = requests.get("https://www.youtube.com/results?search_query={}".format(search))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    return soup


def find_video(soup, i=1):
    all_item = {}
    for element in soup.find_all('a', {"rel": "spf-prefetch"}):
        video_title = element.get('title')
        video_link = element.get('href')
        img_value = element.get("href").split("=")[1]
        all_img = soup.find_all("img", {"alt": True, "width": True, "height": True,
                                        "onload": ";window.__ytRIL && __ytRIL(this)", "data-ytimg": "1"})
        img = str(re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_value), str(all_img))[0]).strip("[\"\']")
        video_img = img.replace("&amp;", "&")
        all_item["{}".format(i)] = {
            "title": video_title,
            "link": "https://www.youtube.com{}".format(video_link),
            "img": video_img
        }
        i += 1
    return all_item


def video_time(soup, all_item, i=1):
    for time in soup.find_all("span", {"class": "video-time"}):
        all_item.get("{}".format(i))["time"] = time.text
        i += 1
    return all_item


def every_video(soup):
    all_item = find_video(soup)
    all_item = video_time(soup, all_item)
    return all_item


def page_bar(soup):
    page = {};
    for page_value in soup.find_all("a", {"class": True, "data-sessionlink": True, "data-visibility-tracking": True,
                                          "aria-label": True}):
        page['{}'.format(page_value.text)] = page_value.get("href")
    return page


def download_mp3(url):
    ydl_opts = {
        'outtmpl': '/audio/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_mp4(url):
    ydl_opts = {'outtmpl': '/video/%(title)s.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
