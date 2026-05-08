from dotenv import load_dotenv
import os

load_dotenv()

#db config

DB_HOST = os.getenv('DB_HOST','localhost')
DB_PORT = os.getenv('DB_PORT','5432')
DB_NAME = os.getenv('DB_NAME','retail_supply_network')
DB_USER = os.getenv('DB_USER','postgresql')
DB_PASSWORD = os.getenv('DB_PASSWORD','password')

JWT_KEY= os.getenv('JWT_KEY','jwtkeydeafult')
SUPER_USER_KEY= os.getenv('SUPER_USER_TOKEN','jwtkeydeafult')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
