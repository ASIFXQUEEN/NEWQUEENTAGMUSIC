from typing import Union
import re
import os
from os import getenv

from dotenv import load_dotenv

from pyrogram import filters


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
load_dotenv()
YOUR_GROUP = getenv("YOUR_GROUP", "")
YOUR_CHANNEL = getenv("YOUR_CHANNEL", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")

def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋 ғᴇᴀᴛᴜʀᴇ 🦋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️ sᴇᴛᴛɪɴɢ ⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ ᴏᴡɴᴇʀ ✨", url=f"https://t.me/{OWNER_USERNAME}",
            ),
            InlineKeyboardButton(
                text="🔎 ʜᴇʟᴘ 🔎", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💫 sᴜᴘᴘᴏʀᴛ 💫", url=f"https://t.me/{YOUR_GROUP}",
            ),
            InlineKeyboardButton(
                text="🍁 ᴜᴘᴅᴀᴛᴇs 🍁", url=f"https://t.me/{YOUR_CHANNEL}",
            )
        ],
        [
            InlineKeyboardButton(
                text="❄️ sᴏᴜʀᴄᴇ ❄️",
                url=f"https://github.com/AloneXBot/AloneX",
            )
        ],
     ]
    return buttons
