import json
import os


# Retrieving discord bot token with opening the env json file
def get_token_from_json():
    with open('env.json', 'r+') as file:
        data = json.load(file)
    return data["TOKEN"]


# Loading all python cogs files
def load_cogs(_client, subdir):
    for _cog in [file.split(".")[0] for file in os.listdir(f'cogs/{subdir}') if file.endswith('.py')]:
        try:
            _client.load_extension(f'cogs.{subdir}.{_cog}') if _cog != '__init__' else ...
        except Exception as e:
            print(e)


# Return an empty character
def empty_char() -> str:
    return '⠀'
