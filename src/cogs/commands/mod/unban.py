from discord.ext.commands import MissingRequiredArgument, BadArgument, MissingPermissions, BotMissingPermissions
from discord.ext import commands
from src.modules.random import get_random_gif_by_theme
from src.utils import empty_char
from discord import Embed, Member
from datetime import date


# Unban, you have to forgive sometimes...
class Unban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Example : %unban Ergazia#7586
    @commands.command(name='unban', aliases=['pardon', 'forgive', 'deban'])
    @commands.has_permissions(kick_members=True)
    async def unban(self, ctx, *, target):
        ban_list = await ctx.guild.bans()
        member_name, member_id = target.split('#')
        for entry in ban_list:
            user = entry.user
            print(user.name)
            if (user.name, user.discriminator) == (member_name, member_id):
                await ctx.guild.unban(user)
                await ctx.message.delete()
                print(f"[log] {self.bot.get_guild(ctx.message.guild.id).name} | {ctx.author.name} has unbanned {user.mention} | {date.today()}")
                await ctx.send(embed=Embed(description=f"I have unbanned {user.mention} for you **{ctx.author.name}**, give me a cookie ! (%cookie Chan)",
                                           color=0x2F3136)
                               .set_image(url=f"{await get_random_gif_by_theme('anime forgive')}"), delete_after=8.0)
            else: await ctx.send("Are you sure that user exists or is banned ? 😓", delete_after=5.0)

    @unban.error
    async def unban_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, MissingRequiredArgument) or isinstance(error, BadArgument):
            await ctx.send("Please specify someone to unban !", delete_after=5.0)
        elif isinstance(error, MissingPermissions) or isinstance(error, BotMissingPermissions):
            await ctx.send("Sorry.. but you didn't give me the permission for...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Unban(bot))
