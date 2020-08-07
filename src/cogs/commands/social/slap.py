from discord import User
from discord.ext.commands import MissingRequiredArgument, BadArgument

from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# Take a bit if you are hungry
from src.utils import safe_delete


class Slap(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='slap')
    async def slap(self, ctx, target: User):
        await safe_delete(ctx)
        if ctx.message.author != target:
            await ctx.send(embed=Embed(description=f"(=ﾟ ωﾟ)つ )ﾟ∀ﾟ) **{ctx.author.name}** slaps **{target.name}**",
                                       color=0x2F3136)
                           .set_image(url=f"{await get_random_gif_by_theme('anime slap')}"))
        else: await ctx.send("You really want to slap yourself-.. ? It's not a problem, but..", delete_after=5.0)

    @slap.error
    async def slap_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify someone to slap, it would be so sad otherwise ! 😢", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that member...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Slap(bot))
