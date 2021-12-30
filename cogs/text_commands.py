import discord
from discord.ext import commands
import random
from random import randint
import textwrap

from discord.ext.commands.core import Command

from cogs.common import Common
from cogs.lists import Lists
from cogs.sentence_generation import SentenceGeneration

class TextCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief=";spam [message]")
    async def spam(self, ctx, *message):
        message = " ".join(message[:])
        for i in range(20):
            async with ctx.typing():
                await ctx.send(message)
        await Common.log(self, f'Spammed {message} 20 times', ctx)

    @commands.command(brief="guesses the pokemon sent by pokemon discord bot")
    async def mon(self, ctx):
        mon = random.choice(Lists.pokemon)
        async with ctx.typing():
            await ctx.send(f'The Pokémon is: {mon}')
        await Common.log(self, f'mon command sent: {mon}', ctx)

    @commands.command(brief="sends invite link")
    async def invite(self, ctx):
        async with ctx.typing():
            await ctx.send('https://discord.com/api/oauth2/authorize?client_id=925854592154095667&permissions=137643809857&scope=bot')
        await Common.log(self, f'invite link sent', ctx)
    
    #@commands.command(brief="DO NOT")
    #async def infinite_pain(self, ctx):
    #    await Common.log(self, f'infinite pain started o HEKC')
    #    while True:
    #        async with ctx.typing():
    #            await ctx.send(f'{Common.random_message(self)}')

    @commands.command(aliases=['mc'], brief="random minecraft item, block, or entity")
    async def minecraft(self, ctx, amount=1):
        for i in range(amount):
            async with ctx.typing():
                await ctx.send(f'{random.choice(Lists.item)}')


    #@commands.command(brief="??????????")
    #async def demfex(self, ctx):
    #    async with ctx.typing():
    #        await ctx.send(SentenceGeneration.generate_demfex_quote(self))
    #    await Common.log(self, 'demfex generated', ctx)

    @commands.command(brief="sends a random emoji from a server the bot is in")
    async def emoji(self, ctx):
        selected_emoji = random.choice(self.client.emojis)
        async with ctx.typing():
            await ctx.send(selected_emoji)
        await Common.log(self, f'sent {selected_emoji}', ctx)

    @commands.command(brief="sends some random regular emojis (default is 3)")
    async def emojis(self, ctx, count = 3):
        emoji = ""
        for i in range(count):
            emoji += random.choice(Lists.all_emoji)
        async with ctx.typing():
            await ctx.send(emoji)
        await Common.log(self, f'sent {emoji}', ctx)

    
    @commands.command(brief="adds an emoji between each of your words")
    async def emojipasta(self, ctx, *message):
        message = " ".join(message[:])
        try:
            async with ctx.typing():
                await ctx.send(Common.random_emoji_insert(self, message))
        except:
            await ctx.send("message too long :grimacing:")
        await Common.log(self, f'sent {message}', ctx)



    @commands.command(brief="send info about the current server")
    async def server_information(self, ctx):
        server_info = ''
        server_info += (f'afk_channel: {ctx.guild.afk_channel}, ')
        server_info += (f'afk_timeout: {ctx.guild.afk_timeout}, ')
        server_info += (f'banner: {ctx.guild.banner}, ')
        server_info += (f'banner_url: {ctx.guild.banner_url}, ')
        server_info += (f'bitrate_limit: {ctx.guild.bitrate_limit}, ')
        server_info += (f'chunked: {ctx.guild.chunked}, ')
        server_info += (f'created_at: {ctx.guild.created_at}, ')
        server_info += (f'default_notifications: {ctx.guild.default_notifications}, ')
        server_info += (f'description: {ctx.guild.description}, ')
        server_info += (f'discovery_splash: {ctx.guild.discovery_splash}, ')
        server_info += (f'discovery_splash_url: {ctx.guild.discovery_splash_url}, ')
        server_info += (f'emoji_limit: {ctx.guild.emoji_limit}, ')
        server_info += (f'explicit_content_filter: {ctx.guild.explicit_content_filter}, ')
        server_info += (f'features: {ctx.guild.features}, ')
        server_info += (f'filesize_limit: {ctx.guild.filesize_limit}, ')
        server_info += (f'icon: {ctx.guild.icon}, ')
        server_info += (f'icon_url: {ctx.guild.icon_url}, ')
        server_info += (f'id: {ctx.guild.id}, ')
        server_info += (f'large: {ctx.guild.large}, ')
        server_info += (f'max_members: {ctx.guild.max_members}, ')
        server_info += (f'max_presences: {ctx.guild.max_presences}, ')
        server_info += (f'max_video_channel_users: {ctx.guild.max_video_channel_users}, ')
        server_info += (f'me: {ctx.guild.me}, ')
        server_info += (f'member_count: {ctx.guild.member_count}, ')
        #server_info += (f'members: {ctx.guild.members}, ')
        server_info += (f'mfa_level: {ctx.guild.mfa_level}, ')
        server_info += (f'name: {ctx.guild.name}, ')
        server_info += (f'owner: {ctx.guild.owner}, ')
        server_info += (f'owner_id: {ctx.guild.owner_id}, ')
        server_info += (f'preferred_locale: {ctx.guild.preferred_locale}, ')
        server_info += (f'premium_subscription_count: {ctx.guild.premium_subscription_count}, ')
        server_info += (f'premium_tier: {ctx.guild.premium_tier}, ')
        server_info += (f'public_updates_channel: {ctx.guild.public_updates_channel}, ')
        server_info += (f'region: {ctx.guild.region}, ')
        #server_info += (f'roles: {ctx.guild.roles}, ')
        server_info += (f'rules_channel: {ctx.guild.rules_channel}, ')
        server_info += (f'shard_id: {ctx.guild.shard_id}, ')
        server_info += (f'splash: {ctx.guild.splash}, ')
        server_info += (f'splash_url: {ctx.guild.splash_url}, ')
        server_info += (f'system_channel: {ctx.guild.system_channel}, ')
        server_info += (f'system_channel_flags: {ctx.guild.system_channel_flags}, ')
        server_info += (f'unavailable: {ctx.guild.unavailable}, ')
        server_info += (f'verification_level: {ctx.guild.verification_level}, ')
        server_info += (f'voice_client: {ctx.guild.voice_client} ') 
        for line in textwrap.wrap(server_info, 2000):
            async with ctx.typing():
                await ctx.send(line)
        await Common.log(self, 'server info sent', ctx)

    @commands.command(brief="gets channels")
    async def getchannels(self, ctx):
        if ctx.author.id == Common.deatg_id:
            channels = ''
            for guild in self.client.guilds:
                channels += f'{guild}:\n'
                for channel in guild.channels:
                    channels += f'{channel}, '
            for line in textwrap.wrap(channels, 2000):
                async with ctx.typing():
                    await ctx.send(line)
        else:
            await ctx.send('you not deatg :skull:')

    @commands.command(brief="gets servers")
    async def getservers(self, ctx):
        servers = ''
        await ctx.send(f"If i had a dollar for every server bot of deatg is in, i'd have like, {len(self.client.guilds)} dollars.")
        for guild in self.client.guilds:
            servers += f'{guild}, '
        for line in textwrap.wrap(servers, 2000):
            async with ctx.typing():
                await ctx.send(line)

    @commands.command()
    async def stats(self, ctx):
        await ctx.send(f'server count: {len(self.client.guilds)}')
        ch_list = []
        u_list = []
        for guild in self.client.guilds:
            for channel in guild.channels:
                ch_list.append(channel)
            for user in guild.members:
                u_list.append(user)

        await ctx.send(f'channel count: {len(ch_list)}')
        await ctx.send(f'user count: {len(u_list)}')
        await ctx.send(f'emoji count: {len(self.client.emojis)}')
        await ctx.send(f'possible messages: {len(Lists.messages)}')
        #await ctx.send(f'this channel\'s message count: {len(m_list)}')

    @commands.command(aliases=['8ball'], brief="ask a question")
    async def eightball(self, ctx):
        answers = ["Yes","No","Maybe","Probably","Not","Absolutely","Definitely","Definitely not","50% chance","Very likely","Perhaps","はい","Never","Tomorrow","DO NOT","DO","No way",
        "ye","yes","no","yeah lol","Ask again","NO","YES","Try it","yep","false","true", "I'm sorry, but it's not gonna happen"]
        await ctx.send(random.choice(answers))
        await Common.log(self, '8ball command sent', ctx)

    @commands.command()
    async def ping(self, ctx):
        if randint(0, 200) < 190:
            await ctx.send(f"{round(self.client.latency * 1000)}ms. ")
        else:
            await ctx.send(f"{round(self.client.latency * 5963)} SCPM (snow cones per minute)")


    

    
    

        

def setup(client):
    client.add_cog(TextCommands(client))