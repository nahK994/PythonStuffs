import re
import requests
from PIL import Image
import os
import shutil

url = 'https://www.youtube.com/playlist?list=PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG'

response = requests.get(url)
if response.ok:
    print('Ok')

with open("a.html", "w") as f:
    f.write(response.text)