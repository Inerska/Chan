from discord.ext import commands
from src.utils import get_token_from_json, load_cogs


class Chan(commands.Bot):

    def __init__(self, prefix):
        super().__init__(command_prefix=prefix)

    async def on_ready(self):
        get_token_from_json()
        load_cogs(self, subdir='commands')
        print("Logged as", self.user)


if __name__ == '__main__':
    client = Chan(prefix='/')
    client.run(get_token_from_json())
