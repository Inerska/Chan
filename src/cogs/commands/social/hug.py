from discord import User
from discord.ext.commands import MissingRequiredArgument, BadArgument

from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# Sometimes, a hug can be the solution
class Hug(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hug')
    async def hug(self, ctx, target: User):
        await ctx.message.delete()
        await ctx.send(embed=Embed(description=f"༼ つ ◕o◕ ༽つ **{ctx.author.name}** hugs **{target.name}**",
                                   color=0x2F3136)
                       .set_image(url=f"{await get_random_gif_by_theme('anime hug')}"))

    @hug.error
    async def hug_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify someone to hug on, it would be so sad otherwise ! 😢", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that member...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Hug(bot))
