from discord import Embed
from discord.ext import commands

from modules.random import get_random_gif_by_theme


# Hehe.. :3
from utils import safe_delete


class Smug(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='smug')
    async def smug(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=Embed(description=f"¬‿¬ **{ctx.author.name}** is preparing something- ",
                                   color=0x2F3136)
                       .set_image(url=f"{await get_random_gif_by_theme('anime smug')}"))


def setup(bot):
    bot.add_cog(Smug(bot))
