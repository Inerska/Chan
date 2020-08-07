from discord.ext import commands
from src.utils import get_key_from_json, load_cogs
from src.serverconfig import check_server_json, get_guild_prefix


class Chan(commands.Bot):

    def __init__(self, prefix):
        super().__init__(command_prefix=prefix)

    async def on_ready(self):
        check_server_json(self)                         # Check if each servers where the bot is, have a json config file
        load_cogs(self, subdir='callbacks')             # Loading event paradigm
        load_cogs(self, subdir='commands')              # Loading all commands
        load_cogs(self, subdir='commands/social')       # Loading all social commands
        load_cogs(self, subdir='commands/utility')      # Loading very useful commands
        load_cogs(self, subdir='commands/mod')          # Loading all moderation commands
        load_cogs(self, subdir='commands/game_stats')   # Loading all game stats commands
        print(f"Logged as {self.user}, active in {len(self.guilds)} server(s) with a total amount of {len([user for user in self.users if not user.bot])} user(s).")

    async def on_guild_join(self, guild):
        check_server_json(self)                         # Update guild informations


if __name__ == '__main__':
    client = Chan(prefix=get_guild_prefix)
    # Middleware
    client.remove_command('help')
    client.run(get_key_from_json("TOKEN"))
