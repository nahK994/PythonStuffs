import re
import requests
import os
import shutil


url = 'https://www.tonesmp3.com/'
response = requests.get(url)
if response.ok:
    print('Ok')

response = response.text
#print(response)

fileName = 'Ringtones'
try:
    os.mkdir(fileName)
except FileExistsError:
    print("File initializing again.....")
    shutil.rmtree(fileName)
    os.mkdir(fileName)


genres = re.findall(r'<li class="list-group-item footer-list">.*?<a href="(https://www.tonesmp3.com/.*?/)">(.*?)</a></li>', response, re.S)
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

    url1 = i[0]
    #print(url1)
    
    response1 = requests.get(url1)
    response1 = response1.text
    
    
    aa = re.findall(r'</li>.*<li><a href="https://www.tonesmp3.com/.*?/(.*?)/">Last</a></li>', response1, re.S)
    lastPageNumber = 2
    if len(aa) == 1:
        lastPageNumber = int(aa[0])
    

    for pageNumber in range(1, lastPageNumber+1):

        response2 = requests.get(url1 + str(pageNumber) + '/')
        response2 = response2.text

        mp3files = re.findall(r'<div class="box-play" onclick="audioplayer.*?(https://www.tonesmp3.com/ringtones/.*?.*?\.mp3).*?;"', response2, re.S)
        titles = re.findall(r'<h3 class="tone-title">(.*?)</h3>', response2, re.S)
        
        '''
        print(url1 + str(pageNumber) + '/', '---->', len(titles))
        for iii in titles:
            print('------->', iii)
        '''

        for tones in range(len(titles)):

            print(titles[tones], '    downloading...  ', mp3files[tones])
            r = requests.get(mp3files[tones])

            with open(fileName + "/" + i[1] + "/" + titles[tones], "wb") as f:
                f.write(r.content)


print("DONE")