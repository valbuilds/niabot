import os
from dotenv import load_dotenv
load_dotenv()
import json
import discord

TOKEN: str = os.getenv('token')

cfile = open('config/config.json')
CONFIG = json.load(cfile)

ACTIVITY = discord.Activity(type=discord.ActivityType.listening, name=f"{CONFIG['bot']['prefix']}help")
if CONFIG['bot']['status']['activity']['type'] == "playing":
    ACTIVITY = discord.Activity(type=discord.ActivityType.playing, name=f"{CONFIG['bot']['status']['activity']['name']}")
elif CONFIG['bot']['status']['activity']['type'] == "streaming":
    ACTIVITY = discord.Activity(type=discord.ActivityType.streaming, name=f"{CONFIG['bot']['status']['activity']['name']}")
elif CONFIG['bot']['status']['activity']['type'] == "listening":
    ACTIVITY = discord.Activity(type=discord.ActivityType.listening, name=f"{CONFIG['bot']['status']['activity']['name']}")
elif CONFIG['bot']['status']['activity']['type'] == "watching":
    ACTIVITY = discord.Activity(type=discord.ActivityType.watching, name=f"{CONFIG['bot']['status']['activity']['name']}")
elif CONFIG['bot']['status']['activity']['type'] == "custom":
    ACTIVITY = discord.Activity(type=discord.ActivityType.custom, name=f"{CONFIG['bot']['status']['activity']['name']}")
elif CONFIG['bot']['status']['activity']['type'] == "competing":
    ACTIVITY = discord.Activity(type=discord.ActivityType.competing, name=f"{CONFIG['bot']['status']['activity']['name']}")

STATUS = discord.Status.online
if CONFIG['bot']['status']['type'] == "online":
    STATUS = discord.Status.online
elif CONFIG['bot']['status']['type'] == "idle":
    STATUS = discord.Status.idle
elif CONFIG['bot']['status']['type'] == "dnd":
    STATUS = discord.Status.dnd
elif CONFIG['bot']['status']['type'] == "do not disturb":
    STATUS = discord.Status.do_not_disturb
elif CONFIG['bot']['status']['type'] == "invisible":
    STATUS = discord.Status.invisible