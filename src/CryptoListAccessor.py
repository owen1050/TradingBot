from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pathlib import Path
import time

class CryptoListAccessor:

    #driverPath - path from the .. directory to the geckodriver you want to use
    #returns - 2d array of [name, symbol, marketCap, priceUSD, volume]s
    def getList(driverPath):

        driverPath = str(Path(__file__).parents[1]) + driverPath #no exe on linux and swap the \\ with /
        opts = Options()
        opts.headless = True

        driver = webdriver.Firefox(executable_path=driverPath, options=opts)

        url = "https://coinmarketcap.com/all/views/all/"

        driver.get(url)

        xButton = driver.find_element_by_xpath("/html/body/div/div[3]/div[2]")
        xButton.click()
        time.sleep(0.5)

        data = []
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

            temp = [name, symbol, marketCap, priceUSD, volume]
            data.append(temp)
            if i % 10 == 0:
                driver.execute_script("window.scrollTo(0, "+ str(i * 75)+")")
        return data