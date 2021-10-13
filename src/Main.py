from TwitterActivityAccessor import TwitterActivityAccessor
from CryptoListAccessor import CryptoListAccessor
from GoogleTrendsAccessor import GoogleTrendsAccessor

driverPath = "/geckodriverMac" #\\geckodriver.exe for windows /geckodriver for linux

if False:
    data = TwitterActivityAccessor.getActivity("twitter", driverPath)

if True:
    data = CryptoListAccessor.getList(driverPath)

if False:
    data = GoogleTrendsAccessor.getLast24HoursByHour("doge")

print(data)