from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# uh... baka
class Facepalm(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='facepalm')
    async def facepalm(self, ctx):
        await ctx.message.delete()
        await ctx.send(embed=Embed(description=f"(－‸ლ) {ctx.message.author.name}",
                                   color=0x2F3136)
                       .set_image(url=await get_random_gif_by_theme("anime facepalm")))


def setup(bot):
    bot.add_cog(Facepalm(bot))
