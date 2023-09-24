import discord
from discord import app_commands
import json

class Embeds(app_commands.Group):
    @app_commands.command()
    async def send(self, interaction: discord.Interaction, id: str):
        f = open(f'./config/messages/{id}.json')
        data = json.load(f)

        e = []
        for embed in data['embeds']:
            e.append(discord.Embed.from_dict(embed))

        if interaction.user.guild_permissions.mention_everyone is True:
            await interaction.response.send_message(content=data['content'], embeds=e, allowed_mentions=discord.AllowedMentions.all())
        else:
            await interaction.response.send_message(content=data['content'], embeds=e, allowed_mentions=discord.AllowedMentions.none())

async def setup(bot):
    bot.tree.add_command(Embeds(name="embed", description="Embed commands (version 0.0.1a)"))
    print("commands.embeds is ready!")