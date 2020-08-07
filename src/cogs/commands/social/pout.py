from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# (￣ε(#￣)
from src.utils import safe_delete


class Pout(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pout')
    async def pout(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=Embed(description=f"(￣ε(#￣) **{ctx.author.name}** pouts !",
                                   color=0x2F3136)
                       .set_image(url=f"{await get_random_gif_by_theme('anime pout')}"))


def setup(bot):
    bot.add_cog(Pout(bot))
