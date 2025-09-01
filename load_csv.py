from req_bitcoin import request_bitcoin, dt
import pandas as pd

if __name__ == "__main__":
  try:
    data = pd.read_csv('bitcoin_saves.csv')
    if len(data) > 0:
       header=False
  except:
    header=True

  while True:
      try:
        df = request_bitcoin(lim_time=10, timestamp=dt.now())
        df.to_csv("bitcoin_saves.csv", mode="a", index=False, header=header)
        header=False
        print("Cotações inseridas com sucesso, maluco!!!!!!")
      except:
         print("Erro ao inserir")
         break
