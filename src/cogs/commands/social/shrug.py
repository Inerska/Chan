from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# /shrug
from src.utils import safe_delete


class Shrug(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='shrug')
    async def shrug(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=Embed(description=f"¯\_( ツ )_/¯ **{ctx.author.name}** shrugs",
                                   color=0x2F3136)
                       .set_image(url=f"{await get_random_gif_by_theme('anime shrug')}"))


def setup(bot):
    bot.add_cog(Shrug(bot))
