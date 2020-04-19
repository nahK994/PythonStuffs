import re
import requests
import os
import shutil
from pytube import YouTube


url = 'https://www.youtube.com/playlist?list=PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG'
#url = 'https://www.youtube.com/playlist?list=PLp1zSymEu3zJXITF_WuSPj32_Bni6062l'
response = requests.get(url)
if response.ok:
    print('Ok')


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


contents = re.findall(r'<a class="pl-video-title-link.*?href="(.*?)&amp.*?".*?>\s*(.*?)\s+</a>', response, re.S)
for i in contents:
    link = 'https://www.youtube.com' + i[0]
    #fileName = i[1] + '.mp4'
    fileName = YouTube(link).streams.filter(subtype='mp4').get_highest_resolution().download()
    index = 0
    for i in range(len(fileName)):
        if fileName[i] == '/':
            index = i
    fileName = fileName[index+1:]
    print('downloading.......')
    print(fileName)
    print(link)
    print()

    shutil.move(fileName, path)


print("DONE")