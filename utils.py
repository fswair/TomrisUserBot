import json
from pyrogram import Client, filters


class TelegramClient:
    def __new__(cls, config_path: str = "./configure/tomris-config.json") -> Client:
        with open(config_path, "r", encoding="utf8") as config:
            cls.data: dict = json.loads(config.read())
        return Client(**cls.data)


class Filters:
    ON_START = filters.me & filters.command("start")


on_start = Filters.ON_START
