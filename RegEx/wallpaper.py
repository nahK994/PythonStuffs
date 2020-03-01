import re
import requests
from PIL import Image
import os
import shutil

#url = 'https://wallpapercave.com/minimalist-wallpapers'
url = 'https://wallpaperplay.com/board/4k-hd-wallpapers'
response = requests.get(url)
if response.ok:
    print('Ok')

response = response.text
#print(response)

#folderName = re.findall(r'slug="(.*?)" src=', response, re.S)[0]
folderName = re.findall(r'<h1.*?>(.*?)</h1>', response, re.S)[0]
print(folderName)

try:
    os.mkdir(folderName)
except FileExistsError:
    print("File initializing again.....")
    shutil.rmtree(folderName)
    os.mkdir(folderName)


#pattern = re.compile(r'<img data-url="(.*?)" slug', re.S)
pattern = re.compile(r'data-fullimg="(.*?)"', re.S)
imageFilesURL = pattern.findall(response)
num = 1

for i in imageFilesURL:

    fileName = str(num)
    num += 1
    #i = 'https://wallpapercave.com/wp/' + i + '.jpg'
    i = 'https://wallpaperplay.com' + i
    print(fileName, " downloading... ", i)

    r = requests.get(i)
    with open(folderName + "/" + fileName, "wb") as f:
        f.write(r.content)

print("DONE")
