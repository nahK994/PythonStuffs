from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
print(f"Title = {title}")
driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

is_selected = driver.find_element(By.XPATH, value="//input[@id='my-check-1']").is_selected()
print(f"Checkbox 1 isSelected: {is_selected}")
is_selected = driver.find_element(By.XPATH, value="//input[@id='my-check-2']").is_selected()
print(f"Checkbox 2 isSelected: {is_selected}")
is_enabled = driver.find_element(By.XPATH, value="//input[@name='my-disabled']").is_enabled()
print(f"Disabled box isEnabled: {is_enabled}")
is_displayed = driver.find_element(By.XPATH, value="//select/option[@value='1']").is_displayed()
print(f"Drop down item isDisplayed: {is_displayed}")

text_box.send_keys("Selenium")
submit_button.click()
message = driver.find_element(by=By.ID, value="message")
text = message.text
print(text)
driver.quit()
