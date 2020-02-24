import re
import requests
from PIL import Image
import os

url = 'https://manganelo.com/chapter/death_note_colored_edition/chapter_4'
response = requests.get(url)
if response.ok:
    print('Ok')

response = response.text
folderName = re.findall(r'title="Death Note \[Colored Edition\] (.*?) :.*1.*?>', response)[0]
print(folderName)
os.mkdir(folderName)

img = []
pattern = re.compile(r'<img src="(.*?)" alt', re.S)
pattern1 = re.compile(r'\d+\.jpg')
imageFilesURL = pattern.findall(response, re.S)


for i in imageFilesURL:

    fileName = pattern1.findall(i)
    if len(fileName) == 0:
        continue
    print(fileName[0], " downloading ... ", i)

    r = requests.get(i)
    with open(folderName + "/" + fileName[0], "wb") as f:
        f.write(r.content)
    img.append(Image.open(folderName + "/" + fileName[0]).convert('RGB'))


img[0].save(folderName + "/" + folderName + ".pdf", save_all=True, append_images=img[1:])
print("DONE")