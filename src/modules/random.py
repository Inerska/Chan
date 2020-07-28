import random

import aiohttp

from src.utils import fetch


# Retrieving gifs by theme query from Giphy API
async def get_random_gif_by_theme(theme: str):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session,
                               f"https://api.tenor.com/v1/random?q={theme.replace(' ', '+')}&contentfilter=medium")
        await session.close()
        return response["results"][random.randint(0, 19)]["media"][0]["gif"]["url"]


# Retrieving meme picture from Some-Random-API
async def get_random_meme_pic():
    async with aiohttp.ClientSession() as session:
        response = await fetch(session,
                               "https://some-random-api.ml/meme")
        await session.close()
        return response["image"]


# Retrieving joke text from Official Joke API by 15Dkatz
async def get_random_joke_text():
    async with aiohttp.ClientSession() as session:
        response = await fetch(session,
                               "https://official-joke-api.appspot.com/random_joke")
        await session.close()
        return response["setup"], response["punchline"]


# Retrieving image from API
async def get_link_from_API(api):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session,
                               api)
        await session.close()
        return response["link"]
