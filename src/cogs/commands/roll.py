import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument, BadArgument
from random import randint


# Please an odd number
class Roll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll')
    async def roll(self, ctx, max_value: int):
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(color=0x2F3136,
                                           description=f"You have rolled a `{randint(1, max_value)}` !"))

    @roll.error
    async def roll_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify a max value to roll ! 😢", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- but you have only to put a number (%roll 10)", delete_after=5.0)


def setup(bot):
    bot.add_cog(Roll(bot))
