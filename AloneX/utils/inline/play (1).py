import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP, YOUR_GROUP, YOUR_CHANNEL
from AloneX import app

import config
from AloneX.utils.formatters import time_to_seconds


## After Edits with Timer ba

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    alone = math.floor(percentage)
    if 0 < alone <= 2:
        ba = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < alone < 3:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 3 <= alone < 4:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 4 <= alone < 5:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 6 <= alone < 7:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 7 <= alone < 8:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 9 <= alone < 10:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 11 <= alone < 12:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 12 <= alone < 13:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 13 < alone < 14:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 14 <= alone < 15:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 15 <= alone < 16:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 16 <= alone < 17:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 17 <= alone < 18:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 18 <= alone < 19:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 19 <= alone < 20:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 20 <= alone < 21:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 21 <= alone < 22:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 22 <= alone < 23:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 23 <= alone < 24:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 24 <= alone < 25:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 25 <= alone < 26:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 26 <= alone < 27:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 27 <= alone < 28:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 28 <= alone < 29:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 29 <= alone < 30:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 30 <= alone < 31:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 31 <= alone < 32:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 32 <= alone < 33:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 33 <= alone < 34:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 34 <= alone < 35:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 35 <= alone < 36:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 36 <= alone < 37:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 37 <= alone < 38:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 38 <= alone < 39:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 39 <= alone < 40:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 40 <= alone < 41:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 41 <= alone < 42:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 42 <= alone < 43:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 43 <= alone < 44:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 44 < alone < 45:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 45 <= alone < 46:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 46 <= alone < 47:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 47 <= alone < 48:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 48 <= alone < 49:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 49 <= alone < 50:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 50 <= alone < 51:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 51 <= alone < 52:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 52 <= alone < 53:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 53 <= alone < 54:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 54 <= alone < 55:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 55 <= alone < 56:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 56 <= alone < 57:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 57 <= alone < 58:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 58 <= alone < 59:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 59 <= alone < 60:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= alone < 61:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 61 <= alone < 62:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 62 <= alone < 63:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 63 <= alone < 64:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 64 <= alone < 65:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 65 <= alone < 66:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 66 <= alone < 67:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 67 <= alone < 68:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 68 <= alone < 69:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 69 <= alone < 70:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 70 <= alone < 71:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 71 <= alone < 72:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 72 <= alone < 73:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 73 <= alone < 74:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 74 <= alone < 75:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 75 <= alone < 76:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 76 < alone < 77:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 77 <= alone < 78:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 78 <= alone < 79:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 79 <= alone < 80:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 80 <= alone < 81:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 81 <= alone < 82:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 82 <= alone < 83:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 83 <= alone < 84:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 84 <= alone < 85:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 85 <= alone < 86:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 86 <= alone < 87:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 87 <= alone < 88:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 88 <= alone < 89:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 89 <= alone < 90:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 90 <= alone < 91:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 91 <= alone < 92:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 92 <= alone < 93:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 93 <= alone < 94:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 94 <= alone < 95:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 95 <= alone < 96:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 96 <= alone < 97:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 97 <= alone < 98:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 98 <= alone < 99:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    else:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"

        buttons  = [

        [
            InlineKeyboardButton(
                text=f"{played} {ba} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),

          ],

          [
            InlineKeyboardButton(

                text="▷",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="II", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▢", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons
                


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    alone = math.floor(percentage)
    if 0 < alone <= 2:
        ba = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < alone < 3:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 3 <= alone < 4:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 4 <= alone < 5:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 6 <= alone < 7:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 7 <= alone < 8:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 9 <= alone < 10:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 11 <= alone < 12:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 12 <= alone < 13:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 13 < alone < 14:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 14 <= alone < 15:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 15 <= alone < 16:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 16 <= alone < 17:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 17 <= alone < 18:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 18 <= alone < 19:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 19 <= alone < 20:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 20 <= alone < 21:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 21 <= alone < 22:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 22 <= alone < 23:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 23 <= alone < 24:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 24 <= alone < 25:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 25 <= alone < 26:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 26 <= alone < 27:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 27 <= alone < 28:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 28 <= alone < 29:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 29 <= alone < 30:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 30 <= alone < 31:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 31 <= alone < 32:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 32 <= alone < 33:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 33 <= alone < 34:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 34 <= alone < 35:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 35 <= alone < 36:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 36 <= alone < 37:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 37 <= alone < 38:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 38 <= alone < 39:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 39 <= alone < 40:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 40 <= alone < 41:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 41 <= alone < 42:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 42 <= alone < 43:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 43 <= alone < 44:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 44 < alone < 45:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 45 <= alone < 46:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 46 <= alone < 47:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 47 <= alone < 48:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 48 <= alone < 49:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 49 <= alone < 50:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 50 <= alone < 51:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 51 <= alone < 52:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 52 <= alone < 53:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 53 <= alone < 54:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 54 <= alone < 55:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 55 <= alone < 56:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 56 <= alone < 57:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 57 <= alone < 58:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 58 <= alone < 59:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 59 <= alone < 60:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= alone < 61:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 61 <= alone < 62:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 62 <= alone < 63:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 63 <= alone < 64:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 64 <= alone < 65:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 65 <= alone < 66:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 66 <= alone < 67:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 67 <= alone < 68:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 68 <= alone < 69:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 69 <= alone < 70:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 70 <= alone < 71:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 71 <= alone < 72:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 72 <= alone < 73:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 73 <= alone < 74:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 74 <= alone < 75:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 75 <= alone < 76:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 76 <= alone < 77:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 77 <= alone < 78:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 78 <= alone < 79:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 79 <= alone < 80:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 80 <= alone < 81:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 81 <= alone < 82:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 82 <= alone < 83:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 83 <= alone < 84:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 84 <= alone < 85:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 85 <= alone < 86:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 86 <= alone < 87:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 87 <= alone < 88:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 88 <= alone < 89:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 89 <= alone < 90:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 90 <= alone < 91:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 91 <= alone < 92:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 92 <= alone < 93:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 93 <= alone < 94:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 94 <= alone < 95:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 95 <= alone < 96:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 96 <= alone < 97:
        ba = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 97 <= alone < 98:
        ba = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 98 <= alone < 99:
        ba = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    else:
        ba = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
        
        buttons  = [

        [

            InlineKeyboardButton(
                text=f"{played} {ba} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text="▷",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="II", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▢", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons
    
def stream_markup(_, videoid, chat_id):

    buttons  = [   

            [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text="▷",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="II", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▢", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons

def telegram_markup(_, chat_id):
    buttons  = [   
        
            [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),
            
            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],
    ]

    return buttons
## Search Query Inline

def track_markup(_, videoid, user_id, channel, fplay):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text=_["P_B_1"],

                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["P_B_2"],

                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons
## Live Stream Markup

def livestream_markup(_, videoid, user_id, mode, channel, fplay):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text=_["P_B_3"],

                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text=_["CLOSEMENU_BUTTON"],

                callback_data=f"forceclose {videoid}|{user_id}",

            ),

        ]

    ]

    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text=_["P_B_1"],

                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["P_B_2"],

                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text=_["CLOSE_BUTTON"],

                callback_data=f"forceclose {videoid}|{user_id}",

            ),

        ],

    ]

    return buttons
## Slider Query Markup

def slider_markup(

    _, videoid, user_id, query, query_type, channel, fplay

):

    query = f"{query[:20]}"

    buttons = [
        [
           InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),

          ],
          [
          
            InlineKeyboardButton(

                text=_["P_B_1"],

                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["P_B_2"],

                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="◁",

                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["CLOSE_BUTTON"],

                callback_data=f"forceclose {query}|{user_id}",

            ),

            InlineKeyboardButton(

                text="▷",

                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",

            ),

        ],

    ]

    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 

            [

                [

                    InlineKeyboardButton(

                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"

                    )

                ]    

            ]

        )

## Queue Markup

def queue_markup(_, videoid, chat_id):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text="▷",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="II", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▢", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [  

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons
