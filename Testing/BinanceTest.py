from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import matplotlib.pyplot as plt

api_key = "ElCyQOEuwezw51qUUj7v1kBva3oE"
api_secret= "f2ZYEdaTdiLo9bGE7kZqFcvK5khUj"

#https://python-binance.readthedocs.io/en/latest/

client = Client(api_key, api_secret)

prices = client.get_all_tickers()
for i in prices:
    if(i['symbol'].find("USD") >= 0):
        pass#print(i)
klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, "2 days ago UTC")
stLb = 10
ltLb = 45
lltLb = 100
data = []
#open time, open, high, low, close, volume, close time, quote assset volume, number of trades, taker buy base asset volume, taker buy quote asset volume, ignore
mv = 9999999999999
Mv = 0

mp = 99999999999999
Mp = 0

for k in klines:
    p = float(k[1])
    v = float(k[5])
    if p < mp:
        mp =p
    if p > Mp:
        Mp = p
    if v < mv:
        mv = v
    if v > Mv:
        Mv = v

scale = ((Mp-mp) / (Mv - mv))
shift = mp - mv * scale
print(mv, Mv, mp, Mp, mv * scale + shift, Mv * scale + shift)

for i in range(len(klines) - ltLb):
    iT = i + ltLb
    stTotal = 0
    for j in range(stLb):
        stTotal = stTotal + float(klines[iT-j][1])
    stAvg = stTotal / stLb

    ltTotal = 0
    for j in range(ltLb):
        ltTotal = ltTotal + float(klines[iT-j][1])
    ltAvg = ltTotal / ltLb
    data.append([float(klines[iT][1]), stAvg, ltAvg, float(klines[iT][5]) * scale + shift])
    #print([float(klines[i][1]), stAvg, ltAvg,float(klines[i][7]) ])

order = False
bp = 0
sp = 0
total = 0
buys = 0
fig, ax = plt.subplots()
n  = 0
for d in data:
    n = n + 1
    if(d[1] < d[2] and order == False):
        pass
    elif(d[1] < d[2] and order == True):
        sp = d[0]
        order = False
        total = total + (sp / bp)
        print("Sold at:" + str(sp))
        print("made:" + str(sp-bp) + ":"+str(total))
        ax.plot(n, d[0], 'ro')
    elif(d[1] > d[2] and order == False):
        order = True
        buys = buys + 1
        bp = d[0]
        print("bought at:" + str(bp))
        ax.plot(n, d[0], 'go')



print(total, total/buys, buys)

ax.plot(data)
plt.show()

