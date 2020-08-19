from discord import Embed
from discord.ext import commands

from modules.random import get_random_gif_by_theme


# Yeah, that's sad...
from src.utils import safe_delete


class Cry(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cry')
    async def cry(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=Embed(description=f"｡:ﾟ(;´∩`;)ﾟ:｡ **{ctx.author.name}** cries...",
                                   color=0x2F3136)
                       .set_image(url=f"{await get_random_gif_by_theme('anime cry')}"))


def setup(bot):
    bot.add_cog(Cry(bot))
