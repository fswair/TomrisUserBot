import os
from typing import TypeAlias
from utils import on_start
from pyrogram import Client, filters, enums
from pyrogram.types import Message, User

if os.path.isfile("__pycache__"):
    os.remove("__pycache__")

client: TypeAlias = Client


@client.on_message(on_start)
async def start_message(client: Client, message: Message):
    if len(message.command) > 1:
        return await message.reply(
            f"Hello, arguments: {', '.join(message.command[1:])}", quote=True
        )
    return await message.reply(f"Hello, I'm {message.from_user.mention}", quote=True)
