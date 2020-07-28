from discord.ext import commands
from src.utils import get_key_from_json, load_cogs


class Chan(commands.Bot):

    def __init__(self, prefix):
        super().__init__(command_prefix=prefix)

    async def on_ready(self):
        load_cogs(self, subdir='commands')
        load_cogs(self, subdir='commands/social')
        print(f"Logged as {self.user}, active in {len(self.guilds)} server(s) with a total amount of {len([user for user in self.users if not user.bot])} user(s).")


if __name__ == '__main__':
    client = Chan(prefix='%')
    client.run(get_key_from_json("TOKEN"))
