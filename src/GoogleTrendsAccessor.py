from pytrends.request import TrendReq
from calendar import monthrange
import datetime


class GoogleTrendsAccessor:

    #searchTerm - what you want data on
    #returns - 2d array of dateTime and relative popularity of search term over hours
    def getLast24HoursByHour(searchTerm):

        pytrends = TrendReq(hl='en-US', tz=360)
        kw_list = [searchTerm]
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour

        yearStart = year
        monthStart = month
        dayStart = day

        if day - 1 > 0:
            dayStart = day-1
        elif month - 1 > 0:
            monthStart = month - 1
            dayStart = monthrange(year, monthStart)[1]
        else:
            yearStart = year - 1
            monthStart = 12
            dayStart = 31

        results = pytrends.get_historical_interest(kw_list, year_start=yearStart, month_start=monthStart, day_start=dayStart, hour_start=hour, year_end=year, month_end=month, day_end=day, hour_end=hour, cat=0, geo='', gprop='', sleep=0)
        #results is a type=pandas.core.frame.DataFrame
        #results.iloc[i][0] loop through i to get values
        # results.iloc[][] is type pandas._libs.tslibs.timestamps.timestamp
        length = len(results.index)
        data = []
        for i in range(length):
            epoch = (results.index[i].to_pydatetime())
            data.append([epoch, results.iloc[i][0]])

        return data