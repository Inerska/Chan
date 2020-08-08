from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_anime_quote
from random import choice


# Wow... that was so motivating
from src.utils import safe_delete


class AnimeQuote(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='animequote', aliases=["aq"])
    async def animequote(self, ctx):
        await safe_delete(ctx)
        q, c, a = await get_random_anime_quote()
        await ctx.send(embed=Embed(title="⊹　 ✺ * ·　",
                                   color=0x2F3136,
                                   description=f"« {q} »\n— {c} - {a}"))


def setup(bot):
    bot.add_cog(AnimeQuote(bot))
