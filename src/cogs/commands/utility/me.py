import discord
from discord.ext import commands
from src.callbacks_depend import message_dispatcher


# Who am I ?
from src.utils import safe_delete


class Me(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='me', aliases=['info', 'bot', 'about', 'you', 'chan', 'invite', 'link', 'lien', 'contact', 'liens'])
    async def me(self, ctx):
        await safe_delete(ctx)
        await message_dispatcher.about_embed(self.bot, ctx)


def setup(bot):
    bot.add_cog(Me(bot))
