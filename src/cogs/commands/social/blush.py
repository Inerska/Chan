from discord import Embed
from discord.ext import commands

from modules.random import get_random_gif_by_theme


# Senpai..~~
from utils import safe_delete


class Blush(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='blush', aliases=["shy"])
    async def blush(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=Embed(description=f">//< **{ctx.author.name}** blushes !",
                                   color=0x2F3136)
                       .set_image(url=f"{await get_random_gif_by_theme('anime blush')}"))


def setup(bot):
    bot.add_cog(Blush(bot))
