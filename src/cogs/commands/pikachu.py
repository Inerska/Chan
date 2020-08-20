from discord import Embed
from discord.ext import commands

from modules.random import get_link_from_API


# We need some pika pika in our lives
from utils import safe_delete


class Pikachu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pikachu', aliases=['pika'])
    async def pikachu(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=Embed(description="⊹　 ✺ * ·　Pika~ Pika~..",
                                   color=0x2F3136)
                       .set_image(url=await get_link_from_API('https://some-random-api.ml/img/pikachu')))


def setup(bot):
    bot.add_cog(Pikachu(bot))
