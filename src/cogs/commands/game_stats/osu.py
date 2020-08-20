# from dataclasses import dataclass
#
# from discord.ext.commands import MissingRequiredArgument, BadArgument, CommandOnCooldown
# import aiohttp
# from src.utils import fetch, safe_delete
# from discord import Embed
# from discord.ext import commands
#
#
# @dataclass
# class OsuProfile:
#     Author: int
#     Definition: int
#     Ref: str
#
#
# async def fetch_for_osu_profile(name: str, headers: dict) -> OsuProfile:
#     async with aiohttp.ClientSession(headers=headers) as session:
#         response = await fetch(session,
#                                f"http://api.urbandictionary.com/v0/define?term={term}")
#         await session.close()
#         return Meaning(response["list"][sense]["author"], response["list"][sense]["definition"], response["list"][sense]["permalink"]) if len(response["list"]) > 0 else False
#
#
# # I have more pp than you m8
# class Osu(commands.Cog):
#
#     def __init__(self, bot):
#         self.bot = bot
#
#     @commands.command(name='osu', aliases=['osustats'])
#     @commands.cooldown(1, 3)
#     async def osu(self, ctx, name: str):
#         await safe_delete(ctx)
#         terms_mean = await fetch_for_osu_profile(name)
#         if terms_mean:
#             await ctx.send(embed=Embed(description=f"（︶^︶）**{ctx.author.name}** that's the meaning of *{term}*",
#                                        color=0x2F3136)
#                            .add_field(name=f"Definition by __**{terms_mean.Author}**__",
#                                       value=f"{terms_mean.Definition}\n[See it on Urban Dictionary]({terms_mean.Ref})")
#                            .set_author(name="Urban Dictionary", icon_url="https://wjlta.files.wordpress.com/2013/07/ud-logo.jpg?w=300&h=98"))
#         else: await ctx.send("It's so embarassing.. I can't find this player..", delete_after=5.0)
#
#     @osu.error
#     async def osu_error(self, ctx, error):
#         await safe_delete(ctx)
#         if isinstance(error, MissingRequiredArgument):
#             await ctx.send("Please specify a name to find out the profile of", delete_after=5.0)
#         elif isinstance(error, BadArgument):
#             await ctx.send("Erm~, sorry- I can't find that term...", delete_after=5.0)
#         elif isinstance(error, CommandOnCooldown):
#             await ctx.send("You're typing so fast, wait a moment...", delete_after=5.0)
#
#
# def setup(bot):
#     bot.add_cog(Osu(bot))
