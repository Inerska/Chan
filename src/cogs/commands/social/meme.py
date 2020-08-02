from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme, get_random_meme_pic
from random import choice


# Add some spicy in our lives
from src.utils import safe_delete


class Meme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='meme')
    async def meme(self, ctx):
        await safe_delete(ctx)
        meme = choice([True, False])
        await ctx.send(embed=Embed(description="⊹　 ✺ * ·　",
                                   color=0x2F3136)
                       .set_image(url=await get_random_gif_by_theme('meme') if meme else await get_random_meme_pic()))


def setup(bot):
    bot.add_cog(Meme(bot))
