from discord import User
from discord.ext.commands import MissingRequiredArgument, BadArgument

from discord import Embed
from discord.ext import commands

from modules.random import get_random_gif_by_theme


# Moooh... poor thing
from utils import safe_delete


class Pat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pat', aliases=["patpat"])
    async def pat(self, ctx, target: User):
        await safe_delete(ctx)
        if ctx.message.author != target:
            await ctx.send(embed=Embed(description=f"(　´Д｀)ﾉ(´･ω･`) **{ctx.author.name}** patpats **{target.name}**",
                                       color=0x2F3136)
                           .set_image(url=f"{await get_random_gif_by_theme('anime pat')}"))
        else: await ctx.send("You really want to pat yourself-.. ? It's not a problem, but..", delete_after=5.0)

    @pat.error
    async def pat_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify someone to pat on, it would be so sad otherwise ! 😢", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that member...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Pat(bot))
