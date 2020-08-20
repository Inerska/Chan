from random import randint
from discord import Embed
from discord.ext import commands

from modules.random import get_random_gif_by_theme


# Drink a bowl of nostalgy!
from utils import safe_delete


class Undertale(commands.Cog):

    sentence = ["Despite everything, it's still you.",
                "Hoi, I'm Flowey, Flowey the Flower!",
                "Isn't that delicious?",
                "You are filled with Determination.",
                "Hi. I'm Bob.",
                "Pathetic, is it not? I can't even save a single child.",
                "S H O U L D  B E  B U R N I N G  I N  H E L L",
                "OHHHHHHHH, YESSSSSSSS!",
                "I'M UNDYNE AND I'M PILING ON THE SMOOCHES!",
                "YOU! WILL! NEVER! SPARE ME!",
                "Get Dunked On!",
                "HOI! I'm TEMMIE!",
                "NYEH HEH HEH HEH!",
                "Don't kill and don't be killed, alright?",
                "finally, I was so tired of being a flower",
                "Oh wait, I just remembered... You don't have any friends",
                "That's the trash can, feel free to visit it anytime",
                "YOU MADE YOUR CHOICE LONG AGO.",
                "I don't want to let go"]

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='undertale')
    async def undertale(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=Embed(description=f"(￣__￣) « {self.sentence[randint(0, len(self.sentence))]} »",
                                   color=0x2F3136)
                       .set_image(url=f"{await get_random_gif_by_theme('undertale')}"))


def setup(bot):
    bot.add_cog(Undertale(bot))
