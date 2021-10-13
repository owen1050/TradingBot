from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["doge"]
results = pytrends.get_historical_interest(kw_list, year_start=2021, month_start=10, day_start=11, hour_start=19, year_end=2021, month_end=10, day_end=12, hour_end=22, cat=0, geo='', gprop='', sleep=0)
#results is a type=pandas.core.frame.DataFrame
#results.iloc[i][0] loop through i to get values
# results.iloc[][] is type pandas._libs.tslibs.timestamps.timestamp
length = len(results.index)
data = []
for i in range(length):
    epoch = (results.index[i].to_pydatetime())
    data.append([epoch, results.iloc[i][0]])

print(data)