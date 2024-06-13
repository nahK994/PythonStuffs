import re
import requests
from PIL import Image
import os
import shutil
import time

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
    print(aa)
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

    folderName = re.findall(r'<div class="column collection_thumb">.*?title="(.*?)".*?href="https://wallpaperplay.com/board/(.*?)"', response1, re.S)

    '''
    print(len(folderName))
    for aaa in folderName:
        print(aaa[0] + '->' + aaa[1])
    '''

    for j in folderName:
        
        try:
            os.mkdir(fileName + "/" + i[1] + "/" + j[0])
        except FileExistsError:
            print("File initializing again.....")
            shutil.rmtree(fileName + "/" + i[1] + "/" + j[0])
            os.mkdir(fileName + "/" + i[1] + "/" + j[0])

        print('  ' + j[0])
        url2 = 'https://wallpaperplay.com/board/' + j[1]

        response2 = requests.get(url2)
        response2 = response2.text

        imageFilesURL = re.findall(r'data-fullimg="(.*?)"', response2, re.S)
        imageNumber = 1

        for k in imageFilesURL:

            imageFileName = str(imageNumber)
            imageNumber += 1
            startDownload = True

            k = 'https://wallpaperplay.com' + k
            print('   ', imageFileName, " downloading... ", k)

            while startDownload:
                startDownload = False
                try:
                    r = requests.get(k)
                    with open(fileName + "/" + i[1] + "/" + j[0] + "/" + imageFileName, "wb") as f:
                        f.write(r.content)        
                except:
                    print("     Failed")
                    startDownload = True
                    time.sleep(3)
                
print("DONE")