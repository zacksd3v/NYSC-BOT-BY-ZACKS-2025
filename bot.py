from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=Service)

driver.get('https://google.com/')

class_name = driver.find_element(By.CLASS_NAME, 'gLFyf')
class_name.send_keys('Nigerian coup 2025')
time.sleep(5)
class_name.send_keys(Keys.ENTER)


# bypassing = driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border')
bypassing = driver.find_elements(By.XPATH, '//div[@class="ecaptcha-checkbox-border"]')
bypassing.click()

time.sleep(90)

driver.quit()