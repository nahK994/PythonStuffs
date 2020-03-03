import re
import requests
from PIL import Image
import os
import shutil

url = 'https://wallpaperplay.com/genres/abstract'

response = requests.get(url)
if response.ok:
    print('Ok')

with open("a.txt", "w") as f:
    f.write(response.text)