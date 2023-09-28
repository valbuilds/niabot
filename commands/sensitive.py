import discord
from discord import app_commands
import settings


class Sensitive(app_commands.Group):
    @app_commands.command()
    async def anon(self, interaction: discord.Interaction, channel: discord.TextChannel, input: str):
        logchat = interaction.guild.get_channel(settings.CONFIG['bot']['logs_channel'])
        e = discord.Embed(title="Anonymous Post", description=input[:2048], color=discord.Colour.dark_gray())
        le = discord.Embed(title="Anonymous Post sent", description=input[:2048], color=discord.Colour.dark_gray())
        le.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        le.set_footer(text="Warning: Sharing a screenshot or simillar of this embed will result in demotion.")
        await logchat.send(embed=le)
        await interaction.channel.send(embed=e)
        return await interaction.response.send_message(embed=le, ephemeral=True)
