from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 𝐂σммαи∂ѕ ✨",
                callback_data="settings_back_helper",
            )
        ],
        [
            InlineKeyboardButton(
                text="📡 𝐔ρ∂αтєѕ",
                url=f"https://t.me/AloneXBots",
            ),
            InlineKeyboardButton(
                text="𝐒συяᴄє ❄️", url=config.GITHUB_REPO),
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ 𝐁σт 𝐒єттιиgѕ ⚙", callback_data="settings_helper"),
            )
        ]
    ]
    
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ❰ 𝐀∂∂ 𝐘συя 𝐆яσυρ ❱ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐇єℓρ 💖", callback_data="settings_back_helper"),
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐂нαииєℓ 💥", url=config.SUPPORT_CHANNEL),
            ),
            InlineKeyboardButton(
                text="🥀 𝐆яσυρ 💥", url=config.SUPPORT_GROUP),
            )
        ],
        [           
            InlineKeyboardButton(
                text="❄️ 𝐒συяᴄє ❄️", url=config.GITHUB_REPO),
            )
        ],
        [
            InlineKeyboardButton(
                text="♕ 𝐎ωиєя ♕", user_id=OWNER),
            )
        ]
     ]
    return buttons

close_key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✯ 𝐂ℓσѕє ✯", callback_data="close"
                    )
                ]
            ]
        )
