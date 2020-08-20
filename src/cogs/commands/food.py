from discord import Embed
from discord.ext import commands

from modules.random import get_random_gif_by_theme, get_random_meme_pic
from random import choice


# I'm hungry !
from utils import safe_delete


class Food(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='food', aliases=['foods', 'foodporn'])
    async def food(self, ctx):
        await safe_delete(ctx)
        meme = choice([True, False])
        await ctx.send(embed=Embed(description="웃┏♨❤♨┑유",
                                   color=0x2F3136)
                       .set_image(url=await get_random_gif_by_theme('food')))


def setup(bot):
    bot.add_cog(Food(bot))
