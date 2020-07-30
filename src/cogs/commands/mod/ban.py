from discord.ext.commands import MissingRequiredArgument, BadArgument, MissingPermissions, BotMissingPermissions
from discord.ext import commands
from src.modules.random import get_random_gif_by_theme
from src.utils import empty_char
from discord import Embed, Member
from datetime import date


# Ban nasty people out from your server
class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, target: Member, *, reason: str = "N/A"):
        await ctx.message.delete()
        if target.guild_permissions.administrator:
            await ctx.send("The target is an admin.", delete_after=5.0)
        else:
            print(f"[log] {self.bot.get_guild(ctx.message.guild.id).name} | {ctx.author.name} has banned {target.name} | {date.today()}")
            await ctx.send(embed=Embed(description=f"I have banned {target.mention} for you **{ctx.author.name}**, give me a cookie ! (%cookie Chan)",
                                       color=0x2F3136)
                           .set_image(url=f"{await get_random_gif_by_theme('anime ban hammer')}")
                           .add_field(name=f"Reason: {reason if len(reason) < 255 else reason[:255] + '..'}", value=empty_char()), delete_after=8.0)
            await target.ban(reason=reason)

    @ban.error
    async def ban_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, MissingRequiredArgument) or isinstance(error, BadArgument):
            await ctx.send("Please specify someone to ban out !", delete_after=5.0)
        elif isinstance(error, MissingPermissions) or isinstance(error, BotMissingPermissions):
            await ctx.send("Sorry.. but you didn't give me the permission for...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Ban(bot))
