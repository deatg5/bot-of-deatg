import discord
from discord.ext import commands
import random
import datetime

from cogs.lists import Lists

class Common(commands.Cog):

    def __init__(self, client):
        self.client = client

        
    deatg_id = 923313823195205645
    log_channel_ids = [838451092739457084]
    spam_channel_ids = []
    

    async def log(self, message, ctx = None):
        if ctx != None:
            print(f"{str(datetime.datetime.now())} {ctx.guild}, {ctx.channel},  {ctx.message.author}, {str(message)}")
        else:
            print(f"{str(datetime.datetime.now())}")
        #for channel_id in Common.log_channel_ids:
        #    log_channel = self.client.get_channel(channel_id)
        #    if ctx != None:
        #        await log_channel.send(f"{str(datetime.datetime.now())} {ctx.guild}, {ctx.channel},  {ctx.message.author}, {str(message)}")
        #    else:
        #        await log_channel.send(f"{str(datetime.datetime.now())} {str(message)}")
    
    def random_message(self):
        message_type = random.choice([Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, Lists.messages, 
                        Lists.item, Lists.item, Lists.item, Lists.item, Lists.item, 
                        Lists.songs,
                        Lists.splashes, 
                        Lists.pokemon, Lists.pokemon, 
                        Lists.games,
                        Lists.kanji,
                        Lists.hiragana])
        return random.choice(message_type)

    


    async def dynamic_message(self, message):
        members = message.guild.members
        selected_user = random.choice(members)
        selected_user = str(selected_user)
        selected_user = selected_user[:-5]

        #having a list of f strings with random.choice only chooses one message per bot start, so if it's called more than once between when the bot restarts, the message will be the same, thats why i have to make this painfully long if else statement
        #i left some f strings in the messages array because they wont appear often enough for anyone to notice (hopefully)
        #wait maybe theres an even better way to do this (there is)   well i'll change it later maybe
        message_type = random.randint(0, 12)
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
            temp_msg = random.choice(random.choice([Lists.item, Lists.funny_nouns, Lists.messages, Lists.tunesList, Lists.games, selected_user, selected_user, selected_user]))
            temp_msg2 = random.choice(random.choice([Lists.item, Lists.funny_nouns, Lists.messages, Lists.tunesList, Lists.games, selected_user, selected_user, selected_user]))
            return f"Zoom in on the {temp_msg2}, and you'll see: {temp_msg}"

        elif message_type == 11:
            return f"com.mojang.authlib.GameProfile@2f47cbcf[id=<null>,name={selected_user},properties=[],legacy=false] lost connection: Disconnected"

        elif message_type == 12:
            temp_kanji = ""
            for i in range(random.randint(3, 30)):
                temp_kanji += random.choice(Lists.kanji)
            return temp_kanji

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

    def random_style(self, message_content):
        styles = ["**", "*", "~~", "`", "||", "```"]
        selected_style = random.choice(styles)
        return f'{selected_style}{message_content}{selected_style}'

    def random_word_edit(self, message_content):
        word_to_replace = random.choice(message_content.split())
        word_to_add = random.choice(['[[Hyperlink Blocked]]', '[REDACTED]', '[REMOVED TO CONFORM WITH LOCAL AND INTERNATIONAL CENSORSHIP LAWS]', f'||{word_to_replace}||', f'*{word_to_replace}*', f'**{word_to_replace}**', f'~~{word_to_replace}~~', f'[{word_to_replace.capitalize()}]'])
        return message_content.replace(word_to_replace, word_to_add)

    def random_insert(self, message_content):
        index = random.randint(0, len(message_content))
        add_string = random.choice(['TAB'])
        return message_content[:index] + add_string + message_content[index:]

    def cutoff(self, message_content):
        index = random.randint(5, len(message_content))
        return f'{message_content[0:index]}-'
    
    def generate_fake_japanese_sentence(self):
        the_sentence = ""
        for i in range(random.randint(2, 70)):
            type = random.randint(1, 3)
            if type == 1 or type == 2:
                the_sentence += random.choice(Lists.hiragana)
            elif type == 3:
                the_sentence += random.choice(Lists.kanji)
        return the_sentence

    def fancy_letters(self, input_sentence):
        ret = ""
        selected_dict = Lists.fancy_text_4
        for letter in input_sentence.lower():
            try:
                ret += selected_dict[letter]
            except:
                ret += letter
        return ret





def setup(client):
    client.add_cog(Common(client))