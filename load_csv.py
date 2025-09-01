from req_bitcoin import request_bitcoin, dt
import os
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

CSV_PATH = "bitcoin_saves.csv"
if __name__ == "__main__":
  CONT = 0
  header = not (os.path.exists(CSV_PATH) and os.path.getsize(CSV_PATH) > 0)

  while True:
      try:
        df = request_bitcoin(lim_time=10, timestamp=dt.now())
        df.to_csv("bitcoin_saves.csv", mode="a", index=False, header=header, lineterminator='\n')
        if header:
          header=False
        print("Cotações inseridas com sucesso, maluco!!!!!!")
      except KeyboardInterrupt:
        logging.info("Interrompido pelo usuário. Saindo.")
        break
      except Exception:
        CONT += 1
        logging.exception(f"Erro ao inserir cotações (tentativa {CONT}/5).")
        if CONT >= 5:
            logging.error("Número máximo de tentativas alcançado. Encerrando.")
            break
        time.sleep(5)
        continue
