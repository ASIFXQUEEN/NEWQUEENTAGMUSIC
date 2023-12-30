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
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://radare.arzfun.com/api/tg/photo?id=AgACAgUAAxkBAAICu2V05I5iyqVwodWNdGz7LKFICcsvAAKiwTEbbu2oVytQ0lbYIWZ4AQADAgADeAADMwQ",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹ASIF🌹", url=f"https//t.me/ASHIF903")
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
        photo=f"https://radare.arzfun.com/api/tg/photo?id=AgACAgUAAxkBAAICu2V05I5iyqVwodWNdGz7LKFICcsvAAKiwTEbbu2oVytQ0lbYIWZ4AQADAgADeAADMwQ",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹XQUEENSERVER🌹", url=f"https//t.me/ASHIF903")
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
        photo=f"https://radare.arzfun.com/api/tg/photo?id=AgACAgUAAxkBAAICu2V05I5iyqVwodWNdGz7LKFICcsvAAKiwTEbbu2oVytQ0lbYIWZ4AQADAgADeAADMwQ",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•NAVEEN MUSIC•", url=f"https//t.me/ASHIF903"
                    ),
                    InlineKeyboardButton(
                        "•ASIFXQUEEN•", url=f"https//t.me/ASHIF903"
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
        photo=f"https://radare.arzfun.com/api/tg/photo?id=AgACAgUAAxkBAAICu2V05I5iyqVwodWNdGz7LKFICcsvAAKiwTEbbu2oVytQ0lbYIWZ4AQADAgADeAADMwQ",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•MAVEEN MUSIC•", url=f"https//t.me/ASHIF903"
                    ),
                    InlineKeyboardButton(
                        "•ASIFXQUEEN•", url=f"https//t.me/ASHIF903"
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
        photo=f"https://radare.arzfun.com/api/tg/photo?id=AgACAgUAAxkBAAICu2V05I5iyqVwodWNdGz7LKFICcsvAAKiwTEbbu2oVytQ0lbYIWZ4AQADAgADeAADMwQ",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•NAVEEN MUSIC•", url=f"https//t.me/ASHIF903"
                    ),
                    InlineKeyboardButton(
                        "•ASIFXQUEEN•", url=f"https//t.me/ASHIF903"
                    ),
                ]
            ]
        ),
    )

