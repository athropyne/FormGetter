import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))

ONE_PATTERN_ONLY = False
