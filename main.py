import discord
import settings
from discord.ext import commands

def run():
    bot = commands.Bot(command_prefix=settings.CONFIG['bot']['prefix'], intents=discord.Intents.all(), activity=settings.ACTIVITY, status=settings.STATUS)
    
    @bot.event
    async def on_connect():
        print("A quick warning: Slash commands may not be synced! Everytime slash commands are modified, you have to run " + '"' + settings.CONFIG['bot']['prefix'] + 'synccommands".')
    
    @bot.event
    async def on_ready():
        await bot.load_extension("commands.embeds")
        print("The bot is now online!")

    @bot.command()
    @commands.is_owner()
    async def synccommands(ctx: commands.Context):
        r = await ctx.reply(content="Syncing...")
        await bot.tree.sync()
        await r.edit(content="Synced!")

    bot.run(settings.TOKEN)


if __name__ == "__main__":
    run()