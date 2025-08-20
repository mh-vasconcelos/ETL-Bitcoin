import requests
from datetime import datetime as dt, timedelta as td
import time
import pandas as pd

url = "https://api.coinbase.com/v2/prices/spot"
# response = requests.get(url)

# preco = float(response.json()['data']['amount'])
# ativo = response.json()['data']['base']
# moeda = response.json()['data']['currency']
timestamp = dt.now()

def request_bitcoin(url="https://api.coinbase.com/v2/prices/spot", lim_time = 60, timestamp = None):
  if timestamp:
    lim = timestamp + td(seconds=lim_time)
  else:
    return "No Timestampt found"
  
  precos = []
  moedas = []
  ativos = []
  timestamps = []
  while dt.now() < lim:
    response = requests.get(url)
    preco = float(response.json()['data']['amount'])
    ativo = response.json()['data']['base']
    moeda = response.json()['data']['currency']
    precos.append(preco)
    ativos.append(ativo)
    moedas.append(moeda)
    timestamps.append(dt.now())
    time.sleep(4)


  df = pd.DataFrame({
    "preco": precos,
    "ativo": ativos,
    "moeda": moedas,
    "timestamp": timestamps
  })

  return df


