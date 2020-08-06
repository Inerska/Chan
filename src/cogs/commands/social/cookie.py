from discord import User
from discord.ext.commands import MissingRequiredArgument, BadArgument

from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# Give a cookie, eat a cookie, cookie forever <3
from src.utils import safe_delete


class Cookie(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cookie')
    async def cookie(self, ctx, target: User):
        await safe_delete(ctx)
        if target == self.bot.user:
            await ctx.send(f"Thankkks ! I love cookies ! I love you sooo muchhh ! (%luv)")
        elif ctx.message.author != target:
            await ctx.send(f"👉 👈 Hey {target.mention}, {ctx.message.author.mention} gave you a cookie ! 🍪")
        else: await ctx.send("Do not be egoist ! (Give me that cookie)", delete_after=5.0)

    @cookie.error
    async def cookie_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify someone to give your cookie, it would be so sad if it's not eaten ! 😢", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that member... but.. can I eat it ? :p", delete_after=5.0)


def setup(bot):
    bot.add_cog(Cookie(bot))
