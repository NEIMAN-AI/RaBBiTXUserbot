from os import getenv

from dotenv import load_dotenv
import os
import asyncio
import sys
import time

from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
HNDLR = os.getenv("HNDLR", ".")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
ALIVE_MSG = os.getenv("ALIVE_MSG", "")
PING_MSG = os.getenv("PING_MSG", "")
LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)

__version__ = "v0.1"

if os.path.exists(".env"):
    load_dotenv(".env")
    
if os.path.exists(".env"):
    load_dotenv(".env")

#_______________________________________________________________________________________________________________#
