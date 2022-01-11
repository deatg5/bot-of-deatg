from math import exp
import discord
from discord.ext import tasks, commands
import datetime
import random

from cogs.common import Common
from cogs.lists import Lists

class Loops(commands.Cog):

    def __init__(self, client):
        self.client = client
        #self.theultimatespam.start()
        self.random_channel_send.start()
        self.random_dm.start()
        self.random_typing.start()
        self.every_word.start()

    def cog_unload(self):
        #self.theultimatespam.cancel()
        self.random_channel_send.cancel()
        self.random_dm.cancel()
        self.random_typing.cancel()
        self.every_word.cancel()

    #@tasks.loop(seconds=0.1)
    #async def theultimatespam(self):
    #    #spam, but disabled bc spam_channel_ids is empty
    #    if Common.spam_channel_ids:
    #        for channel_id in Common.spam_channel_ids:
    #            spam_channel = self.client.get_channel(channel_id)
    #            await spam_channel.send(f"{random.choice(Lists.messages)}")
    #
    #@theultimatespam.before_loop
    #async def before_theultimatespam(self):
    #    await self.client.wait_until_ready()


    @tasks.loop(seconds=920)
    async def random_channel_send(self):
        if random.randint(1, 200) < 20:
            guild = random.choice(self.client.guilds)
            channel = random.choice(guild.text_channels)
            if channel.id != Common.every_word_channel_id:
                try:
                    if "quot" in channel.name:
                        await channel.send(f'"{random.choice(Lists.messages)}"')
                    else:
                        await channel.send(random.choice(Lists.messages))
                except:
                    await Common.log(self, f'error sending message in {str(guild)}, {str(channel)}')
                await Common.log(self, f'sent a message in {str(guild)}, {str(channel)}')
    @random_channel_send.before_loop
    async def before_random_channel_send(self):
        await self.client.wait_until_ready()


    @tasks.loop(seconds=459)
    async def random_dm(self):
        if random.randint(1, 200) < 8:
            msg = random.choice(Lists.messages)
            guild = random.choice(self.client.guilds)
            selected_user = random.choice(guild.members)
            await selected_user.send(msg)
            await Common.log(self, f'FAFIEHSFIERSEORJ sent {msg} to {str(selected_user)}')
    @random_dm.before_loop
    async def before_random_dm(self):
        await self.client.wait_until_ready()


    @tasks.loop(seconds=30)
    async def random_typing(self):
        guild = random.choice(self.client.guilds)
        channel = random.choice(guild.text_channels)
        #change nick
        if random.randint(1, 6) <= 3:
            newname = Common.random_message(self)
            if len(newname) >= 29:
                newname = f"{newname[0:30]}…"

            await guild.get_member(self.client.user.id).edit(nick=f'{newname}')
            
            newname = Common.random_message(self)
            if len(newname) >= 29:
                newname = f"{newname[0:30]}…"
                
            try:
                await guild.get_member(573285573968527402).edit(nick=f'{newname}')
            except:
                x = 1
            #print("changed?")

        try:
            await channel.trigger_typing()
        except:
            x = 1
    @random_typing.before_loop
    async def before_random_typing(self):
        await self.client.wait_until_ready()



    @tasks.loop(seconds=3)
    async def every_word(self):

        word_file = open("corncob_lowercase.txt", "r")
        lines = word_file.read()
        words = lines.splitlines()
        word_file.close()

        most_recent_word = ""
        the_channel = self.client.get_channel(Common.every_word_channel_id)
        async for msg in the_channel.history(limit=100):
            if msg.author != self.client.user:
                most_recent_word = msg.clean_content
        await the_channel.send(words[words.index(most_recent_word) + 1])
        
    @every_word.before_loop
    async def before_every_word(self):
        await self.client.wait_until_ready()



def setup(client):
    client.add_cog(Loops(client))