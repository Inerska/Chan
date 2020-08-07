from discord import User
from discord.ext.commands import MissingRequiredArgument, BadArgument

from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# ;)
from src.utils import safe_delete


class Wink(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='wink')
    async def wink(self, ctx, target: User):
        await safe_delete(ctx)
        if ctx.message.author != target:
            await ctx.send(embed=Embed(description=f"(✿-◡•̀) **{ctx.author.name}** winks **{target.name}**",
                                       color=0x2F3136)
                           .set_image(url=f"{await get_random_gif_by_theme('anime wink')}"))
        else: await ctx.send("You really want to wink alone-.. ? It's not a problem, but..", delete_after=5.0)

    @wink.error
    async def wink_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify someone to winks to, it would be so sad otherwise ! 😢", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that member...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Wink(bot))
