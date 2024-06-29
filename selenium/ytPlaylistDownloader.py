from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
import requests

driver = webdriver.Chrome()
driver1 = webdriver.Chrome()
driver.get("https://www.youtube.com/playlist?list=PLWKjhJtqVAbn21gs5UnLhCQ82f923WCgM")
wait = WebDriverWait(driver, timeout=20)

def download_video(element):
    r = requests.get(element.get_attribute('href'))
    with open(element.get_attribute('download'), 'wb') as f:
        f.write(r.content)

# try:
playlist_video_elements = driver.find_elements(By.XPATH, value='//ytd-playlist-video-renderer')
for index, element in enumerate(playlist_video_elements):
    element = element.find_element(By.XPATH, value='.//a[@id="video-title"]')
    title = element.text
    url = element.get_attribute('href')
    print(f"{index+1}. {title} -> {url}")
    driver1.get('https://en1.savefrom.net')
    time.sleep(5)
    driver1.find_element(By.XPATH, value='//input[@placeholder="Paste your video link here"]').send_keys(url)
    driver1.find_element(By.XPATH, value="//button[@type='submit']").click()
    time.sleep(20)
    url_element_xpath = "//div[@class='drop-down-box']/div[@class='list']/div[@class='links']//a[contains(@title, 'video format') and not(contains(@title, 'without audio'))]"
    # wait.until(lambda d : driver1.find_element(By.XPATH, value="//div[not(contains(@id, 'output-captcha-dialog'))]"))
    url_elements = driver1.find_elements(By.XPATH, value=url_element_xpath)
    for index, element in enumerate(url_elements):
        url = element.get_attribute('href')
        print(f"url {index+1} ====> {element.get_attribute('title')}")
    
    if len(url_elements):
        download_video(url_elements[0])

# except KeyboardInterrupt:
#     print("Hh gag")
#     driver.quit()
#     driver1.quit()
# finally:
#     print("Hh")
#     driver.quit()
#     driver1.quit()

driver.quit()
driver1.quit()
