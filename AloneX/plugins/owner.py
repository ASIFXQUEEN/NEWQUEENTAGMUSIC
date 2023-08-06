from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AloneX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("coder")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹Aʟᴏɴᴇ Cᴏᴅᴇʀ🌹", url=f"https://t.me/ALONE_WAS_BOT")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("coder")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹Aʟᴏɴᴇ Cᴏᴅᴇʀ🌹", url=f"https://t.me/ALONE_WAS_BOT")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ᴀʟᴏɴᴇ ᴍᴜꜱɪᴄ•", url="https://github.com/TeamAloneOp/AloneX/fork"
                    ),
                    InlineKeyboardButton(
                        "•ᴀʟᴏɴᴇ ʀᴏʙᴏᴛ•", url="https://github.com/TeamAloneOp/AloneRobot/fork"
                    ),
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ᴀʟᴏɴᴇ ᴍᴜꜱɪᴄ•", url="https://github.com/TeamAloneOp/AloneX/fork"
                    ),
                    InlineKeyboardButton(
                        "•ᴀʟᴏɴᴇ ʀᴏʙᴏᴛ•", url="https://github.com/TeamAloneOp/AloneRobot/fork"
                    ),
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ᴀʟᴏɴᴇ ᴍᴜꜱɪᴄ•", url="https://github.com/TeamAloneOp/AloneX/fork"
                    ),
                    InlineKeyboardButton(
                        "•ᴀʟᴏɴᴇ ʀᴏʙᴏᴛ•", url="https://github.com/TeamAloneOp/AloneRobot/fork"
                    ),
                ]
            ]
        ),
    )

