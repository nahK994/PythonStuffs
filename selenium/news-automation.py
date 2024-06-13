from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime

# get date in format MMDDYYYY
now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

web = 'https://www.thesun.co.uk/sport/football/'
path = './chromedriver'  # introduce path here

# Headless mode
options = Options()
options.headless = True
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(web)

containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    try:
        title_container = container.find_element(by='xpath', value='./a/span')
        title = title_container.text
        titles.append(title)
    except:
        titles.append('')

    try:
        subtitle_container = container.find_element(by='xpath', value='./a/h3')
        subtitle = subtitle_container.text
        subtitles.append(subtitle)
    except:
        subtitles.append('')
    
    try:
        link_container = container.find_element(by='xpath', value='./a')
        link = link_container.get_attribute('href')
        links.append(link)
    except:
        links.append('')

# Exporting data to the same folder where the executable will be located
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'football_headlines_{month_day_year}.csv'
df_headlines.to_csv('./' + file_name)

driver.quit()
