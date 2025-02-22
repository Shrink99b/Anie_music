import asyncio

from plugins import LOGS
from pytgcalls import idle
from config import BOT_USERNAME as cli

async def start_bot():
    LOGS.info("[INFO]: BOT & ANIEUSERBOT CLIENT STARTED !!")
    LOGS.info("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await idle()
    LOGS.info("[INFO]: BOT & USERBOT STOPPED !!")

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
