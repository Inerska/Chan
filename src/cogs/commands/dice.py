import discord
from discord.ext import commands
from random import randint


# Please 6
class Dice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dice')
    async def dice(self, ctx):
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(color=0x2F3136,
                                           description=f"🎲 You roll a `{randint(1, 6)}` !"))


def setup(bot):
    bot.add_cog(Dice(bot))
