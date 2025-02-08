import os
from sys import path

from dotenv import load_dotenv

load_dotenv()
print(os.path.dirname(__file__))
operations_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../operations"))

database_path = os.path.join(operations_path, 'operations.db')
overwrite_db = os.getenv("OVERWRITE_DB") == "1"