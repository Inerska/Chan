from discord import User
from discord.ext.commands import MissingRequiredArgument, BadArgument

from discord import Embed
from discord.ext import commands

from modules.random import get_random_gif_by_theme


# Sluuurp.. nice taste bae <3
from utils import safe_delete


class Lick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='lick')
    async def lick(self, ctx, target: User):
        await safe_delete(ctx)
        if ctx.message.author != target:
            await ctx.send(embed=Embed(description=f"(ˆڡˆ) **{ctx.author.name}** is licking **{target.name}**",
                                       color=0x2F3136)
                           .set_image(url=f"{await get_random_gif_by_theme('anime lick')}"))
        else: await ctx.send("You really want to lick.. yourself-.. ?", delete_after=5.0)

    @lick.error
    async def lick_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify someone to lick on, it would be so sad otherwise ! 😢", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that member...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Lick(bot))
