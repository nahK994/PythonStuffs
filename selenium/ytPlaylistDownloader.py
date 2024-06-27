from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/playlist?list=PLWKjhJtqVAbn21gs5UnLhCQ82f923WCgM")

playlist_video_elements = driver.find_elements(By.XPATH, value='//ytd-playlist-video-renderer')
for index, element in enumerate(playlist_video_elements):
    title = element.find_element(By.XPATH, value='.//a[@id="video-title"]').text
    print(f"{index+1}. {title}")

driver.quit()
