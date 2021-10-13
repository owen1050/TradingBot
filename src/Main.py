from TwitterActivityAccessor import TwitterActivityAccessor
from CryptoListAccessor import CryptoListAccessor
from GoogleTrendsAccessor import GoogleTrendsAccessor

driverPath = "/geckodriverMac" #\\geckodriver.exe for windows /geckodriver for linux

if False:
    data = TwitterActivityAccessor.getActivity("twitter", driverPath)

if False:
    data = CryptoListAccessor.getList(driverPath)

if True:
    data = GoogleTrendsAccessor.getLast24HoursByHour("doge")

print(data)