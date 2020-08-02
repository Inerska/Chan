import os
import json
from datetime import date
from discord.ext import commands


# Checking if the server has it's json file
def check_server_json(bot_instance: commands.Bot):
    json_pattern = {}
    for guild in bot_instance.guilds:
        if not os.path.exists(f'../servers/{guild.id}.json'):
            with open(f"../servers/{guild.id}.json", 'w') as json_file:
                json.dump(json_pattern, json_file)
                print(f"[os] {guild.id}.json has been created | {date.today()}")
