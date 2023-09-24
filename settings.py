import os
from dotenv import load_dotenv
load_dotenv()
import json
import discord

TOKEN: str = os.getenv('token')

cfile = open('config.json')
CONFIG = json.load(cfile)

ACTIVITY = None
if CONFIG['bot']['status']['activity']['type'] == 0 or CONFIG['bot']['status']['activity']['type'].lower() == "playing":
    ACTIVITY = discord.Game(name=CONFIG['bot']['status']['activity']['name'])
elif CONFIG['bot']['status']['activity']['type'] == 1 or CONFIG['bot']['status']['activity']['type'].lower() == "streaming":
    ACTIVITY = discord.Streaming(name=CONFIG['bot']['status']['activity']['name'])
elif CONFIG['bot']['status']['activity']['type'] == 2 or CONFIG['bot']['status']['activity']['type'].lower() == "listening":
    ACTIVITY = discord.Activity(type=discord.ActivityType.listening, name=CONFIG['bot']['status']['activity']['name'])
elif CONFIG['bot']['status']['activity']['type'] == 3 or CONFIG['bot']['status']['activity']['type'].lower() == "watching":
    ACTIVITY = discord.Activity(type=discord.ActivityType.watching, name=CONFIG['bot']['status']['activity']['name'])
elif CONFIG['bot']['status']['activity']['type'] == 4 or CONFIG['bot']['status']['activity']['type'].lower() == "custom":
    ACTIVITY = discord.CustomActivity(name=CONFIG['bot']['status']['activity']['name'])

STATUS = discord.Status.online
if CONFIG['bot']['status']['type'] == 0 or CONFIG['bot']['status']['type'] == "online":
    STATUS = discord.Status.online
elif CONFIG['bot']['status']['type'] == 1 or CONFIG['bot']['status']['type'] == "idle":
    STATUS = discord.Status.idle
elif CONFIG['bot']['status']['type'] == 2 or CONFIG['bot']['status']['type'] == "dnd":
    STATUS = discord.Status.dnd
elif CONFIG['bot']['status']['type'] == 3 or CONFIG['bot']['status']['type'] == "invisible":
    STATUS = discord.Status.invisible