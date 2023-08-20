import discord
from discord.ext import commands
import random
import asyncio
from random import randint
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

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
    	if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"yeah, please wait another {round(error.retry_after, 2)} seconds before starting spam again.")

    
    #@commands.Cog.listener()
    #async def on_command_error(self, ctx, error):
    #    await ctx.send(f'Oops, my system crashed. I lost my data! And I have an antivirus!\nError: {error}')
    #    await Common.log(self, f'Oops, my system crashed. I lost my data! And I have an antivirus!\nError: {error}', ctx)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.id == self.client.user.id:  # check if it's the bot that joined/left
                if before.self_mute != after.self_mute:  # check if the bot's mute status changed
                    await member.edit(mute=True)  # mute the bot
                elif before.self_deaf != after.self_deaf:  # check if the bot's deafen status changed
                    await member.edit(deafen=True)  # deafen the bot
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

        message_type = random.randint(0, 250)

        if 0 <= message_type <= 172:
            message_to_send = Common.random_message(self)
        elif 172 < message_type <= 180:
            message_to_send = SentenceGeneration.generate_sentence(self)
        elif 180 < message_type <= 182:
            message_to_send = SentenceGeneration.generate_demfex_quote(self)
        elif 182 < message_type <= 184:
            message_to_send = Common.generate_fake_japanese_sentence(self)
        elif 180 < message_type <= 195:
            message_to_send = await Common.dynamic_message(self, message)
        elif 195 < message_type <= 200:
            message_to_send = Common.minecraft_message(self, message)
        elif 200 < message_type <= 300:
            message_to_send = Common.chatbot_message(self)
            
        if random.randint(0, 1000) < 20:
            message_to_send = Common.random_style(self, message_to_send)
        if random.randint(0, 1000) < 20:
            message_to_send = await Common.random_word_edit(self, message_to_send)
        if random.randint(0, 1000) < 15:
            message_to_send = Common.random_insert(self, message_to_send)
        if random.randint(0, 1000) < 10:
            message_to_send = Common.cutoff(self, message_to_send)
        if random.randint(0, 1000) < 40:
            message_to_send = await Common.fancy_letters(self, message_to_send)
        if random.randint(0, 1000) < 35:
            message_to_send = Common.random_emoji_insert(self, message_to_send)
        if random.randint(0, 1000) < 80:
            message_to_send = Common.sentence_ender(self, message_to_send)

        return message_to_send
    

    @commands.Cog.listener()
    async def on_message(self, message):

        #author_id = str(message.author.id)

        #sans
        if 'sans' in message.clean_content.lower():
            try:
                await message.add_reaction('<:Sans:926163252306665532>')
                await Common.log(self, 'OMG SANMS UNDERTAL', message)
            except:
                await Common.log(self, 'OMG SANMS UNDERTAL failed this is so sad', message)


        #ratio
        if message.channel.id == 913202658821681192: #'ratio' in message.clean_content.lower() and random.randint(1, 2) == 1 or 
            try:
                await message.add_reaction("👍")
                await message.add_reaction("👎")
            except:
                print('error reacting')

        #neco arc bot
        if message.author.id == 920485628792160299:
            try:
                for i in range(1):
                    if random.randint(1, 100) < 50:
                        await message.add_reaction(random.choice(["🥰", "😍", "😘", "😻", "💌", "💘", "💝", "💖", "💗", "💓", "💞", "💕", "💟", "❣️", "💔", "❤️‍🔥", "❤️‍🩹", "❤️", "🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "🤍", "🫀", "💏"])) 
            except:
                await Common.log(self, 'failed to react')

        #if mentioned
        if (self.client.user.mentioned_in(message)) and not (message.channel.id in Common.every_word_channel_ids) and 'milk' in message.clean_content.lower():
            await message.channel.send(random.choice(["dont forget to check out GangoZango on YouTube","i really think you should check out GangoZango on YouTube", "We interrupt your regularly scheduled bot of deatg message to bring you a word from our sponsor, GangoZango on YouTube: dont forget to check out GangoZango on YouTube"]))
            

        #random msg send chance
        if (random.randint(0, 1000) < 10 or self.client.user.mentioned_in(message)) and not (message.channel.id in Common.every_word_channel_ids):
            #random message has been triggered
            kind_of_message = random.randint(0, 900)

            #regular message
            if kind_of_message <= 800:
                message_to_send = await Listeners.decide_message(self, message)

                if "quoting" in message.channel.name:
                    await message.channel.send(f'"{message_to_send}"')
                    return
                else:
                    await Common.send(self, message.channel, message_to_send)
                    #await message.channel.send(message_to_send)
            
            #send emojis
            elif 800 < kind_of_message <= 1000:
                emoji = ""
                if random.randint(1, 100) > 7:
                    for i in range(random.randint(1, 5)):
                        emoji += random.choice(random.choice([Lists.all_emoji, Lists.all_emoji, Lists.all_emoji, Lists.all_face_emoji]))
                else:
                    for i in range(random.randint(6, 130)):
                        emoji += random.choice(random.choice([Lists.all_emoji, Lists.all_emoji, Lists.all_emoji, Lists.all_face_emoji]))

                await Common.send(self, message.channel, emoji)
                #await message.channel.send(emoji)

            #file upload - DISCONTINUED
            #elif 960 < kind_of_message <= 1000:
            #    the_file = os.listdir('uploadable_files/')
            #    filename = random.choice(the_file)
            #    path = "uploadable_files/" + filename
            #    await message.channel.send(file=discord.File(path))


        #if in DM
        if isinstance(message.channel, discord.DMChannel):
            if message.author != self.client.user: 
                    
                if randint(0, 100) >= 4:
                    await asyncio.sleep(float(randint(0, 40))) 
                    #check number of msgs
                    count = 0
                    async for msg in message.channel.history(limit = 6):
                        if msg.author != self.client.user:
                            count += 1
                        if msg.author == self.client.user:
                            break
                    async with message.channel.typing():
                        await asyncio.sleep(float(randint(0, 13)))
                        if count >= 3:
                            await message.reply(await Listeners.decide_message(self, message))
                        else:
                            await Common.send(self, message.channel, await Listeners.decide_message(self, message))
                            #await message.channel.send(await Listeners.decide_message(self, message))


        #message reaction
        if random.randint(0, 160) == 69:
            reaction_type = random.randint(1, 12)

            if reaction_type == 15:
                try:
                    await message.add_reaction("👍")
                    await message.add_reaction("👎")
                except:
                    print('error reacting')
            else:
                #choose emoji type
                emoji = ""
                emoji_type = random.randint(1, 3)
                if emoji_type == 1:
                    emoji = random.choice(message.guild.emojis)
                else:
                    emoji = random.choice(Lists.all_emoji)

                #deciding how many emojis 
                emoji_count = 0
                emoji_count_rng = random.randint(0, 160)
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
                            emoji = random.choice(message.guild.emojis)
                        else:
                            emoji = random.choice(message.guild.emojis)
                    except:
                        print('error reacting')


        
        if ';help' in message.clean_content.lower():
            embed=discord.Embed(title="bot of deatg", description="commands", color=Common.random_color())

            embed.add_field(name="misc commands", 
            value=  "**ai**                 \nsends a pre-generated message by the GPT2 AI engine\n" +
                    "**8ball**              \nask the bot a question\n" + 
                    "**emojiletters (el)**       \nconverts message to emoji letters\n" +
                    "**emojipasta**         \nadds emojis between each word\n" +
                    "**emojis**             \nsends some random regular emojis\n" +
                    "**face_emojis**        \nsends some random regular emojis\n" +
                    "**invite**             \nsends invite link\n" +
                    "**minecraft**          \nrandom minecraft item, block, or entity\n" +
                    "**mon**                \nguesses the pokemon sent by pokemon discord bot\n" +
                    "**ping**               \nshows the bot's ping\n"
                    "**server_emojis**      \nsends random emojis from servers the bot's in\n" +
                    "**server_information (si)** \nsend info about the current server\n" +
                    "**help**               \nShows this message\n" +
                    "**leaderboard**        \nthe global leaderboard (1 xp = 1 message sent)\n" +
                    "**level**              \ncheck the level of you or another user\n" +
                    "**stats**              \nthe bot's stats\n\n"
            , inline=False)

            embed.add_field(name="image commands",
            value=  "**cool_image (ci)**         \nrandomly generate an image\n" +
                    "**gif**                \ngif generation test\n" +
                    "**quote_image**        \ncreate a nice image with your quote\n" +
                    "**sign**               \ngenerate mario 64 sign image\n" +
                    "**petpet**             \npet a user's pfp or custom emoji\n\n" 
            , inline=False)

            embed.add_field(name="economy commands",
            value=  "**balance**            \ncheck your balance\n" +
                    "**buy**                \nbuy an item\n" +
                    "**donate_cash**        \ngive some money to another user\n" +
                    "**donate_item**        \ngive an item to another user\n" +
                    "**inventory**          \ncheck your inventory\n" +
                    "**rob**                \nrob someone :flushed:\n" +
                    "**shop**               \nopens the shop\n" +
                    "**stop**               \nquickly restart the bot\n" +
                    "**toss**               \nthrow away an item\n\n" 
            , inline=False)

            embed.set_footer(text="Please read http://deatg.com/bot_terms before using this bot.")

            await message.channel.send(embed=embed)

        #slur moment
        try:
            if message.guild.id == 910352456431566898 and not message.author.bot:
                for word in Lists.slur_list:
                    if word in message.clean_content.lower().replace(" ", ""):
                        for user_id in Common.mod_ids:
                            await self.client.get_user(user_id).send(f"slur alert!\n{message.author} said {message.clean_content}\nhttps://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
        except:
            pass
        


        ##random reply to old msg --this doesn't really work
        #if random.randint(0, 7600) < 6:
        #    async for msg in message.channel.history(limit=10000):
        #        if random.randint(0, 9000) < 5:
        #            if msg.channel.id != 838451092739457084 and msg.channel.id != 471178465375158273:
        #                message_to_send = await Listeners.decide_message(self, message)
#
        #                if "quoting" in message.channel.name:
        #                    await message.channel.send(f'"{message_to_send}"')
        #                    return
        #                else:
        #                    await message.channel.send(message_to_send)
        #        break
#
#
        #    return

        #status change
        if random.randint(0, 1000) < 10:
            statusType = random.randint(2, 18)

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

            if statusType == 16:
                await self.client.change_presence(status=discord.Status.online, activity=discord.Activity(type=5, name=f"the {randint(4, 10)}th annual {gamePlaying} tournament"))
            if statusType == 17:
                await self.client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=5, name=f"the {randint(4, 10)}th annual {gamePlaying} tournament"))
            if statusType == 18:
                await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=5, name=f"the {randint(4, 10)}th annual {gamePlaying} tournament"))

            if statusType == 19:
                await self.client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.custom, name=random.choice(Lists.messages)))
            if statusType == 20:
                await self.client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.custom, name=random.choice(Lists.messages)))
            if statusType == 21:
                await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.custom, name=random.choice(Lists.messages)))

            if statusType == 22:
                await self.client.change_presence(status=discord.Status.invisible)

        if random.randint(0, 39000) < 10 and not (message.channel.id in Common.every_word_channel_ids):
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
            try:
                img.paste(avatar, (180, 110), avatar)
            except:
                img.paste(avatar, (180, 110))
            img.save("quote.png") 

            await message.reply(file = discord.File("quote.png"))

        await self.client.process_commands(message)






def setup(client):
    client.add_cog(Listeners(client))