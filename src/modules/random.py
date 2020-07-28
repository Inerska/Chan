import random
import aiohttp

from src.utils import get_key_from_json, fetch


# Retrieving gifs by theme query from Giphy API
async def get_random_gif_by_theme(theme: str):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session,
                               f"http://api.giphy.com/v1/gifs/search?q={theme.replace(' ', '+')}&api_key={get_key_from_json('GIPHY_API_KEY')}&limit=10&sort=revelant&rating=g")
        await session.close()
        return response["data"][random.randint(0, 9)]["images"]["downsized"]["url"]
