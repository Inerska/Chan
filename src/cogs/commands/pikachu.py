from discord import Embed
from discord.ext import commands

from src.modules.random import get_link_from_API


# We need some pika pika in our lives
class Pikachu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pikachu', aliases=['pika'])
    async def pikachu(self, ctx):
        await ctx.message.delete()
        await ctx.send(embed=Embed(description="⊹　 ✺ * ·　Pika~ Pika~..",
                                   color=0x2F3136)
                       .set_image(url=await get_link_from_API('https://some-random-api.ml/img/pikachu')))


def setup(bot):
    bot.add_cog(Pikachu(bot))
