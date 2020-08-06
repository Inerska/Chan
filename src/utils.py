import io
import json
import os
import re
from datetime import date


# Retrieving discord bot token with opening the env json file
def get_key_from_json(key: str):
    with open('env.json', 'r+') as file:
        data = json.load(file)
    return data[key]


# Loading all python cogs files
def load_cogs(_client, subdir: str):
    for _cog in [file.split(".")[0] for file in os.listdir(f'cogs/{subdir}') if file.endswith('.py')]:
        subdir = subdir.replace('/', '.')
        try:
            _client.load_extension(f'cogs.{subdir}.{_cog}') if _cog != '__init__' else ...
        except Exception as e:
            print(e)


# Return an empty character
def empty_char() -> str:
    return '⠀'


# Fetching data from restful api
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


# Fetching media from restful api, returning a buffer
async def fetch_media(session, url):
    async with session.get(url) as response:
        data = io.BytesIO(await response.read())
        data.seek(0)
        return data


# Deleting user command message, preventing Permission error
async def safe_delete(ctx):
    try:
        await ctx.message.delete()
    except Exception as e:
        pass
