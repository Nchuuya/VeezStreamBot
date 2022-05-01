from config import admins
from typing import Dict, List
from pyrogram.types import Chat
from pyrogram.enums import ChatMembersFilter


admins: Dict[int, List[int]] = {}


def set(chat_id: int, admins_: List[int]):
    admins[chat_id] = admins_


def get(chat_id: int) -> List[int]:
    if chat_id in admins:
        return admins[chat_id]
    return []


async def get_administrators(chat: Chat) -> List[int]:
    take = get(chat.id)

    if take:
        return take
    else:
        to_set = []
        administrators = await chat.get_members(
            filter=ChatMembersFilter.ADMINISTRATORS
        )

        for administrator in administrators:
            if administrator.can_manage_voice_chats:
                to_set.append(administrator.user.id)

        set(chat.id, to_set)
        return await get_administrators(chat)
