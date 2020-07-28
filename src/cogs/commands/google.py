from dataclasses import dataclass

from discord.ext.commands import MissingRequiredArgument, BadArgument
from discord.ext import commands


# More knowledge
class Google(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='google', aliases=['lgsfy', 'googleit', 'gi', 'lmgt', 'lmgtfy'])
    async def google(self, ctx, *, term: str):
        await ctx.message.delete()
        await ctx.send(f"https://lmgtfy.com/?q={term.replace(' ', '+')}")

    @google.error
    async def google_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify a term to google it", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that term...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Google(bot))
