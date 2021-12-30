import discord
from discord.ext import commands
import random
import os

from cogs.common import Common
from cogs.loops import Loops
from cogs.lists import Lists
from cogs.sentence_generation import SentenceGeneration
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

class Listeners(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.Cog.listener()
    async def on_ready(self):
        await Common.log(self, 'BOT ACTIVATED')
        print('BOT ACTIVATED')

    
    #@commands.Cog.listener()
    #async def on_command_error(self, ctx, error):
    #    await ctx.send(f'Oops, my system crashed. I lost my data! And I have an antivirus!\nError: {error}')
    #    await Common.log(self, f'Oops, my system crashed. I lost my data! And I have an antivirus!\nError: {error}', ctx)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await Common.log(self, f'bot of deatg joined {guild}')
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send(random.choice(["BOT OF DEATG HAS ARRIVED", "BOT OF DEATG IS HERE","bot of deatg joined the game","BOT OF DEATG TIME","IT'S TIME TO BOT OF DEATG","THIS SERVER IS NOW 100% SOUP", "THIS SERVER IS NOW 100% SOUP"]))
                await channel.send(f"Chance of bot of deatg getting kicked from this server: {random.choice(Lists.percents)}")
                break


    #@commands.Cog.listener()
    #async def on_member_join(self, member):
    #    await Common.log(self, f'{member} joined a server')
    #    for channel in member.guild.text_channels:
    #        if channel.permissions_for(member.guild.me).send_messages:
    #            await channel.send(random.choice([f"{member} has joined yay", f"yay {member} joined"]))
    #            break


    async def decide_message(self, message):
            
        message_to_send = Common.random_message(self)

        message_type = random.randint(0, 200)

        if 0 <= message_type <= 170:
            message_to_send = Common.random_message(self)
        elif 171 < message_type <= 180:
            message_to_send = SentenceGeneration.generate_sentence(self)
        elif 180 < message_type <= 185:
            message_to_send = SentenceGeneration.generate_demfex_quote(self)
        elif 185 < message_type <= 187:
            message_to_send = Common.generate_fake_japanese_sentence(self)
        elif 187 < message_type <= 195:
            message_to_send = await Common.dynamic_message(self, message)
        elif 195 < message_type <= 200:
            message_to_send = Common.minecraft_message(self, message)
            
        if random.randint(0, 1000) < 70:
            message_to_send = Common.random_style(self, message_to_send)
        if random.randint(0, 1000) < 70:
            message_to_send = await Common.random_word_edit(self, message_to_send)
        if random.randint(0, 1000) < 20:
            message_to_send = Common.random_insert(self, message_to_send)
        if random.randint(0, 1000) < 20:
            message_to_send = Common.cutoff(self, message_to_send)
        if random.randint(0, 1000) < 70:
            message_to_send = await Common.fancy_letters(self, message_to_send)
        if random.randint(0, 1000) < 800:
            message_to_send = Common.random_emoji_insert(self, message_to_send)


        return message_to_send

    @commands.Cog.listener()
    async def on_message(self, message):

        #author_id = str(message.author.id)

        if 'sans' in message.clean_content.lower() and not message.channel.id in Common.spam_channel_ids:
            try:
                await message.add_reaction('<:Sans:842198488358977566>') 
                await Common.log(self, 'OMG SANMS UNDERTAL')
            except:
                await Common.log(self, 'OMG SANMS UNDERTAL failed this is so sad')

        #random msg send chance
        if random.randint(0, 1000) < 50 or self.client.user.mentioned_in(message):
            #random message has been triggered
            kind_of_message = random.randint(0, 1000)

            #regular message
            if kind_of_message <= 800:
                message_to_send = await Listeners.decide_message(self, message)

                if "quoting" in message.channel.name:
                    await message.channel.send(f'"{message_to_send}"')
                    return
                else:
                    await message.channel.send(message_to_send)
            
            #send emojis
            elif 800 < kind_of_message <= 1000:
                emoji = ""
                if random.randint(1, 100) > 7:
                    for i in range(random.randint(1, 5)):
                        emoji += random.choice(Lists.all_emoji)
                else:
                    for i in range(random.randint(6, 130)):
                        emoji += random.choice(Lists.all_emoji)

                await message.channel.send(emoji)

            #file upload - DISCONTINUED
            #elif 960 < kind_of_message <= 1000:
            #    the_file = os.listdir('uploadable_files/')
            #    filename = random.choice(the_file)
            #    path = "uploadable_files/" + filename
            #    await message.channel.send(file=discord.File(path))

        #message reaction
        if random.randint(14, 70) == 69:

            #choose emoji type
            emoji = ""
            emoji_type = random.randint(1, 3)
            if emoji_type == 1:
                emoji = random.choice(self.client.emojis)
            else:
                emoji = random.choice(Lists.all_emoji)

            #deciding how many emojis 
            emoji_count = 0
            emoji_count_rng = random.randint(0, 250)
            if emoji_count_rng < 50 or emoji_count_rng > 100:
                emoji_count = 1
            elif 50 < emoji_count_rng <= 70: 
                emoji_count = 2
            elif 70 < emoji_count_rng <= 80: 
                emoji_count = 3
            elif 80 < emoji_count_rng <= 85: 
                emoji_count = 4
            elif 85 < emoji_count_rng <= 88: 
                emoji_count = 5
            elif 88 < emoji_count_rng <= 90: 
                emoji_count = 6
            elif emoji_count_rng == 91: 
                emoji_count = 7
            elif emoji_count_rng == 92: 
                emoji_count = 9
            elif emoji_count_rng == 93: 
                emoji_count = 11
            elif emoji_count_rng == 94: 
                emoji_count = 13
            elif emoji_count_rng == 95: 
                emoji_count = 14
            elif emoji_count_rng == 96: 
                emoji_count = 15
            elif emoji_count_rng == 97: 
                emoji_count = 16
            elif emoji_count_rng == 98: 
                emoji_count = 17
            elif emoji_count_rng == 99: 
                emoji_count = 18
            elif emoji_count_rng == 100: 
                emoji_count = 20

            for i in range(emoji_count):
                try:
                    await message.add_reaction(emoji)
                    emoji_type = random.randint(1, 3)
                    if emoji_type == 1:
                        emoji = random.choice(self.client.emojis)
                    else:
                        emoji = random.choice(Lists.all_emoji)
                except:
                    print('error reacting')

        


        #random reply to old msg --this doesn't really work
        if random.randint(0, 7600) < 6:
            async for msg in message.channel.history(limit=10000):
                if random.randint(0, 9000) < 5:
                    if msg.channel.id != 838451092739457084 and msg.channel.id != 471178465375158273:
                        message_to_send = await Listeners.decide_message(self, message)

                        if "quoting" in message.channel.name:
                            await message.channel.send(f'"{message_to_send}"')
                            return
                        else:
                            await message.channel.send(message_to_send)
                break


            return

        #status change
        if random.randint(0, 100) < 90:
            statusType = random.randint(2, 15)

            gameToSelect = random.choice([Lists.games, Lists.games, Lists.joke_games])
            gamePlaying = random.choice(gameToSelect)

            songToSelect = random.choice([Lists.tunesList, Lists.tunesList, Lists.memeSongs])
            songPlaying = random.choice(songToSelect)

            videoWatching = random.choice(Lists.videos)

            if statusType == 2:
                await self.client.change_presence(status=discord.Status.online, activity=discord.Game(name=gamePlaying))
            if statusType == 3:
                await self.client.change_presence(status=discord.Status.idle, activity=discord.Game(name=gamePlaying))

            if statusType == 4:
                await self.client.change_presence(status=discord.Status.online, activity=discord.Game(name=gamePlaying))
            if statusType == 5:
                await self.client.change_presence(status=discord.Status.idle, activity=discord.Game(name=gamePlaying))
            if statusType == 6:
                await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=gamePlaying))


            if statusType == 7:
                await self.client.change_presence(status=discord.Status.online, activity=discord.Streaming(name=gamePlaying, url="http://deatg.com"))
            if statusType == 8:
                await self.client.change_presence(status=discord.Status.idle, activity=discord.Streaming(name=gamePlaying, url="http://deatg.com"))
            if statusType == 9:
                await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Streaming(name=gamePlaying, url="http://deatg.com"))

            if statusType == 10:
                await self.client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=videoWatching))
            if statusType == 11:
                await self.client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=videoWatching))
            if statusType == 12:
                await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name=videoWatching))

            if statusType == 13:
                await self.client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=songPlaying))
            if statusType == 14:
                await self.client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=songPlaying))
            if statusType == 15:
                await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name=songPlaying))

        if random.randint(0, 39000) < 10 or "GGGGRRRROOOWWWWEABgggg" in message.clean_content.lower():
            img = Image.open("images/quote.jpg")


            draw = ImageDraw.Draw(img)
            #selected_font = random.choice(os.listdir("fonts/"))
            font = ImageFont.truetype("fonts/Honoka-Shin-Antique-Kaku_M.otf", 80)

            the_quote = message.clean_content.lower()

            selected_user = str(message.author)
            selected_user = selected_user[:-5]

            asset = message.author.avatar_url_as(size = 256)
            data = BytesIO(await asset.read())
            avatar = Image.open(data)
            avatar = avatar.resize((390, 390))
            if any(ext in the_quote for ext in Lists.hiragana):
                if len(the_quote) > 24:
                    the_quote = the_quote[:24] + "\n" + the_quote[24:]
            else:
                if len(the_quote) > 37:
                    the_quote = the_quote[:37] + "\n" + the_quote[37:]

            text = f"\"{the_quote}\"\n\n                          - {selected_user}"

            draw.text((150, 660), text, (255, 255, 255), font=font)
            img.paste(avatar, (180, 110), avatar)
            img.save("quote.png")

            await message.reply(file = discord.File("quote.png"))

        await self.client.process_commands(message)






def setup(client):
    client.add_cog(Listeners(client))