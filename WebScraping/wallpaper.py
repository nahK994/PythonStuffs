import re
import requests
from PIL import Image
import os
import shutil


url = 'https://wallpaperplay.com/board/anime-scenery-wallpapers'
response = requests.get(url)
if response.ok:
    print('Ok')

response = response.text
#print(response)


folderName = re.findall(r'<h1.*?>(.*?)</h1>', response, re.S)[0]
print(folderName)

try:
    os.mkdir(folderName)
except FileExistsError:
    print("File initializing again.....")
    shutil.rmtree(folderName)
    os.mkdir(folderName)


imageFilesURL = re.findall(r'data-fullimg="(.*?)"', response, re.S)
imageNumber = 1

for i in imageFilesURL:

    fileName = str(imageNumber)
    imageNumber += 1
    i = 'https://wallpaperplay.com' + i
    print(fileName, " downloading... ", i)

    r = requests.get(i)
    with open(folderName + "/" + fileName, "wb") as f:
        f.write(r.content)

print("DONE")