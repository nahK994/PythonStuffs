import re
import requests
from PIL import Image
import os
import shutil

url = 'https://www.tonesmp3.com/bollywood-ringtones/1/'

response = requests.get(url)
if response.ok:
    print('Ok')

with open("a.html", "w") as f:
    f.write(response.text)