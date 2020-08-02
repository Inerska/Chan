from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_joke_text


# Add some spicy in our lives
from src.utils import safe_delete


class Joke(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='joke')
    async def joke(self, ctx):
        await safe_delete(ctx)
        q, a = await get_random_joke_text()
        await ctx.send(embed=Embed(title="⊹　 ✺ * ·　",
                                   color=0x2F3136,
                                   description=f"{q}\n— {a}"))


def setup(bot):
    bot.add_cog(Joke(bot))
