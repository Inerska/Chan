from discord import Embed
from discord.ext import commands

from modules.random import get_random_gif_by_theme


# uh... baka
from utils import safe_delete


class Facepalm(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='facepalm')
    async def facepalm(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=Embed(description=f"(－‸ლ) {ctx.message.author.name}",
                                   color=0x2F3136)
                       .set_image(url=await get_random_gif_by_theme("anime facepalm")))


def setup(bot):
    bot.add_cog(Facepalm(bot))
