from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime

def wait_func(class_name, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
    except TimeoutException:
        pass

def scrool_into_view(element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)


# get date in format MMDDYYYY
now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

web = 'https://www.wallpaperflare.com/'
path = './chromedriver'  # introduce path here

# # Headless mode
# options = Options()
# options.headless = True
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)

container = driver.find_element(by='xpath', value="//li/figure/a")
scrool_into_view(container)
# image_page_url = container.get_attribute('href')

wait_func('item shadow', 5)
image = driver.find_element(by='xpath', value='//figure/a[@itemprop="url"]')
# scrool_into_view(image)
image.click()

wait_func('pl-3ff1c800b6e719c0389db99dee445e5d__closelink', 10)
try:
    driver.find_element(by='xpath', value='//div[@class="pl-3ff1c800b6e719c0389db99dee445e5d__closelink"]').click()
except:
    pass
wait_func('item_left_btns greencolor')
driver.find_element(by='xpath', value='//a[@class="item_left_btns greencolor"]').click()
