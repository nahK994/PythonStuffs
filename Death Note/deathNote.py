import re
import requests
from PIL import Image
import os
import shutil
import cv2

url = 'https://manganelo.com/chapter/death_note_colored_edition/chapter_2'
response = requests.get(url)
if response.ok:
    print('Ok')

response = response.text
#print(response)

folderName = re.findall(r'<h1>(.*?)</h1>', response)[0]
print(folderName)


try:
    os.mkdir(folderName)
except FileExistsError:
    print("File initializing again.....")
    shutil.rmtree(folderName)
    os.mkdir(folderName)


img = []
pattern = re.compile(r'<img src="(.*?)" alt', re.S)
pattern1 = re.compile(r'\d+\.jpg')
imageFilesURL = pattern.findall(response, re.S)
#num = 0

for i in imageFilesURL:

    fileName = pattern1.findall(i)
    if len(fileName) == 0:
        continue
    print(fileName[0], " downloading... ", i)

    r = requests.get(i)
    with open(folderName + "/" + fileName[0], "wb") as f:
        f.write(r.content)
    
    imageFile = Image.open(folderName + "/" + fileName[0])
    #img.append(imageFile)
    
    if imageFile.size[0] < 1700:
        img.append(imageFile)
    else:
        img.append(imageFile.crop((int(imageFile.size[0]/2), 0, imageFile.size[0]-1, imageFile.size[1]-1)))
        img.append(imageFile.crop((0, 0, int(imageFile.size[0]/2), imageFile.size[1]-1)))
    
    '''
    if num > 5:
        break
    num += 1
    '''


img[0].save(folderName + "/" + folderName + ".pdf", save_all=True, append_images=img[1:])
print("DONE")