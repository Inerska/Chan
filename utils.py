from distutils import util
import io
import json
import os


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
        return io.BytesIO(await response.read())


# Retrieving buffer data from argument's avatar
# async def get_buffer_avatar_from(user: Union[User, Member], size=128) -> bytes:
#     avatar_url = str(user.avatar_url_as(format='png', size=size))
#     async with aiohttp.ClientSession() as session:
#         async with session.get(avatar_url) as response:
#             avatar_buff = await response.read()
#         await session.close()
#         return avatar_buff


# Deleting user command message, preventing Permission error
async def safe_delete(ctx):
    try:
        await ctx.message.delete()
    except Exception as e:
        pass


# Converting string to bool type
def strtobool(string: str) -> bool:
    return bool(util.strtobool(string))
