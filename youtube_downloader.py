from pytube import YouTube
import os

# Where to save the video
os.makedirs("videos", exist_ok=True)
DOWNLOAD_FOLDER = "videos"
url = "https://www.youtube.com/watch?v=_bfkYbLgs5s"

yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)