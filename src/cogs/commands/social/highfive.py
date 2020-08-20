from discord import User
from discord.ext.commands import MissingRequiredArgument, BadArgument

from discord import Embed
from discord.ext import commands

from modules.random import get_random_gif_by_theme


# Yay, we did it !
from utils import safe_delete


class HighFive(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='highfive', aliases=['high5', 'h5'])
    async def highfive(self, ctx, target: User):
        await safe_delete(ctx)
        if ctx.message.author != target:
            await ctx.send(embed=Embed(description=f"(._.)/(._. **{ctx.author.name}** highfives **{target.name}**",
                                       color=0x2F3136)
                           .set_image(url=f"{await get_random_gif_by_theme('anime highfive')}"))
        else: await ctx.send("You really want to do this alone-.. ?", delete_after=5.0)

    @highfive.error
    async def highfive_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify someone to highfive with, it would be so sad otherwise ! 😢", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that member...", delete_after=5.0)


def setup(bot):
    bot.add_cog(HighFive(bot))
