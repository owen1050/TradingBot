from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pathlib import Path
import time, datetime

def hourWrapAround(i):
    if i >= 0:
        return i
    return 24 + i

driverPath = str(Path(__file__).parents[1]) + "/geckodriverMac" #no exe on linux and swap the \\ with /
opts = Options()
opts.headless = True

driver = webdriver.Firefox(executable_path=driverPath, options=opts)

searchTerm = "BTCUSDT"
url = "https://www.hashtags.org/analytics/"+searchTerm+"/"

print("Loading url:" + url)
driver.set_window_size(1920, 1080)
driver.get(url)
time.sleep(0.2)
driver.save_screenshot('test.png')

source = str(driver.page_source)

i0 = source.rfind("<text text-anchor=\"end")
i1 = source.find("\">", i0)
i2 = source.find("</text>", i1)
maxValue = source[i1+2:i2]

iStop = i2

i0 = source.find("#_ABSTRACT_RENDERER_ID")
i1 = source[:i0].rfind("<circle")

data = []
now = datetime.datetime.now().timestamp()
count = -1

while(i1 > 0 and i1 < iStop):
    i2 = source.find("cx=", i1) + 4
    i3 = source.find("\"", i2)
    x = float(source[i2:i3])
    i2 = source.find("cy=", i3) + 4
    i3 = source.find("\"", i2)
    y = float(source[i2:i3])
    i1 = source.find("<circle", i3)
    if y < 350:
        timeEpoch = int(now - (24 - count) * 3600)
        datetimeTime = datetime.datetime.fromtimestamp(timeEpoch)
        uses = int(float(y * -0.004063 + 1.164)*float(maxValue.replace(',',""))) #only works for 4000
        data.append([datetimeTime, uses])
    count = count + 1

for d in data:
    print(d[0].hour, d[1])
print(maxValue, len(data))

