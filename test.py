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

def time_l():
    time.sleep(2)

Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=Service)

# driver.get('https://portal.nysc.org.ng/')
driver.get('https://portal.nysc.org.ng/nysc1/')

time_l()

class_name = driver.find_element(By.CSS_SELECTOR, 'a[href="ResumePayment.aspx"]')
class_name.click()

time_l()

inputs = driver.find_elements(By.XPATH, '//input[@name="ctl00$ContentPlaceHolder1$txtemailAddress"]')
inputs[0].send_keys('CORPS-MEMBER-EMAIL')

time_l()

inputs = driver.find_elements(By.XPATH, '//input[@name="ctl00$ContentPlaceHolder1$txtPassCode"]')
inputs[0].send_keys('CORPS-MEMBER-PASSWD')

time_l()

inputs = driver.find_element(By.XPATH, '//input[@type="submit"]')
inputs.click()


# input_element = driver.find_element(By.CLASS_NAME, 'clients-logo-wrapper text-center row')
# input_element.send_keys('portal nysc' + Keys.ENTER)

# capture_click = driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border')
# capture_click.click()

# link = driver.find_element(By.CSS_SELECTOR, "a[href='https://ResumePayment.aspx']")
# link = driver.find_element(By.CSS_SELECTOR, "a[href='https://portal.nysc.org.ng/nysc1/ResumePayment.aspx']")
# link.click()

time.sleep(90)

driver.quit()