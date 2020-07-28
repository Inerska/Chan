from discord import message
from discord.ext.commands import MissingRequiredArgument

from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


class Hug(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hug')
    async def hug(self, ctx, target):
        await ctx.message.delete()
        await ctx.send(embed=Embed(description=f"༼ つ ◕o◕ ༽つ **{ctx.author.name}** hugs **{target.name}**",
                                   color=0x2F3136)
                       .set_image(url=f"{get_random_gif_by_theme('anime hug')}"))

    @hug.error
    async def hug_error(self, ctx, target):
        await ctx.message.delete()
        if isinstance(target, MissingRequiredArgument):
            await ctx.send("Please specify someone to hug on, it would be so sad otherwise ! 😢", delete_after=5.0)


def setup(bot):
    bot.add_cog(Hug(bot))
