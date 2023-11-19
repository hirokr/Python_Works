import os
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("WK_PATH")
print(path)
