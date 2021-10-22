from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pathlib import Path
import time, os

print("Loading website...")
cwd = os.getcwd()
i0 = cwd.rfind("/")
driverPath = cwd[:i0] + "/geckodriverMac" #no exe on linux and swap the \\ with /
opts = Options()
opts.headless = True
opts.acceptInsecureCerts = True

driver = webdriver.Firefox(executable_path=driverPath)#, options=opts)

url = "https://lunarcrush.com"

driver.get(url)
driver.set_window_size(1920, 1080)
time.sleep(5)
driver.save_screenshot("ss.png")

daily = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/ul/div[1]/a[2]")
href = daily.get_attribute('href')
print(href)
driver.get(href)

dailyCoinTicker = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div/span/a")


