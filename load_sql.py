from sqlalchemy import create_engine
# from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
import os
from req_bitcoin import request_bitcoin, dt
from urllib.parse import quote_plus
from sqlalchemy import text

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DB_NAME")

# URL-encode user/password para lidar com caracteres especiais
user_enc = quote_plus(USER)
pw_enc = quote_plus(PASSWORD)

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql://{user_enc}:{pw_enc}@{HOST}:{PORT}/{DBNAME}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})

SLEEP_SECONDS = 30

if __name__ == "__main__":
  # Test the connection
  try:
      with engine.connect() as connection:
          print("Connection successful!")
  except Exception as e:
      print(f"Failed to connect: {e}")

  # with engine.connect() as conn:
  #   result = conn.execute(text(
  #       "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'bitcoin';"
  #   ))
  #   print(result.fetchall())


  while True:
      df = request_bitcoin(lim_time=10, timestamp=dt.now())
      df.to_sql("bitcoin", engine, if_exists="append", index=False)
      # df.to_csv("bitcoin_saves.csv", mode="a", index=False, header=False)

      print("Cotações inseridas com sucesso, maluco!!!!!!")

