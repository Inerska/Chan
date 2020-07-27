import discord
import json


# Retrieving discord bot token with opening the env json file
def get_token_from_json():
    with open('env.json', 'r+') as os:
        data = json.load(os)
    return data["TOKEN"]


class Chan(discord.Client):

    async def on_ready(self):
        get_token_from_json()
        print("Logged as", self.user)


client = Chan()
client.run(get_token_from_json())
