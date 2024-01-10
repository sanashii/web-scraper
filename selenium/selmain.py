from selenium import webdriver
import time

PATH = r"C:\Program Files (x86)\chromedriver.exe"

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Specify the executable path using the add_argument method
options.add_argument("executable_path=" + PATH)

# Pass options to the Chrome driver
driver = webdriver.Chrome(options=options)

driver.get("https://www.reddit.com/r/SHFiguarts/comments/107sx8d/is_this_gohan_worth_getting/")
print(driver.title)

time.sleep(20)
driver.quit()