from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pathlib import Path
import time

driverPath = str(Path(__file__).parents[1]) + "\\geckodriver.exe" #no exe on linux and swap the \\ with /
opts = Options()
opts.headless = True

driver = webdriver.Firefox(executable_path=driverPath, options=opts)

searchTerm = "shib"
url = "https://www.hashtags.org/analytics/"+searchTerm+"/"

print("Loading url:" + url)
driver.get(url)
time.sleep(0.2)
driver.save_screenshot('test.png')

source = str(driver.page_source)

i0 = source.find("<text text-anchor=\"middle")
i1 = source.find("\">", i0)
i2 = source.find("</text>", i1)
firstTime = source[i1+2:i2]

i0 = source.rfind("<text text-anchor=\"middle")
i1 = source.find("\">", i0)
i2 = source.find("</text>", i1)
lastTime = source[i1+2:i2]

i0 = source.rfind("<text text-anchor=\"end")
i1 = source.find("\">", i0)
i2 = source.find("</text>", i1)
maxValue = source[i1+2:i2]

i0 = source.find("#_ABSTRACT_RENDERER_ID")
i1 = source[:i0].rfind("<circle")

data = []

while(i1 > 0):
    i2 = source.find("cx=", i1) + 4
    i3 = source.find("\"", i2)
    x = float(source[i2:i3])
    i2 = source.find("cy=", i3) + 4
    i3 = source.find("\"", i2)
    y = float(source[i2:i3])
    i1 = source.find("<circle", i3)

    data.append([x,y])

print(data, firstTime, lastTime, maxValue)
