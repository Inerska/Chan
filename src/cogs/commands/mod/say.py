import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument, BadArgument
from random import randint


# Say something as admin
from src.utils import safe_delete


class Say(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='say')
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, msg: str):
        await safe_delete(ctx)
        await ctx.send(msg)

    @say.error
    async def say_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify a message to say ! 😢", delete_after=5.0)


def setup(bot):
    bot.add_cog(Say(bot))
