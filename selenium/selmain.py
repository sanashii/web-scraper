import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #this module allows us to have access to keyboard keys such as enter, esc, and etc
import time

os.environ['PATH'] += r";C:/SeleniumDrivers"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

driver.get("https://www.reddit.com/?rdt=37323")
driver.implicitly_wait(30) # similar to time.sleep(30) but this method is used for times when an element is already found and will then move on so we dont have to explicitly wait (time.sleep)
print(driver.title)

search = driver.find_element(By.ID, "login-button")
search.click()
# search.send_keys("jujutsu kaisen") # what we want to search for
# search.send_keys(Keys.RETURN) # return is basically enter so we're clicking enter after searching

# print(driver.page_source)

# while True:
#     pass
time.sleep(30)

driver.quit()
