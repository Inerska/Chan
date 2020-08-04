from discord.ext.commands import MissingRequiredArgument, BadArgument
from discord.ext import commands
from src.modules.random import get_random_gif_by_theme
from src.serverconfig import set_per_guild_prefix
from discord import Embed
from datetime import date


# Setting per-guild prefix
from src.utils import safe_delete


class SetPrefix(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setprefix', aliases=['defineprefix ', 'setpre ', 'sprefix ', 'spre'])
    @commands.has_permissions(manage_messages=True)
    async def setprefix(self, ctx, prefix: str):
        if 0 < len(prefix) < 10:
            await safe_delete(ctx)
            set_per_guild_prefix(prefix=prefix, guild_id=ctx.message.guild.id)
            print(f"[log] {self.bot.get_guild(ctx.message.guild.id).name} | {ctx.author.name} has edited the prefix to '{prefix}' | {date.today()}")
            await ctx.send(f"I have edited the server prefix to {prefix} (%cookie Chan)")
        else: await ctx.send("The prefix must be between 1 and 9 characters.", delete_after=5.0)

    @setprefix.error
    async def setprefix_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify a new prefix for your server !", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't well understand what you mean...", delete_after=5.0)


def setup(bot):
    bot.add_cog(SetPrefix(bot))
