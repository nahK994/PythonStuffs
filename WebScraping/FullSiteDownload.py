import re
import requests
from PIL import Image
import os
import shutil


url = 'https://wallpaperplay.com/'
response = requests.get(url)
if response.ok:
    print('Ok')

response = response.text
#print(response)

fileName = 'Wallpapers'
try:
    os.mkdir(fileName)
except FileExistsError:
    print("File initializing again.....")
    shutil.rmtree(fileName)
    os.mkdir(fileName)


genres = re.findall(r'<a href="https://wallpaperplay.com/genres/(.*?)" class="category_sidebar item">(.*?)</a>', response, re.S)
'''
print(len(genres))
for aa in genres:
    print(aa[0] ,' :D ', aa[1])
'''

for i in genres:
    print('\n' + i[1])

    try:
        os.mkdir(fileName + "/" + i[1])
    except FileExistsError:
        print("File initializing again.....")
        shutil.rmtree(fileName + "/" + i[1])
        os.mkdir(fileName + "/" + i[1])
    
    url1 = 'https://wallpaperplay.com/genres/' + i[0]
    response1 = requests.get(url1)
    response1 = response1.text


    folderName = re.findall(r'<div class="column collection_thumb">.*?href="https://wallpaperplay.com/board/(.*?)"', response1, re.S)
    print(len(folderName))
    for j in folderName:

        try:
            os.mkdir(fileName + "/" + i[1] + "/" + j)
        except FileExistsError:
            print("File initializing again.....")
            shutil.rmtree(fileName + "/" + i[1] + "/" + j)
            os.mkdir(fileName + "/" + i[1] + "/" + j)

        print('  ' + j)
        url2 = 'https://wallpaperplay.com/board/' + j

        response2 = requests.get(url2)
        response2 = response2.text


        imageFilesURL = re.findall(r'data-fullimg="(.*?)"', response2, re.S)
        imageNumber = 1

        for k in imageFilesURL:

            imageFileName = str(imageNumber)
            imageNumber += 1
            k = 'https://wallpaperplay.com' + k
            print('   ', imageFileName, " downloading... ", k)

            r = requests.get(k)
            with open(fileName + "/" + i[1] + "/" + j + "/" + imageFileName, "wb") as f:
                f.write(r.content)

print("DONE")