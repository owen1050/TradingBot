from TwitterActivityAccessor import TwitterActivityAccessor
from CryptoListAccessor import CryptoListAccessor
from GoogleTrendsAccessor import GoogleTrendsAccessor
from CryptoHistoryAccessor import CryptoHistoryAccessor

driverPath = "\\geckodriver.exe" #\\geckodriver.exe for windows /geckodriver for linux

if False:
    data = TwitterActivityAccessor.getActivity("twitter", driverPath)

if False:
    data = CryptoListAccessor.getList(driverPath)

if False:
    data = GoogleTrendsAccessor.getLast24HoursByHour("doge")

if True:
    data = CryptoHistoryAccessor.getDailyForNDays(100, "https://coinmarketcap.com/currencies/bitcoin/historical-data/", driverPath)

print(data)