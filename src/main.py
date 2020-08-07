from discord.ext import commands
from src.serverconfig import check_server_json, get_per_guild_prefix
from src.utils import get_key_from_json, load_cogs
from src.callbacks_depend import join_dispatcher, message_dispatcher


class Chan(commands.Bot):

    def __init__(self, prefix):
        super().__init__(command_prefix=prefix)

    @commands.Cog.listener()
    async def on_ready(self):
        check_server_json(self)                         # Check if each servers where the bot is, have a json config file
        load_cogs(self, subdir='commands')              # Loading all commands
        load_cogs(self, subdir='commands/social')       # Loading all social commands
        load_cogs(self, subdir='commands/utility')      # Loading very useful commands
        load_cogs(self, subdir='commands/mod')          # Loading all moderation commands
        load_cogs(self, subdir='commands/game_stats')   # Loading all game stats commands
        print(f"Logged as {self.user}, active in {len(self.guilds)} server(s) with a total amount of {len([user for user in self.users if not user.bot])} user(s).")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        check_server_json(self)                         # Update guild informations

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await join_dispatcher.send_join_canvas(self, member)

    @commands.Cog.listener()
    async def on_message(self, message):
        if str(self.user.id) in message.content:
            await message_dispatcher.about_embed(self, message)
        await client.process_commands(message)


if __name__ == '__main__':
    client = Chan(prefix=get_per_guild_prefix)
    # Middleware
    client.remove_command('help')
    client.run(get_key_from_json("TOKEN"))
