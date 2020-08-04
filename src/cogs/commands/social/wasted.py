from discord import User
from discord.ext.commands import MissingRequiredArgument, BadArgument

from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# uh...
from src.utils import safe_delete


class Wasted(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='wasted')
    async def wasted(self, ctx, target: User):
        await safe_delete(ctx)
        await ctx.send(embed=Embed(description=f"(x_x) **{target.name}** has been wasted.",
                                   color=0x2F3136)
                       .set_image(url=f"{await get_random_gif_by_theme('anime wasted')}"))

    @wasted.error
    async def wasted_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify someone to wasted, it would be so sad otherwise ! 😢", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that member...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Wasted(bot))
