import ssl
from datetime import date
from typing import Tuple
from utils import get_key_from_json, strtobool
from discord.ext import commands
from pymongo import MongoClient

client = MongoClient(f'mongodb+srv://{get_key_from_json("db_username")}:{get_key_from_json("db_password")}@root.zfrgv.gcp.mongodb.net/{get_key_from_json("db_name")}?retryWrites=true&w=majority', ssl_cert_reqs=ssl.CERT_NONE)
database = client["database_root"]
server_col = database["collection_root"]


def is_guild_registered(guild_id) -> bool:
    return server_col.find({"guild_id": guild_id}).count() > 0


# Checking if the server has it's json file
def check_server_json(bot_instance: commands.Bot) -> None:
    for guild in bot_instance.guilds:
        if not is_guild_registered(guild.id):
            server_col.insert_one({"guild_id": guild.id,
                                   "guild_prefix": "%",
                                   "log_channel": "False",
                                   "role_join": "False",
                                   "log_channel_id": "N/A",
                                   "role_join_id": "N/A",
                                   "music_channel": "False",
                                   "music_channel_id": "N/A",
                                   "private_channel": "False",
                                   "private_channel_id": "N/A",
                                   "xp_system": "False",
                                   "xp_channel_id": "N/A",
                                   "join": "False",
                                   "join_channel_id": "N/A",
                                   "join_message": "N/A",
                                   "join_image_url": "N/A",
                                   "quit_image_url": "N/A",
                                   "news": "False",
                                   "new_id": "N/A",
                                   "lang": "en"})
            print(f"[os] - {date.today()} » {guild.id} ({guild.name}) config file has been created.")


# Retrieving per guild prefix
def get_per_guild_prefix(_, message) -> str:
    return server_col.find_one({"guild_id": message.guild.id})["guild_prefix"]


# Define a new per guild prefix
def set_per_guild_prefix(prefix: str, guild_id) -> None:
    server_col.update_one({"guild_id": guild_id}, {"$set": {"guild_prefix": prefix}})


# Retrieving bool join
def is_guild_join_enabled(guild_id) -> bool:
    return server_col.find_one({"guild_id": guild_id})["join"]


# Retrieving join message
def get_join_message(guild_id) -> bool:
    return server_col.find_one({"guild_id": guild_id})["join_message"]


# Retrieving join channel
def get_join_channel(guild_id) -> bool:
    return server_col.find_one({"guild_id": guild_id})["join_channel_id"]


# Set join channel
def set_join_channel(guild_id, channel_id) -> None:
    server_col.update_one({"guild_id": guild_id}, {"$set": {"join_channel_id": channel_id}})


# Define bool join
def set_guild_join(guild_id, value: bool) -> None:
    server_col.update_one({"guild_id": guild_id}, {"$set": {"join": value}})
