import aiohttp
from discord.ext.commands import MissingRequiredArgument, BadArgument, MissingPermissions, BotMissingPermissions
from discord.ext import commands
from src.modules.random import get_random_gif_by_theme
from src.utils import empty_char, safe_delete, fetch
from discord import Embed, Member
from datetime import date


async def get_answer(question: str):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session,
                               f"https://8ball.delegator.com/magic/JSON/{question}")
        await session.close()
        return response["magic"]["answer"]


# Answer my question Chan!
class heighBall(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball', aliases=["8b"])
    async def hball(self, ctx, *, question: str):
        await safe_delete(ctx)
        await ctx.send(f"{ctx.message.author.mention}, {await get_answer(question)} !")

    @hball.error
    async def hball_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, MissingRequiredArgument) or isinstance(error, BadArgument):
            await ctx.send("Please specify a question !", delete_after=5.0)


def setup(bot):
    bot.add_cog(heighBall(bot))
