from discord.ext import commands
from discord import Embed
from datetime import datetime
from src.serverconfig import get_per_guild_prefix


async def about_embed(bot_instance: commands.Bot, ctx):
    await ctx.channel.send(embed=Embed(description=f"Hello, I'm Chan 💞\n"
                                                   f"\n"
                                                   f"My prefix here is `{get_per_guild_prefix(_=None, message=ctx)}`, I'm owned by <@!228830814878564352>, you know, he is a kind master ! He gives me cookie everytiiime ! You know, you can do it too !\nIf you want more help about me, please check the help command !\n"
                                                   f"\n"
                                                   f"I'm also Open-Source please check my [GitHub Repertory <:git:741425389666173010> ](https://github.com/Inerska/Chan)\n"
                                                   f"If you need help, please join the [Assistance Server 💮](https://discord.gg/wbMXek6)"
                                                   f"\n"
                                                   f"\n"
                                                   f"Servers count: {len(bot_instance.guilds)}", timestamp=datetime.now(), colour=0x2F3136)
                           .set_thumbnail(url=bot_instance.user.avatar_url))
