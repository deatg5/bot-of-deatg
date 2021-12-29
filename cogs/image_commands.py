import discord
from discord.ext import commands
from discord.ext.commands.core import Command
import random
from random import randint
import os
import math
import requests
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

from cogs.common import Common
from cogs.lists import Lists

class ImageCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command(brief="generate mario 64 sign image")
    async def sign(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        sign = Image.open("images/1707.png")
        asset = user.avatar_url_as(format="png", size = 128)
        data = BytesIO(await asset.read())
        avatar = Image.open(data)
        avatar = avatar.resize((168,168))

        sign.paste(avatar, (301,106), avatar)
        sign.save("generated_sign.png")
    
        await ctx.send(file = discord.File("generated_sign.png"))

    @commands.command()
    async def quote_image(self, ctx, *input_text):
        img = Image.open("images/quote.jpg")

        draw = ImageDraw.Draw(img)
        #selected_font = random.choice(os.listdir("fonts/"))
        font = ImageFont.truetype("fonts/Honoka-Shin-Antique-Kaku_M.otf", 80)

        selected_user = str(ctx.author)
        selected_user = selected_user[:-5]
        asset = ctx.author.avatar_url_as(format="png", size = 256)
        data = BytesIO(await asset.read())
        avatar = Image.open(data)
        avatar = avatar.resize((390, 390))
        input_text = " ".join(input_text[:])
        if any(ext in input_text for ext in Lists.hiragana):
            if len(input_text) > 24:
                input_text = input_text[:24] + "\n" + input_text[24:]
        else:
            if len(input_text) > 38:
                input_text = input_text[:38] + "\n" + input_text[38:]
        text = f"\"{input_text}\"\n\n                        - {selected_user}"
        draw.text((150, 660), text, (255, 255, 255), font=font)
        img.paste(avatar, (180, 110), avatar)
        img.save("quote.png")
        await ctx.send(file = discord.File("quote.png"))


    @commands.command(aliases=["ci"],brief="randomly generate an image")
    async def cool_image(self, ctx, image = None):
        if image == None:
            selected_file = random.choice(os.listdir("images/"))
            img = Image.open("images/" + selected_file)
        else:
            img = Image.open(requests.get(image, stream=True).raw)
        loop_times = random.randint(1, 16)
        for i in range(loop_times):
            members = ctx.guild.members
            emojis = ctx.guild.emojis
            user = random.choice(members)
            selected_emoji = random.choice(emojis)
            emoji = selected_emoji.url_as()

            selected_font = random.choice(os.listdir("fonts/")) 

            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("fonts/" + selected_font, random.randint(10, 200))
            text = Common.random_message(self)    

            asset = user.avatar_url_as(size = 128)
            data = BytesIO(await asset.read())
            avatar = Image.open(data)
            avatar = avatar.resize((random.randint(1, 450), random.randint(1, 450)))    

            emoji_data = BytesIO(await emoji.read())
            emoji = Image.open(emoji_data)
            emoji = emoji.resize((random.randint(1, 450),random.randint(1, 450)))   

            draw.text((random.randint(0, math.floor(img.width / 20)), random.randint(0, img.height)), text, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), font=font)
            img.paste(avatar, (random.randint(0, img.width), random.randint(0, img.height)), avatar)
            img.paste(emoji, (random.randint(0, img.width), random.randint(0, img.height)), emoji)
        img.save("generated_image.png")

        await ctx.send(file = discord.File("generated_image.png"))

def setup(client):
    client.add_cog(ImageCommands(client))