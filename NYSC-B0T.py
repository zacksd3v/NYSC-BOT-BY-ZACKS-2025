from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print(''' 
        ^^        |         ^^
       ::         |         ::
^^     ::         |         ::     ^^
::     ::         |         ::     ::
 ::     ::        |        ::     ::
   ::    ::       |       ::    ::
     ::    ::   _/~\_   ::    ::
       ::   :::/     \:::   ::
         :::::(       ):::::
               \ ___ /
          :::::/`   `\:::::
        ::    ::\o o/::    ::
      ::     ::  :":  ::     ::
    ::      ::   ` `   ::      ::
   ::      ::           ::      ::
  ::      ::             ::      ::  ZacksD3v
  ^^      ::             ::      ^^
          ::             ::
          ^^             ^^
------------------------------------------------

------------------------------------------------
D3VELOP3D BY Z4CKS CORP MEMBER BATCH AII 2025
BY FUN!
''')

def time_l(default_time=4):
    time.sleep(default_time)

Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=Service)

driver.get('https://portal.nysc.org.ng/nysc1/')

time_l()

class_name = driver.find_element(By.CSS_SELECTOR, 'a[href="ResumePayment.aspx"]')
class_name.click()

time_l()

inputs = driver.find_elements(By.XPATH, '//input[@name="ctl00$ContentPlaceHolder1$txtemailAddress"]')
inputs[0].send_keys('CORP-MEMBER-EMAIL')

time_l()

inputs = driver.find_elements(By.XPATH, '//input[@name="ctl00$ContentPlaceHolder1$txtPassCode"]')
inputs[0].send_keys('CORP-MEMBER-PSSWD')

time_l()

inputs = driver.find_element(By.XPATH, '//input[@type="submit"]')
inputs.click()

time_l()

all_the_way_down = driver.find_elements(By.XPATH,  "//div[@class='col-md-3']")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time_l(20)

clicking_clearence_link = driver.find_elements(By.XPATH, '//div[@id="ctl00_divmonthlyclearance"]')
clicking_clearence_link[0].click()

time_l(10)

back_to_dashboard = driver.find_elements(By.XPATH, '//div[@class="link"]')
back_to_dashboard[0].click()

time_l(180)

# driver.quit()