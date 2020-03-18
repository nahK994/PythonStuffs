import re
import requests
from PIL import Image
import os
import shutil


#url = 'https://www.youtube.com/watch?v=bytnxnZFLeg'
url = 'https://www.tonesmp3.com/ringtones/moni-nobow-by-vreegu-kashyap.mp3'

response = requests.get(url)
if response.ok:
    print('Ok')

r = requests.get(url, stream = True)
with open('a.mp3', 'wb') as f:
    for chunk in r.iter_content(chunk_size=256):
        f.write(chunk)

#response = response.text
#print(response)