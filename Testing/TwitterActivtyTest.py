from selenium import webdriver
from pathlib import Path
import time

driverPath = str(Path(__file__).parents[1]) + "\\geckodriver.exe" #no exe on linux and swap the \\ with /
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()

driver = webdriver.Firefox(executable_path=driverPath, firefox_options=fireFoxOptions)

searchTerm = "shib"
url = "https://www.hashtags.org/analytics/"+searchTerm+"/"

driver.get(url)
time.sleep(1)
driver.save_screenshot('test.png')
print(driver.page_source)
