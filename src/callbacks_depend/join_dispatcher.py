from typing import Union

from PIL import ImageFont, Image, ImageDraw
from discord import User, Member, File
from src.serverconfig import get_join_message, get_join_channel, is_guild_join_enabled
import io


# Send join canvas
async def send_join_canvas(ctx, usr: Union[User, Member]):
    if is_guild_join_enabled(usr.guild.id):
        fms_regular = ImageFont.truetype("Montserrat-Regular.ttf", 40)
        fms_bold = ImageFont.truetype("Montserrat-Bold.ttf", 76)
        fms_light = ImageFont.truetype("Montserrat-Light.ttf", 40)

        image = Image.open('../src/medias/img/default_background.png').convert('RGBA')
        img_width, img_height = image.size

        rectangle_image = Image.new('RGBA', image.size)
        rectangle_draw = ImageDraw.Draw(rectangle_image)
        rectangle_draw.rectangle((20, 20, img_width - 20, img_height - 20), fill=(0, 0, 0, 128))

        # Manipulation
        rectangle_draw.text((297, 236), "WELCOME", (255, 255, 255), font=fms_bold)
        rectangle_draw.text((352, 316), str(usr).upper(), (160, 127, 215), font=fms_regular)
        rectangle_draw.text((303, 401), "ON MY SERVER UwU", (255, 255, 255), font=fms_light)
        user_avatar = usr.avatar_url_as(format='jpg', size=128)
        buffer_user_avatar = io.BytesIO(await user_avatar.read())

        avatar_img = Image.open(buffer_user_avatar)

        circle_image = Image.new('L', (128, 128))
        circle_draw = ImageDraw.Draw(circle_image)
        circle_draw.ellipse((0, 0, 128, 128), fill=255)

        image = Image.alpha_composite(image, rectangle_image)
        # Layers
        image.paste(image, (0, 0))
        image.paste(avatar_img, (440, 72), circle_image)

        # Buffering
        buffer = io.BytesIO()
        image.save(buffer, format('png'), optimize=True)

        # Rendering
        buffer.seek(0)
        msg = get_join_message(usr.guild.id) if not "N/A" else f"Welcome {usr.mention} to my server ! 🌌"
        await ctx.get_channel(int(get_join_channel(usr.guild.id))).send(content=msg, file=File(buffer, 'welcomer.png'))
