__version__ = '8.5 Beta'


import time
import logging

from database.core import me_bot


logging.BasicConfig(
    filename=f'logs-{me_bot.id}.txt',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger('yt_dlp').setLevel(logging.ERROR)
logging.getLogger('pyrogram').setLevel(logging.ERROR)
logging.getLogger('pytgcalls').setLevel(logging.ERROR)


LOGS = logging.getLogger(__name__)
