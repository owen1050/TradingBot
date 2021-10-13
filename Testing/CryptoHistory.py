from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pathlib import Path
import time

print("Loading website...")
driverPath = str(Path(__file__).parents[1]) + "/geckodriverMac" #no exe on linux and swap the \\ with /
opts = Options()
opts.headless = True

driver = webdriver.Firefox(executable_path=driverPath, options=opts)

url = "https://coinmarketcap.com/currencies/amun-bitcoin-3x-daily-short/historical-data/"

driver.get(url)

xButton = driver.find_element_by_xpath("/html/body/div/div[3]/div[2]")
xButton.click()
print("website loaded")
time.sleep(0.5)

data = []
print("Collecting data", end = "")
for i in range(1,175):
    temp = []
    
    nameXpath = "/html/body/div/div[1]/div[2]/div/div[1]/div/div[2]/div[3]/div/table/tbody/tr["+ str(i) +"]/td[2]/div/a[2]"
    sumbXpath = "/html/body/div/div[1]/div[2]/div/div[1]/div/div[2]/div[3]/div/table/tbody/tr["+ str(i) +"]/td[3]/div"
    mkCpXpath = "/html/body/div/div[1]/div[2]/div/div[1]/div/div[2]/div[3]/div/table/tbody/tr["+ str(i) +"]/td[4]/p/span[2]"
    priceXpat = "/html/body/div/div[1]/div[2]/div/div[1]/div/div[2]/div[3]/div/table/tbody/tr["+ str(i) +"]/td[5]/div/a"
    volumXpat = "/html/body/div/div[1]/div[2]/div/div[1]/div/div[2]/div[3]/div/table/tbody/tr["+ str(i) +"]/td[7]/a"
    name = driver.find_element_by_xpath(nameXpath).text
    symbol = driver.find_element_by_xpath(sumbXpath).text
    marketCap = driver.find_element_by_xpath(mkCpXpath).text
    priceUSD = driver.find_element_by_xpath(priceXpat).text
    volume = driver.find_element_by_xpath(volumXpat).text
    
    temp = [i, name, symbol, marketCap, priceUSD, volume]
    data.append(temp)
    if i % 10 == 0:
        print("", end='.')
        driver.execute_script("window.scrollTo(0, "+ str(i * 75)+")")

for d in data:
    print(d)