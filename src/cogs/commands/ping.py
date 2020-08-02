import discord
from discord.ext import commands


# Does Chan has latency ?
from src.utils import safe_delete


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', aliases=['ms', 'latency', 'lag'])
    async def ping(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=discord.Embed(color=0x2F3136,
                                           description=f"Chan's ping is `{int(self.bot.latency * 1000)} ms` !"))


def setup(bot):
    bot.add_cog(Ping(bot))
