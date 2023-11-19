import os
import asyncio
import sys
import time
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from config import SESSION, API_ID, API_HASH, HNDLR

contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Rabbit/Modules"))
call_py = PyTgCalls(bot)


hl = HNDLR[0]
start_time = time.time()
