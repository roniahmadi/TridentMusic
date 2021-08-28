import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Trident Music")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/ce8642a2ab1d0cb0cfcad.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/a025fc507fb2255d950ea.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/a025fc507fb2255d950ea.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b737f6fd7d8e605cd62c5.png")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "LgMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TridentMusicAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "GroupTrident")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ChannelTrident")
OWNER_NAME = getenv("OWNER_NAME", "feryferlX") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "feryferlX")
PMPERMIT = getenv("PMPERMIT", "ENABLE")

OWNER_ID = int(os.environ.get("OWNER_ID","1796487585")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://botmusik:feryferl123@cluster0.abjkq.mongodb.net/cluster0?retryWrites=true&w=majority") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001523077492")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . :").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
