from discord import User
from discord.ext.commands import MissingRequiredArgument, BadArgument

from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# Yeah, that's sad...
class Cry(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cry')
    async def cry(self, ctx):
        await ctx.message.delete()
        await ctx.send(embed=Embed(description=f"｡:ﾟ(;´∩`;)ﾟ:｡ **{ctx.author.name}** cries...",
                                   color=0x2F3136)
                       .set_image(url=f"{await get_random_gif_by_theme('anime cry')}"))


def setup(bot):
    bot.add_cog(Cry(bot))
