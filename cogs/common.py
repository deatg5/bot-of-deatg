from re import A
from typing import List
import discord
from discord.ext import commands
import random
from random import randint
import datetime

from cogs.lists import Lists

class Common(commands.Cog):

    def __init__(self, client):
        self.client = client

        
    deatg_id = 923313823195205645
    log_channel_ids = [930340703958097930]
    every_word_channel_ids = [930304637788102697] #,937978716418637864]
    mod_ids = [573285573968527402,923313823195205645]
    spammable_servers = [873380900434489374, 788195760209920020, 937466336739721236, 944005208948736010, 838578705226924082, 940685462383763507]
    bot_of_deatg_haters = [921621999120420864]
    spam_channel_ids = []
    
    async def send(self, ctx, message):
        if randint(0, 1000) <= 20:
            emb=discord.Embed(title=f"{random.choice(Lists.messages)}", color=Common.random_color())
            emb.add_field(name=f"{random.choice(Lists.messages)}", value=f"{message}")
            if randint(0, 1000) <= 50:
                await ctx.send(embed=emb, tts=True)
                return
            elif randint(0, 1000) <= 10:
                await ctx.send(embed=emb, delete_after = float(randint(2, 10)))
                return
            elif randint(0, 1000) <= 10:
                await ctx.send(embed=emb, tts=True, delete_after = float(randint(2, 10)))
                return
            else:
                await ctx.send(embed=emb)
                return
        elif randint(0, 1000) <= 50:
            await ctx.send(message, tts=True)
            return
        elif randint(0, 1000) <= 10:
            await ctx.send(message, delete_after = float(randint(2, 30)))
            return
        elif randint(0, 1000) <= 10:
            await ctx.send(message, tts=True, delete_after = float(randint(2, 30)))
            return
        else:
            await ctx.send(message)
            return

    async def log(self, message, ctx = None):
        if ctx != None:
            print(f"{str(datetime.datetime.now())} {ctx.guild}, {ctx.channel},  {ctx.message.author}, {str(message)}")
        else:
            print(f"{str(datetime.datetime.now())}")
            
        for channel_id in Common.log_channel_ids:
            log_channel = self.client.get_channel(channel_id)
            if ctx != None:
                #{str(datetime.datetime.now())}
                await log_channel.send(f"{ctx.guild}, {ctx.channel},  {ctx.message.author}, {str(message)}")
            else:
                await log_channel.send(f"{str(message)}")
    
    def random_message(self):
        message_type = random.choice([Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, 
                        Lists.item, Lists.item, Lists.item,
                        Lists.songs,
                        Lists.splashes, 
                        Lists.pokemon,
                        Lists.games,
                        Lists.kanji])
        return random.choice(message_type)

    


        

    
    def old_chatbot_message(self, long_edition = False):
        text_file = open("outputs.txt", "r")
        lines = text_file.read().split('FORNITE_FUNNY69')

        if long_edition:
            line = random.choice(lines)[:1999]
            return "".join(line[:])
        else:
            lines_to_return = random.randint(1, 3)
            lines_split_further = random.choice(lines).split('\n')
            start_index = random.randint(0, len(lines_split_further))
            ret = lines_split_further[start_index:start_index + lines_to_return]
            return "".join(ret[:])

    def chatbot_message(self):
        with open("outputs2.txt", "r") as funny:
            selected = random.choice(funny.readlines())
            return selected


    async def dynamic_message(self, message):
        members = message.guild.members
        selected_user = random.choice(members)
        selected_user_string = str(selected_user)
        selected_user_string = selected_user_string[:-5]

        selected_user2 = random.choice(members)
        selected_user2_string = str(selected_user)
        selected_user2_string = selected_user_string[:-5]

        selected_user3 = random.choice(members)
        selected_user3_string = str(selected_user)
        selected_user3_string = selected_user_string[:-5]

        #having a list of f strings with random.choice only chooses one message per bot start, so if it's called more than once between when the bot restarts, the message will be the same, thats why i have to make this painfully long if else statement
        #i left some f strings in the messages array because they wont appear often enough for anyone to notice (hopefully)
        #wait maybe theres an even better way to do this (there is)   well i'll change it later maybe
        message_type = random.randint(0, 20)
        if message_type == 0:
            random_reward = random.choice(random.choice([Lists.item, Lists.item, Lists.item, Lists.messages, Lists.funny_nouns]))
            return f"I Have A Dire Need\nBring Me:\nHemoglobin\nCompressed Air\nHarpoon\nMany Many Meats (Flavorful)\nButtor\nApe\nBring Me This And You Will Be Rewarded With The {random_reward}"

        elif message_type == 1:
            temp_msg = random.choice(Lists.messages)
            return f"Achievement unlocked: {temp_msg}"

        elif message_type == 2:
            temp_msg = random.choice(Lists.messages)
            return f"to recap: {temp_msg}"

        elif message_type == 3 or message_type == 4:
            temp_song = random.choice(random.choice([Lists.tunesList, Lists.memeSongs, Lists.memeSongs, Lists.memeSongs, Lists.memeSongs]))
            return f"({temp_song} plays)"

        elif message_type == 5 or message_type == 6:
            temp_game = random.choice(random.choice([Lists.games, Lists.joke_games]))
            return f"It is time to play {temp_game}"

        elif message_type == 7:
            temp_video = random.choice(Lists.videos)
            return f"It is time to watch {temp_video}"

        elif message_type == 8 or message_type == 9:
            temp_msg = random.choice(Lists.messages)
            return f"Next you'll say: \"{temp_msg}\""

        elif message_type == 10:
            temp_msg = random.choice(random.choice([Lists.item, Lists.funny_nouns, Lists.messages, Lists.tunesList, Lists.games, selected_user_string, selected_user_string, selected_user_string]))
            temp_msg2 = random.choice(random.choice([Lists.item, Lists.funny_nouns, Lists.messages, Lists.tunesList, Lists.games, selected_user_string, selected_user_string, selected_user_string]))
            return f"Zoom in on the {temp_msg2}, and you'll see: {temp_msg}"

        elif message_type == 11:
            return f"com.mojang.authlib.GameProfile@2f47cbcf[id=<null>,name={selected_user_string},properties=[],legacy=false] lost connection: Disconnected"

        elif message_type == 12:
            temp_kanji = ""
            for i in range(random.randint(3, 30)):
                temp_kanji += random.choice(Lists.kanji)
            return temp_kanji

        elif message_type == 13:
            return f"hi {selected_user_string}"

        elif message_type == 14:
            return f"hello {selected_user_string}"

        elif message_type == 15:
            return f"This bot was made by {selected_user_string}."

        elif message_type == 16:
            return f"{selected_user_string} hates me :sob:"

        elif message_type == 17:
            return f"{selected_user.mention} hi"

        elif message_type == 18:
            return f"{selected_user.mention} {random.choice(Lists.messages)}"

        elif message_type == 19:
            if selected_user.activity != None:
                return f"{selected_user.activity}"
            else:
                return "!rank"
        elif message_type == 20 or message_type == 21:
            return f"{message.author.name} my friend! I believe in your surgical tech skill on {random.choice(Lists.joke_games)}! You can even best the likes of {selected_user_string} and {selected_user2_string}! But be careful.. because {selected_user3_string} is right around the corner.."
            

        elif message_type == 20:
            return f"dear {selected_user_string}: {random.choice(Lists.messages)}"

    def minecraft_message(self, message):
        members = message.guild.members
        selected1 = random.choice(members)
        selected1 = str(selected1)
        selected1 = selected1[:-5]

        selected2 = random.choice(members)
        selected2 = str(selected2)
        selected2 = selected2[:-5]

        selected3 = random.choice(members)
        selected3 = str(selected3)
        selected3 = selected3[:-5]

        possible_messages = [f"{selected1} fell off a ladder", f"{selected1} fell off some vines", f"{selected1} fell off some weeping vines", f"{selected1} fell off some twisting vines", f"{selected1} fell off a scaffolding", f"{selected1} fell while climbing", f"{selected1} fell from a high place", f"{selected1} was doomed to fall", f"{selected1} was doomed to fall by {selected2}", f"{selected1} fell too far and was finished by {selected2}", f"{selected1} was struck by lightning", f"{selected1} was struck by lightning whilst fighting {selected2}", f"{selected1} went up in flames", f"{selected1} walked into fire whilst fighting {selected2}", f"{selected1} was burnt to a crisp whilst fighting {selected2}", f"{selected1} tried to swim in lava", f"{selected1} tried to swim in lava to escape {selected2}", f"{selected1} discovered the floor was lava", f"{selected1} walked into danger zone due to {selected2}", f"{selected1} suffocated in a wall", f"{selected1} suffocated in a wall whilst fighting {selected2}", f"{selected1} was squashed by {selected2}", f"{selected1} drowned", f"{selected1} drowned whilst trying to escape {selected2}", f"{selected1} starved to death whilst fighting {selected2}", f"{selected1} walked into a cactus whilst trying to escape {selected2}", f"{selected1} died", f"{selected1} died because of {selected2}", f"{selected1} blew up", f"{selected1} was blown up by {selected2}", f"{selected1} was blown up by {selected2} using {selected3}", f"{selected1} was killed by magic", f"{selected1} was killed by magic whilst trying to escape {selected2}", f"Actually, message was too long to deliver fully. Sorry! Here's stripped version: %s", f"{selected1} withered away", f"{selected1} withered away whilst fighting {selected2}", f"{selected1} was squashed by a falling anvil", f"{selected1} was squashed by a falling anvil whilst fighting {selected2}", f"{selected1} was squashed by a falling block", f"{selected1} was squashed by a falling block whilst fighting {selected2}", f"{selected1} was slain by {selected2}", f"{selected1} was slain by {selected2}", f"{selected1} was shot by {selected2}", f"{selected1} was fireballed by {selected2}", f"{selected1} was killed by {selected2} using magic", f"{selected1} was killed trying to hurt {selected2}", f"{selected1} was killed by {selected3} trying to hurt {selected2}", f"{selected1} was impaled by {selected2}", f"{selected1} hit the ground too hard", f"{selected1} hit the ground too hard whilst trying to escape {selected2}", f"{selected1} fell out of the world", f"{selected1} didn't want to live in the same world as {selected2}", f"{selected1} experienced kinetic energy", f"{selected1} experienced kinetic energy whilst trying to escape {selected2}", f"{selected1} was killed by {selected2}", f"Intentional Game Design", f"{selected1} was poked to death by a sweet berry bush", f"{selected1} was poked to death by a sweet berry bush whilst trying to escape {selected2}", f"{selected1} has made the advancement **{random.choice(Lists.messages)}**", f"{selected1} has made the advancement **{random.choice(Lists.messages)}**", f"{selected1} has made the advancement **{random.choice(Lists.messages)}**", f"{selected1} has made the advancement **{random.choice(Lists.messages)}**", f"{selected1} has completed the challenge **{random.choice(Lists.messages)}**", f"{selected1} has completed the challenge **{random.choice(Lists.messages)}**", f"{selected1} has made the advancement **{random.choice(Lists.messages)}**", f"{selected1} has made the advancement **{random.choice(Lists.messages)}**", f"{selected1} has made the advancement **{random.choice(Lists.messages)}**", f"{selected1} has made the advancement **{random.choice(Lists.messages)}**", f"{selected1} has completed the challenge **{random.choice(Lists.messages)}**", f"{selected1} has completed the challenge **{random.choice(Lists.messages)}**"]

        return random.choice(possible_messages)

    def random_color():
        #return ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        return random.randint(0, 0xffffff)

    def random_style(self, message_content):
        styles = ["**", "*", "~~", "`", "||", "```"]
        selected_style = random.choice(styles)
        return f'{selected_style}{message_content}{selected_style}'

    async def random_word_edit(self, message_content):
        word_to_replace = random.choice(message_content.split())
        word_to_add = random.choice(['[[Hyperlink Blocked]]', '[REDACTED]', '[REMOVED TO CONFORM WITH LOCAL AND INTERNATIONAL CENSORSHIP LAWS]', f'||{word_to_replace}||', f'*{word_to_replace}*', f'**{word_to_replace}**', f'~~{word_to_replace}~~', f'[{word_to_replace.capitalize()}]', f'{await Common.fancy_letters(self, word_to_replace)}'])
        return message_content.replace(word_to_replace, word_to_add)

    def random_insert(self, message_content):
        index = random.randint(0, len(message_content))
        add_string = random.choice(['TAB'])
        return message_content[:index] + add_string + message_content[index:]

    def random_emoji_insert(self, message_content):
        ret = ""
        new_emoji = random.choice(Lists.all_emoji)
        for char in str(message_content):
            if char == ' ':
                new_emoji = random.choice(Lists.all_emoji)
                ret += f" {new_emoji} "
            else:
                ret += char
        return ret

    def cutoff(self, message_content):
        index = random.randint(5, len(message_content))
        return f'{message_content[0:index]}-'

    def sentence_ender(self, message_content):
        return f"{message_content} {random.choice(Lists.sentence_enders)}"
    
    def generate_fake_japanese_sentence(self):
        the_sentence = ""
        for i in range(random.randint(2, 70)):
            type = random.randint(1, 3)
            if type == 1 or type == 2:
                the_sentence += random.choice(Lists.hiragana)
            elif type == 3:
                the_sentence += random.choice(Lists.kanji)
        return the_sentence

    async def fancy_letters(self, input_sentence, emojis = False):
        ret = ""
        selected_dict = None
        if not emojis:
            dict_type = random.randint(1, 4)
            if dict_type == 1 or dict_type == 2:
                selected_dict = Lists.fancy_text_spaced
            elif dict_type == 3:
                selected_dict = Lists.fancy_text_emo
            elif dict_type == 4:
                selected_dict = Lists.fancy_text_cursive

            for letter in input_sentence:
                try:
                    ret += selected_dict[letter]
                except:
                    ret += letter
            return ret
        else:
            for letter in input_sentence.upper():
                try:
                    ret += str(Lists.fancy_text_emoji[letter])
                except:
                    ret += letter
            return ret

    async def edit_recent_message(self, ctx, new_content):
        async for msg in ctx.history(limit = 1000):
            if msg.author == self.client.user:
                await msg.edit(content=str(new_content))
                break
        return
        





def setup(client):
    client.add_cog(Common(client))