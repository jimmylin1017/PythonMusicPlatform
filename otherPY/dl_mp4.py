# https://github.com/rg3/youtube-dl/blob/master/README.md#embedding-youtube-dl

from __future__ import unicode_literals
import youtube_dl

ydl_opts = {'outtmpl': '/video/%(title)s.%(ext)s'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=9w2-n3adU0c'])