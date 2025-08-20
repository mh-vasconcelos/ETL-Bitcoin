from req_bitcoin import request_bitcoin, dt

if __name__ == "__main__":
  header=True
  while True:
      df = request_bitcoin(lim_time=10, timestamp=dt.now())
      df.to_csv("bitcoin_saves.csv", mode="a", index=False, header=header)
      header=False
      print("Cotações inseridas com sucesso, maluco!!!!!!")