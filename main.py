import asyncio

from plugins import LOGS
from database.core import call, bot, user

from pytgcalls import idle


async def main():
    await bot.start()
    LOGS.info("[ INFO ] ✅ CLIENT.1 STARTED") # client.1 are pyrogram
    await call.start()
    LOGS.info("[ INFO ] ✅ CLIENT.2 STARTED") # client.2 are py-tgcalls
    
    await user.join_chat("levinachannel")
    await user.join_chat("VeezSupportGroup")
    
    await idle()
    await bot.stop()


loop = asyncio.get_event_loop_policy()
new_event_loop = loop.new_event_loop()
new_event_loop.run_until_complete(main())
