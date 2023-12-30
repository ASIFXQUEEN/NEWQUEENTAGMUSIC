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
        photo=f"https://telegra.ph/file/a290c80a784cbe54976cc.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹Asif Cᴏᴅᴇʀ🌹", url=f"https//t.me/ASHIF903")
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
        photo=f"https://telegra.ph/file/a290c80a784cbe54976cc.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹Asif Cᴏᴅᴇʀ🌹", url=f"https//t.me/ASHIF903")
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
        photo=f"https://telegra.ph/file/a290c80a784cbe54976cc.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ɴᴀᴠᴇɴ Qᴜᴇᴇɴ•", url=f"https://telegra.ph/file/905187379436190cf1725.jpg"
                    ),
                    InlineKeyboardButton(
                        "•ᴀꜱɪꜰ Qᴜᴇᴇɴ•", url=f"https://telegra.ph/file/905187379436190cf1725.jpg"
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
        photo=f"https://telegra.ph/file/a290c80a784cbe54976cc.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ɴᴀᴠᴇɴ Qᴜᴇᴇɴ•", url=f"https://telegra.ph/file/905187379436190cf1725.jpg"
                    ),
                    InlineKeyboardButton(
                        "•ᴀꜱɪꜰ Qᴜᴇᴇɴ•", url=f"https://telegra.ph/file/905187379436190cf1725.jpg"
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
        photo=f"https://telegra.ph/file/a290c80a784cbe54976cc.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ɴᴀᴠᴇɴ Qᴜᴇᴇɴ•", url=f"https://telegra.ph/file/905187379436190cf1725.jpg"
                    ),
                    InlineKeyboardButton(
                        "•ᴀꜱɪꜰ Qᴜᴇᴇɴ•", url=f"https://telegra.ph/file/905187379436190cf1725.jpg"
                    ),
                ]
            ]
        ),
    )
