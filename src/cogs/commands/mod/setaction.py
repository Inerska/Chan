import discord
from discord.ext import commands
from src.callbacks_depend import message_dispatcher


# Set where join and leave message will be
from src.utils import safe_delete
from src.serverconfig import set_join_channel, set_guild_join


class SetChannelAction(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setaction')
    @commands.has_permissions(manage_messages=True)
    async def setaction(self, ctx):
        await safe_delete(ctx)
        set_guild_join(guild_id=ctx.guild.id, value=True)
        set_join_channel(guild_id=ctx.guild.id, channel_id=ctx.channel.id)
        await ctx.send("Join messages will be display there !")


def setup(bot):
    bot.add_cog(SetChannelAction(bot))
