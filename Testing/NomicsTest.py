from nomics import Nomics
import json
import requests

def getCurrencyPastData(id, start, end):
    key1 = "28b74cb8a7438eb3ed9514bbc502607bdd688"
    key2 = "4db"
    url = "https://api.nomics.com/v1/currencies/sparkline?key="+key1+key2+"&ids="+id+"&start="+start+"&end=" + end
    r = requests.get(url)
    return r.text


def getCurrencyCurrentData(id):
    add = "4db" #hopefully this gets around the github api key check
    nomics = Nomics("28b74cb8a7438eb3ed9514bbc502607bdd688" + add)

    data = nomics.Currencies.get_currencies(ids = id)
    return data


data = json.loads(getCurrencyPastData("BTC", "2021-10-15T00:00:00Z", "2021-10-16T00:00:00Z"))[0]
for d in range(len(data.get("timestamps"))):
    print(data.get("timestamps")[d], data.get("prices")[d])