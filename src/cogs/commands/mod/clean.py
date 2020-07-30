from discord.ext.commands import MissingRequiredArgument, BadArgument
from discord.ext import commands
from src.modules.random import get_random_gif_by_theme
from discord import Embed
from datetime import date


# Clean the chat as your floor
class Clean(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clean', aliases=['clear', 'clearchat', 'cleanchat', 'cc'])
    @commands.has_permissions(manage_messages=True)
    async def clean(self, ctx, interval: int):
        if interval <= 200:
            await ctx.message.delete()
            await ctx.channel.purge(limit=interval)
            print(f"[log] {self.bot.get_guild(ctx.message.guild.id).name} | {ctx.author.name} has cleared the chat | {date.today()}")
            await ctx.send(embed=Embed(description=f"I have cleared {interval} messages... I can see my reflection now",
                                       color=0x2F3136)
                           .set_image(url=f"{await get_random_gif_by_theme('anime wash')}"), delete_after=8.0)
        else: await ctx.send("It's too big, isn't it ?", delete_after=5.0)

    @clean.error
    async def clean_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify an interval of messages !", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't well understand what you mean...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Clean(bot))
