import discord
import settings
from discord.ext import commands
from discord import app_commands
import aiohttp

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
    
    @bot.tree.context_menu(name="Reblog")
    async def reblog(interaction: discord.Interaction, message: discord.Message):
        print("interaction received")
        await interaction.response.send_message(content="One second...", ephemeral=True)
        print("interaction response created!")
        w = await message.channel.create_webhook(name=interaction.user.display_name, avatar=await interaction.user.display_avatar.read())
        print("webhok made")
        async with aiohttp.ClientSession() as session:
            print("webhook connected")
            webhook = discord.Webhook.from_url(w.url, session=session)
            await webhook.send(content=message.content, files=message.attachments, embeds=message.embeds, allowed_mentions=None)
            print("message sent")
        await w.delete()
        print("webhook deleted")


    bot.run(settings.TOKEN)


if __name__ == "__main__":
    run()