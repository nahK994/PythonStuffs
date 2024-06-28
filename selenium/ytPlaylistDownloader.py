from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver1 = webdriver.Chrome()
driver.get("https://www.youtube.com/playlist?list=PLWKjhJtqVAbn21gs5UnLhCQ82f923WCgM")
wait = WebDriverWait(driver, timeout=10)

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
    time.sleep(15)
    url_elements = driver1.find_elements(By.XPATH, value="//div[@class='drop-down-box']/div[@class='list']/div[@class='links']//a")
    for index, element in enumerate(url_elements):
        url = element.get_attribute('href')
        print(f"url {index+1} ====> {url}")
    
    # driver1.quit()
    # driver.back()

driver.quit()
driver1.quit()
