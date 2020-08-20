import discord
from discord.ext import commands

# I need some help...
from utils import safe_delete


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=discord.Embed(title="List of the commands ",
                                           description="``` You used the command \"help\"`to get there !```")
                       .add_field(name="『⛔』  Staff", value="``` - kick  - ban  - mute  - clear```", inline=True)
                       .add_field(name="『💭』  Social", value="```profile  - avatar ```", inline=True)
                       .add_field(name="『🏃🏼‍♂️』  Fun, animation",
                                  value="``` - love  - undertale - pika  - bite  - cuddle  - facepalm - greet  - highfive  - hug  - food  - kiss  - lick  - punch - wasted  - sleep  - nom  - slap  - blush  - poot  - hug  - smug  - cry  - wink  - kiss  - patpat  - shrug  - tickle  - tsundere```",
                                  inline=True)
                       .add_field(name="『🤡』  Memes",
                                  value="``` - cat  - dog  - fox  - koala  - lizard  - panda  - shiba```", inline=True)
                       .add_field(name="『💎』  System level", value="```- xp  - lvl```", inline=True)
                       .add_field(name="『🎵 』  Song", value="```-  play  - stop  - pause   - reading ```", inline=True)
                       .add_field(name="『🎁』  Giveaway", value="```giveaway```", inline=True)
                       .add_field(name="『🔍』  Search", value="```-  animeinfo  - google  - invite - wiki``",
                                  inline=True)
                       .add_field(name="『🎲』  Games", value="```- flip  - roll  - maths  - 8ball ```", inline=True)
                       .add_field(name="『📥』  Infos", value="```-  lyrics   - invite  - linkshorten  - setprefix  ```",
                                  inline=True)
                       .add_field(name="『❔』  Support",
                                  value="[Website](https://disboard.org/fr/site/redirect) | [Vote](https://disboard.org/fr/site/redirect)",
                                  inline=False)
                       .set_footer(text="Chan v1 | Create by Ergazia"))


def setup(bot):
    bot.add_cog(Help(bot))
