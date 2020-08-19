import aiohttp
from discord import User, Message, File
from discord.ext.commands import BadArgument, MissingRequiredArgument

from discord.ext import commands
from numpy import format_parser

from utils import fetch_media

# Trigger.. bruhhh
from utils import safe_delete


# Returning a triggered avatar
async def trigger_pic(pic: str):
    async with aiohttp.ClientSession() as session:
        triggered = await fetch_media(session,
                                      f"https://some-random-api.ml/canvas/triggered?avatar={pic}")
        await session.close()
        return triggered


class Trigger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='trigger')
    async def trigger(self, ctx, target: User):
        await safe_delete(ctx)
        if ctx.message.author != target:
            await ctx.send(file=File(await trigger_pic(str(target.avatar_url_as(static_format='png'))),
                           f"trigger_{target}.gif"))
        else:
            await ctx.send(file=File(await trigger_pic(str(ctx.message.author.avatar_url_as(static_format='png'))),
                           f"trigger_{ctx.message.author}.gif"))

    @trigger.error
    async def trigger_error(self, ctx, error):
        await safe_delete(ctx)
        if isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that member...", delete_after=5.0)
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send(file=File(await trigger_pic(str(ctx.message.author.avatar_url_as(static_format='png'))),
                           f"trigger_{ctx.message.author}.gif"))


def setup(bot):
    bot.add_cog(Trigger(bot))
