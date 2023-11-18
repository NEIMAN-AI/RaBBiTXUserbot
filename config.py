from os import getenv

from dotenv import load_dotenv

load_dotenv()

# API_IDS
API_ID = int(getenv("API_ID")) # API_ID get it from my.telegram.org
API_HASH = getenv("API_HASH") # API_HASH get it from my.telegram.org

# DATABASES
MONGO_URL = getenv("MONGO_URL", None)

# SESSION
SESSION = getenv("SESSION", None)

# TOKEN
BOT_TOKEN = getenv("BOT_TOKEN", None)

# IMAGES
ALIVE_PIC = getenv("ALIVE_PIC", None)