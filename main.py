import discord
import settings
from discord.ext import commands

def run():
    bot = commands.Bot(command_prefix=settings.Config.prefix, intents=discord.Intents.all(), activity=settings.Status.a, status=settings.Status.s)
    
    @bot.event
    async def on_connect():
        print("A quick warning: Slash commands may not be synced! Everytime slash commands are modified, you have to run " + '"' + settings.Config.prefix + 'synccommands".')
    
    @bot.event
    async def on_ready():
        await bot.load_extension("commands.embeds")
        await bot.load_extension("commands.sensitive")
        await bot.load_extension("events.topictags")
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