## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBQd_nK8uHIrQ17Y27Do25d3rfFqUGvlMaLLEn8kyRnJheGV9BPSwuk_2srNKJz7nrjG3OSvw6jom-MkV3Qw6bvCdnZT2uEv5W5CSknIMIAgzUzrxi8yz1IHL24etus_nO_pO7xfG7cs-V-cEJOBlonLwYpRTlLOozh9VEVG8PAw-fqwr8vshB3JgSAqOHyRzwnbYoa7RXQd36ewxzYeLDm3w2DQ4LIXFOoWsA3uT8WDJahOnvqf4RRtw3mATt9WsayG0VJPmk-Swm-2iAfmqsr8N410VHnxqeQJJjkRcYa82zW77g6LL09iSeRUKl_KprDU4IQV4VYtXFbi-FE0Fn2AAAAATWBwr8A")
BOT_TOKEN = getenv("BOT_TOKEN", "5378258065:AAElEoMEsuSUDkob8O6NJg9Tk3m8GLskO7g")
BOT_NAME = getenv("BOT_NAME", "SkyMusic")
API_ID = int(getenv("API_ID", "17439903"))
API_HASH = getenv("API_HASH", "425417934536df57eab80d387a46db61")
OWNER_NAME = getenv("OWNER_NAME", "Sky")
OWNER_USERNAME = getenv("OWNER_USERNAME", "SkyNinja6T9")
ALIVE_NAME = getenv("ALIVE_NAME", "Sky")
BOT_USERNAME = getenv("BOT_USERNAME", "SkyMusicVCBot")
OWNER_ID = getenv("OWNER_ID", "1437890445")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SkyMusicAssist")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ChattingArea")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Professor_Zero_Channel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5192663743").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/b36e913bd7e38b0596bbc.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/f8871e5c3d0d1841a6b1f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SkyNinja6T9/SkyVCVC")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
