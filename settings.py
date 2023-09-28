import os
from dotenv import load_dotenv
load_dotenv()
import json
import discord

TOKEN: str = os.getenv('token')

class Config:
    f = open('config/config.json')
    json = json.load(f)

    prefix: str = json['bot']['prefix']
    logchannel: int = json['bot']['channels']['log']

    activityType: str = json['bot']['status']['activity']['type'].lower()
    rawActivityType: str = json['bot']['status']['activity']['type']
    activityName: str = json['bot']['status']['activity']['name'].lower()
    rawActivityName: str = json['bot']['status']['activity']['name']
    status: str = json['bot']['status']['type'].lower()
    rawStatus: str = json['bot']['status']['type']

# DEPRECATED: Use Config class above.
cfile = open('config/config.json')
# DEPRECATED: Use Config class above.
CONFIG = json.load(cfile)

class Status:
    a = discord.Activity(type=discord.ActivityType.listening, name=f"{Config.prefix}help")

    if Config.activityType == "playing":
        a.type = discord.ActivityType.playing
        a.name = Config.activityName
    elif Config.activityType == "streaming":
        a.type = discord.ActivityType.streaming
        a.name = Config.activityName
    elif Config.activityType == "listening":
        a.type = discord.ActivityType.listening
        a.name = Config.activityName
    elif Config.activityType == "watching":
        a.type = discord.ActivityType.watching
        a.name = Config.activityName
    elif Config.activityType == "custom":
        a.type = discord.ActivityType.custom
        a.name = Config.activityName
    elif Config.activityType == "competing":
        a.type = discord.ActivityType.competing
        a.name = Config.activityName

    s = discord.Status.online

    if Config.status == "online":
        s = discord.Status.online
    elif Config.status == "idle":
        s = discord.Status.idle
    elif Config.status == "dnd" or Config.status == "do not disturb":
        s = discord.Status.dnd
    elif Config.status == "invisible":
        s = discord.Status.invisible