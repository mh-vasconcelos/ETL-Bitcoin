from req_bitcoin import request_bitcoin, dt

url = "https://api.coinbase.com/v2/prices/spot"
timestamp = dt.now()
df = request_bitcoin(url, lim_time=30, timestamp=timestamp)
print(df)
