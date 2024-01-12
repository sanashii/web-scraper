import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #this module allows us to have access to keyboard keys such as enter, esc, and etc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

os.environ['PATH'] += r";C:/SeleniumDrivers"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

driver.get("https://www.reddit.com/?rdt=37323")
driver.implicitly_wait(30) # similar to time.sleep(30) but this method is used for times when an element is already found and will then move on
# ^^ more efficient than time.sleep() method
print(driver.title)

search = driver.find_element(By.ID, "login-button")
search.click()
# search.send_keys("jujutsu kaisen") # what we want to search for
# search.send_keys(Keys.RETURN) # return is basically enter so we're clicking enter after searching

# print(driver.page_source)

WebDriverWait(driver, 30).until( # explicit wait which wil wait until a condition is true
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'mt-md text-14'),
        ' New to Reddit? '
    )
)


driver.quit()
