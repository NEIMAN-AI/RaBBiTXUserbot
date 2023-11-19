import asyncio
from pytgcalls import idle
from Rabbit import call_py, bot


async def main():
    print("[•RaBBiTX•] Pyrogram client starting....")
    await bot.start()
    print("[•RaBBiTX•] py-tgcalls client starting...")
    await call_py.start()
    print(
        """
    ------------------------
   | !tnx |
    ------------------------
"""
    )
    await idle()
    await pidle()
    print("[•RaBBiTX•] stoping client....")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
