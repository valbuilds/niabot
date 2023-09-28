import discord
from discord import app_commands
import json
import util
from typing import Optional

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
        
    @app_commands.command()
    async def announce(self, interaction: discord.Interaction, channel: discord.TextChannel, announcement: str, link1: Optional[str], link2: Optional[str], link3: Optional[str], link4: Optional[str], link5: Optional[str]):
        e = discord.Embed(title="Announcement", description=announcement, colour=discord.Color.blurple())
        v = discord.ui.View()
        e.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        l = []
        if link1 is not None:
            linkone = util.Strings.findurl(url=link1)
            if linkone is not None:
                l.append(discord.ui.Button(style=discord.ButtonStyle.url, label=linkone[0][:80], url=linkone[0]))
        if link2 is not None:
            linktwo = util.Strings.findurl(url=link2)
            if linktwo is not None:
                l.append(discord.ui.Button(style=discord.ButtonStyle.url, label=linktwo[0][:80], url=linktwo[0]))
        if link3 is not None:
            linkthree = util.Strings.findurl(url=link3)
            if linkthree is not None:
                l.append(discord.ui.Button(style=discord.ButtonStyle.url, label=linkthree[0][:80], url=linkthree[0]))
        if link4 is not None:
            linkfour = util.Strings.findurl(url=link4)
            if linkfour is not None:
                l.append(discord.ui.Button(style=discord.ButtonStyle.url, label=linkfour[0][:80], url=linkfour[0]))
        if link5 is not None:
            linkfive = util.Strings.findurl(url=link5)
            if linkfive is not None:
                l.append(discord.ui.Button(style=discord.ButtonStyle.url, label=linkfive[0][:80], url=linkfive[0]))

        for button in l:
            v.add_item(button)

        if interaction.user.guild_permissions.manage_channels is True:
            await channel.send(embed=e, view=v)
            await interaction.response.send_message(content="Announcement sent!", ephemeral=True)
        else:
            return interaction.response.send_message(content="You don't have the permissons to send an announcement!", ephemeral=True)

async def setup(bot):
    bot.tree.add_command(Embeds(name="embed", description="Embed commands"))
    print("commands.embeds is ready!")