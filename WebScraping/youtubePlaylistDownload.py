import re
import requests
from PIL import Image
import os
import shutil
from pytube import YouTube


url = 'https://www.youtube.com/playlist?list=PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG'
response = requests.get(url)
if response.ok:
    print('Ok')

response = response.text
#print(response)

fileName = 'Wallpapers'
path = fileName + ":/"
try:
    os.mkdir(fileName)
except FileExistsError:
    print("File initializing again.....")
    shutil.rmtree(fileName)
    os.mkdir(fileName)

contents = re.findall(r'<a class="pl-video-title-link.*?href="(.*?)&amp.*?".*?>(.*?)</a>', response, re.S)
link = 'https://www.youtube.com' + contents[0][0]
print(path)
print(link)

yt = YouTube(link)
yt.set_filename(contents[0][1])

video = yt.get('mp4', '720p')
video.download(path)

print("DONE")