# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "VideoMergeDcBot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 4))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 10))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1940030638))

    START_TEXT = """
Oii 🦊, I am Video Merge Bot!

I can Merge Multiple Videos in One Video. Video Formats should be same.

Made by @GroupDcBots
"""
    CAPTION = "Video Merged by @{}\n\nMade by @GroupDcBots"
    PROGRESS = """
⚜️ Percentage : {0}%
✅ Done: {1}
🔱 Total: {2}
💠 Speed: {3}/s
🔹 ETA: {4}
"""
