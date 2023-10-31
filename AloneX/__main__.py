import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AloneX import LOGGER, app, userbot
from AloneX.core.call import Alone
from AloneX.plugins import ALL_MODULES
from AloneX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("AloneX").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("AloneX").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AloneX.plugins." + all_module)
    LOGGER("AloneX.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Alone.start()
    try:
        await Alone.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("AloneX").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Alone.decorators()
    LOGGER("AloneX").info("\x41\x6C\x6F\x6E\x65\x58\x20\x4D\x75\x73\x69\x63\x20\x42\x6F\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6C\x6C\x79")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AloneX").info("Stopping Music Bot...")
