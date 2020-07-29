from discord.ext.commands import MissingRequiredArgument, BadArgument
from discord.ext import commands
from src.modules.random import get_random_gif_by_theme
from src.utils import empty_char
from discord import Embed, Member
from datetime import date


# Kick nasty people out from your server
class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, target: Member, *, reason: str = "N/A"):
        await ctx.message.delete()
        print(f"[log] {self.bot.get_guild(ctx.message.guild.id).name} | {ctx.author.name} has kicked {target.name} | {date.today()}")
        await ctx.send(embed=Embed(description=f"I have kicked {target.mention} for you **{ctx.author.name}**, give me a cookie ! (%cookie Chan)",
                                   color=0x2F3136)
                       .set_image(url=f"{await get_random_gif_by_theme('anime kick')}")
                       .add_field(name=f"Reason: {reason if len(reason) < 255 else reason[:255] + '..'}", value=empty_char()), delete_after=8.0)
        await target.kick(reason=reason)

    @kick.error
    async def kick_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, MissingRequiredArgument) or isinstance(error, BadArgument):
            await ctx.send("Please specify someone to kick out !", delete_after=5.0)


def setup(bot):
    bot.add_cog(Kick(bot))
