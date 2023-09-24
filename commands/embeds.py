import discord
from discord import app_commands
from typing import Optional
import settings

class Embeds(app_commands.Group):
    @app_commands.command(description="Make a custom embed.")
    async def make(self, interaction: discord.Interaction, title: str, description: Optional[str], field1_name: Optional[str], field1_value: Optional[str], field2_name: Optional[str], field2_value: Optional[str], field3_name: Optional[str], field3_value: Optional[str], field4_name: Optional[str], field4_value: Optional[str], field5_name: Optional[str], field5_value: Optional[str], inlinefields: Optional[bool] = True):
        embed = discord.Embed(color=discord.Color.blurple())
        embed.title = title
        embed.description = description
        if field1_name is not None and field1_value is not None:
            embed.add_field(name=field1_name, value=field1_value, inline=inlinefields)
        if field2_name is not None and field2_value is not None:
            embed.add_field(name=field2_name, value=field2_value, inline=inlinefields)
        if field3_name is not None and field3_value is not None:
            embed.add_field(name=field3_name, value=field3_value, inline=inlinefields)
        if field4_name is not None and field4_value is not None:
            embed.add_field(name=field4_name, value=field4_value, inline=inlinefields)
        if field5_name is not None and field5_value is not None:
            embed.add_field(name=field5_name, value=field5_value, inline=inlinefields)
        
        return await interaction.response.send_message(embed=embed)
    
    @app_commands.command(description="Send a pre-made embed!")
    async def send_premade(self, interaction: discord.Interaction, premadeid: str):
        a = settings.CONFIG['embeds'][premadeid]
        embed = discord.Embed()
        if a['title'] is not None:
            embed.title = a['title']
        if a['description'] is not None:
            embed.description = a['description']
        if a['color'] is not None:
            embed.color = discord.Color.from_str(a['color'])
        elif a['color'] is None:
            embed.color = discord.Colour.blurple()

        return await interaction.response.send_message(embed=embed)

async def setup(bot):
    bot.tree.add_command(Embeds(name="embed", description="Embed commands (version 0.0.1a)"))
    print("commands.embeds is ready!")