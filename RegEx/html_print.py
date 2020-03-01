import re
import requests
from PIL import Image
import os
import shutil

url = 'https://www.youtube.com/playlist?list=PLhfHPmPYPPRk6yMrcbfafFGSbE2EPK_A6'

response = requests.get(url)
if response.ok:
    print('Ok')

with open("a.txt", "w") as f:
    f.write(response.text)