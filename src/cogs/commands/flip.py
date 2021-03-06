import discord
from discord.ext import commands
from random import choice


# Heads or Tails !
from utils import safe_delete


class Flip(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='flip', aliases=['coinflip', 'headsortails', 'piece'])
    async def flip(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=discord.Embed(color=0x2F3136,
                                           description=f"`{choice(['Heads', 'Tails'])}`"))


def setup(bot):
    bot.add_cog(Flip(bot))
