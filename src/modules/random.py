import random
import json
from urllib.request import urlopen

from src.utils import get_key_from_json


def get_random_gif_by_theme(theme):
    response = json.load(urlopen(f"http://api.giphy.com/v1/gifs/search?q={theme}&api_key={get_key_from_json('GIPHY_API_KEY')}&limit=10&sort=revelant&rating=g"))
    return response["data"][random.randint(0, 9)]["embed_url"]
