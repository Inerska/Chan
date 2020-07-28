from dataclasses import dataclass

from discord.ext.commands import MissingRequiredArgument, BadArgument
import aiohttp
from src.utils import fetch
from discord import Embed
from discord.ext import commands


@dataclass
class Meaning:
    Author: int
    Definition: int
    Ref: str


async def search_meaning_of(term: str, sense: int) -> Meaning:
    async with aiohttp.ClientSession() as session:
        response = await fetch(session,
                               f"http://api.urbandictionary.com/v0/define?term={term}")
        await session.close()
        return Meaning(response["list"][sense]["author"], response["list"][sense]["definition"], response["list"][sense]["permalink"]) if len(response["list"]) > 0 else False


# More knowledge
class Urban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='urban')
    async def urban(self, ctx, term: str):
        await ctx.message.delete()
        terms_mean = await search_meaning_of(term, 0)
        if terms_mean:
            await ctx.send(embed=Embed(description=f"（︶^︶）**{ctx.author.name}** that's the meaning of *{term}*",
                                       color=0x2F3136)
                           .add_field(name=f"Definition by __**{terms_mean.Author}**__",
                                      value=f"{terms_mean.Definition}\n[See it on Urban Dictionary]({terms_mean.Ref})")
                           .set_author(name="Urban Dictionary", icon_url="https://wjlta.files.wordpress.com/2013/07/ud-logo.jpg?w=300&h=98"))
        else: await ctx.send("It's so embarassing.. I can't find this word..", delete_after=5.0)

    @urban.error
    async def urban_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify a term to find the meaning of", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("Erm~, sorry- I can't find that term...", delete_after=5.0)


def setup(bot):
    bot.add_cog(Urban(bot))
