from pyrogram import filters
from typing import List, Union
from config import cmd_handler


filters_ex = (
    filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded
)
filters_in = (
    filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, cmd_handler)
