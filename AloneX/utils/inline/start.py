from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴊᴀɴᴀ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(text="Cᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="Sᴏᴜʀᴄᴇ", url=config.SUPPORT_GROUP),
        ],
        ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴊᴀɴᴀ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text="Dᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER),
            InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons

close_key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]
            ]
        )
