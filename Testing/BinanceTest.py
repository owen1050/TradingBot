from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
api_key = "ElCyQOEuwezw51qUUj7v1kBva3o95zA5e7Lqjmp###############"
api_secret= "f2ZYEdaTdiLo9bGE7c2ecEKoHWzkAhHSZlSgnJSm0FN02X############"
#https://python-binance.readthedocs.io/en/latest/
client = Client(api_key, api_secret)

prices = client.get_all_tickers()

print(len(prices))