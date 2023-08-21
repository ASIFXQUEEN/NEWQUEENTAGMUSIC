from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ✨",
                callback_data="settings_back_helper"),
            )
        ],
        [
            InlineKeyboardButton(
                text="📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬",
                url=f"https://t.me/AloneXBots",
            ),
            InlineKeyboardButton(
                text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬",
                url=f"https://t.me/AlonesHeaven",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ 𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 ⚙", callback_data="settings_helper"),
            )
        ]
    ]
    
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ❰ 𝐀𝐝𝐝 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐇𝐞𝐥𝐩 💖", callback_data="settings_back_helper"),
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💥", url=config.SUPPORT_CHANNEL),
            ),
            InlineKeyboardButton(
                text="🥀 𝐆𝐫𝐨𝐮𝐩 💥", url=config.SUPPORT_GROUP),
            )
        ],
        [           
            InlineKeyboardButton(
                text="❄️ 𝐒𝐨𝐮𝐫𝐜𝐞 ❄️", url=config.GITHUB_REPO),
            )
        ],
        [
            InlineKeyboardButton(
                text="♕ 𝐎𝐰𝐧𝐞𝐫 ♕", user_id=OWNER),
            )
        ]
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
