import re
import requests
import os
import shutil
from pytube import YouTube
import time

url = 'https://www.youtube.com/playlist?list=PL5O3zv2ZcASgNlf8UqqoWzmCwnqYNkvme'
response = requests.get(url)
if response.ok:
    print('Ok\n')


response = response.text
#print(response)
path = re.findall(r'<title>(.*?)</title>', response, re.S)[0]
path = path[:-10]

try:
    os.mkdir(path)
except FileExistsError:
    print("File initializing again.....")
    shutil.rmtree(path)
    os.mkdir(path)

os.chdir(path)
contents = re.findall(r'<a class="pl-video-title-link.*?href="(.*?)&amp.*?".*?>\s*(.*?)\s+</a>', response, re.S)
for i in contents:
    link = 'https://www.youtube.com' + i[0]
    
    print('downloading....... ' + i[1] + '.mp4')
    print()
    startDownload = True

    while startDownload:
        startDownload = False
        try:
            YouTube(link).streams.filter(subtype='mp4').get_highest_resolution().download()        
        except:
            print("Failed")
            startDownload = True
            time.sleep(3)
        #YouTube(link).streams.filter(subtype='mp4').get_highest_resolution().download()
    

print("DONE")