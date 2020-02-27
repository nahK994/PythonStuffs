import re
import requests
from PIL import Image
import os
import shutil

#url = 'https://wallpapercave.com/minions-wallpaper'
url = 'https://wallpapercave.com/batman-wallpaper'
response = requests.get(url)
if response.ok:
    print('Ok')

response = response.text
#print(response)

folderName = re.findall(r'slug="(.*?)" src=', response, re.S)[0]
print(folderName)

try:
    os.mkdir(folderName)
except FileExistsError:
    print("File initializing again.....")
    shutil.rmtree(folderName)
    os.mkdir(folderName)


pattern = re.compile(r'<img data-url="(.*?)" slug', re.S)
imageFilesURL = pattern.findall(response)
#print(imageFilesURL, len(imageFilesURL))

for i in imageFilesURL:

    fileName = i
    i = 'https://wallpapercave.com/wp/' + i + '.jpg'
    print(fileName, " downloading ... ", i)

    r = requests.get(i)
    with open(folderName + "/" + fileName, "wb") as f:
        f.write(r.content)

print("DONE")