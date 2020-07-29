from dataclasses import dataclass

import aiohttp
from src.utils import fetch
from discord.ext.commands import MissingRequiredArgument, BadArgument
from discord.ext import commands
from discord import Embed


@dataclass
class AnimeInfo:
    Title: str
    Type: str
    Episodes: str
    Airing: bool
    Score: float
    Synopsis: str
    Image_URL: str
    URL: str


# Powered with Jikan API for MAL
async def get_anime_info_by_name(name: str) -> AnimeInfo:
    async with aiohttp.ClientSession() as session:
        response = await fetch(session,
                               f"https://api.jikan.moe/v3/search/anime?q={name}")
        await session.close()
        return AnimeInfo(response["results"][0]["title"],
                         response["results"][0]["type"],
                         response["results"][0]["episodes"],
                         response["results"][0]["airing"],
                         response["results"][0]["score"],
                         response["results"][0]["synopsis"] if len(response["results"][0]["synopsis"]) < 516 else f"{response['results'][0]['synopsis'][:516]}..",
                         response["results"][0]["image_url"],
                         response["results"][0]["url"]
                         ) if len(response["results"]) > 0 else False


# Know more about anime
class Anime(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='anime', aliases=['animeinfo', 'ai', 'mal', 'myanimelist'])
    async def anime(self, ctx, *, term: str):
        await ctx.message.delete()
        query = await get_anime_info_by_name(term)
        if query:
            await ctx.send(embed=Embed(color=0x2F3136, title=f"Anime Informations for {query.Title} - {query.Type}", description=f"ᕙ(⇀‸↼‵‵)ᕗ **{ctx.author.mention}** I've find your anime !")
                           .set_thumbnail(url=query.Image_URL)
                           .add_field(name="**Information**", value=f"MAL Score: **{query.Score}**\nEpisodes: **{query.Episodes}**\nAiring: **{'Yes' if query.Airing else 'No'}**")
                           .add_field(name=f"**Synopsis**", value=f"{query.Synopsis}\n[See it on MAL]({query.URL})"))
        else: await ctx.send("It's so embarassing.. I can't find this anime..", delete_after=5.0)

    @anime.error
    async def anime_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify an anime name to search info for", delete_after=5.0)
        elif isinstance(error, BadArgument):
            await ctx.send("It's so embarassing.. I can't find this anime..", delete_after=5.0)


def setup(bot):
    bot.add_cog(Anime(bot))
