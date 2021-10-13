from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pathlib import Path
import time, datetime

print("Loading website...")
driverPath = str(Path(__file__).parents[1]) + "/geckodriverMac" #no exe on linux and swap the \\ with /
opts = Options()
opts.headless = True

driver = webdriver.Firefox(executable_path=driverPath, options=opts)
driver.set_window_size(1920, 1080)
url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/"

driver.get(url)

print("website loaded")
time.sleep(1)

data = []

# click this /html/body/div/div/div[1]/div[2]/div/div[3]/div/div/div[1]/span/button
dateRangeXpath = "/html/body/div/div/div[1]/div[2]/div/div[3]/div/div/div[1]/span/button"
# clikc this /html/body/div/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/ul/li[4]
oneEightyDaysXpath = "/html/body/div/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/ul/li[5]"
# click this /html/body/div/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[2]/span/button
contButtonXpath = "/html/body/div/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[2]/span/button"

driver.find_element_by_xpath(dateRangeXpath).click()
driver.find_element_by_xpath(oneEightyDaysXpath).click()
driver.find_element_by_xpath(contButtonXpath).click()
now = datetime.datetime.now().timestamp()
for i in range(1,350):
    temp = []
    temp.append(now)
    try:
        for j in range(2,8):
            xPath = "/html/body/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]"
            tempStr = float(str(driver.find_element_by_xpath(xPath).text).replace("$","").replace(",", ""))
            temp.append(tempStr)

        if i % 50 == 0:
            driver.execute_script("window.scrollTo(0, "+ str(i * 500)+")")
        print(temp)
        data.append(temp)

    except:
        pass
    now = now - 86400

for d in data:
    print(d)