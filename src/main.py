from discord.ext import commands
from src.utils import get_token_from_json, load_cogs


class Chan(commands.Bot):

    def __init__(self, prefix):
        super().__init__(command_prefix=prefix)

    async def on_ready(self):
        get_token_from_json()
        load_cogs(self, subdir='commands')
        print(f"Logged as {self.user}, active in {len(self.guilds)} servers with a total amount of {len([user for user in self.users if not user.bot])} user(s).")


if __name__ == '__main__':
    client = Chan(prefix='/')
    client.run(get_token_from_json())
