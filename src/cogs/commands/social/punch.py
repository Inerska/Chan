from discord import User
from discord.ext.commands import MissingRequiredArgument, BadArgument

from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# Hands are the solution
from src.utils import safe_delete


class Punch(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='punch')
    async def punch(self, ctx, target: User):
        await safe_delete(ctx)
        if ctx.message.author != target:
            await ctx.send(embed=Embed(description=f"O=('-'Q) **{ctx.author.name}** punches **{target.name}**",
                                       color=0x2F3136)
                           .set_image(url=f"{await get_random_gif_by_theme('anime punch')}"))
        else: await ctx.send("You really want to punch yourself-.. ?", delete_after=5.0)

    @punch.error
    async def punch_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify someone to punch on, it would be so sad otherwise ! 😢", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that member...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Punch(bot))
