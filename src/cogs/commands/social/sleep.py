from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# I wanna sleep a lil bit...
from src.utils import safe_delete


class Sleep(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sleep')
    async def sleep(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=Embed(description=f"[(－－)]..zzZ **{ctx.author.name}** is sleeping...",
                                   color=0x2F3136)
                       .set_image(url=f"{await get_random_gif_by_theme('anime sleeping')}"))


def setup(bot):
    bot.add_cog(Sleep(bot))
