import discord
from discord.ext import commands


class TopicTags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    topictags = []

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # uping
        # [--uping:123456789,123456789]
        # 1 per channel
        # -------
        # takes 2 inputs
        # user id: discord user id - the user id that this ping corresponds to
        # ping id: discord role id - the role id that this ping corresponds to
        # -------
        uping_disallowedtypes = [discord.ChannelType.news_thread, discord.ChannelType.public_thread, discord.ChannelType.private_thread]
        if message.channel.type not in uping_disallowedtypes:
            if "[--uping:" in message.channel.topic:
                    p = message.channel.topic.split("[")[1].split("]")[0].split(":")[1].split(",")
                    uid = int(p[0])
                    rid = int(p[1])
                    if message.author.id == uid:
                        if "||PING||" in message.content:
                            await message.reply(content=f"> <@&{rid}>")
                        if "||PUBLISH||" in message.content:
                            if message.channel.type == discord.ChannelType.news:
                                try: await message.publish()
                                except discord.HTTPException as exc:
                                    emb = discord.Embed(title="An HTTP Exception occured while publishing!", description=f"```\n{exc.text}\n```", colour=discord.Color.red())
                                    emb.set_footer(text=f"discord.HTTPException: Error code {exc.code}")
                                    await message.reply(embed=emb)


async def setup(bot):
    await bot.add_cog(TopicTags(bot))
    print("events.topictags is ready!")