from discord import User, Message
from discord.ext.commands import BadArgument, MissingRequiredArgument

from discord.ext import commands

from modules.random import get_random_gif_by_theme


# My avatar is beautifuler than yours, or maybe you just want to look at another one's avatar ?
from utils import safe_delete


class Avatar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='avatar', aliases=['pp'])
    async def avatar(self, ctx, target: User):
        await safe_delete(ctx)
        if ctx.message.author != target:
            await ctx.send(f"{ctx.message.author.mention}, that's the avatar of **{target.name}**\n{target.avatar_url_as(size=4096)}")
        else: await ctx.send(f"{ctx.message.author.mention}, that's your avatar !\n{ctx.message.author.avatar_url_as(size=4096)}")

    @avatar.error
    async def avatar_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that member...", delete_after=5.0)
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send(f"{ctx.message.author.mention}, that's your avatar !\n{ctx.message.author.avatar_url_as(size=4096)}")


def setup(bot):
    bot.add_cog(Avatar(bot))
