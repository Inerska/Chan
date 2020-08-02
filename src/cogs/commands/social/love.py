from random import randint
from discord import Embed
from discord.ext import commands

from src.modules.random import get_random_gif_by_theme


# Sometimes we need some love
from src.utils import safe_delete


class Love(commands.Cog):
    sentence = ["Put your head on my shoulder..~",
                "Sending virtual hug... (%hug @me)",
                "I want to taste your soul",
                "It's gonna be okay, everything gonna be okay!",
                "I'm here, don't be sad, things will be ok!",
                "Why are you soo cuteee ?",
                "Meooow~ :3",
                "You are awesome!",
                "I love you!",
                "Feel like cries ? Try some fries",
                "Please don't be so hard on yourself! It makes me sad to see you like this :(",
                "When you're depressed, it always helps to lean your head on your arms",
                "You don't have to force yourself to do anything you don't want to",
                "Everything is ok, you can do it",
                "You're going to get through this okay",
                "I'm doing good because you're here with me !",
                "Today was not great but tomorrow might be :3",
                "YOU CAN DO IT I BELIEVE IN YOU !",
                "Just a daily reminder that people love you and appreciate you, and.. me :x 👉 👈"]

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='love')
    async def love(self, ctx):
        await safe_delete(ctx)
        await ctx.send(embed=Embed(color=0x2F3136,
                                   description=f"{ctx.message.author.mention}, {self.sentence[randint(0, len(self.sentence))]} 💞"))


def setup(bot):
    bot.add_cog(Love(bot))
