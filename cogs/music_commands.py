import discord
from discord.ext import commands
import random
from discord.utils import get
import youtube_dl
import os
from gtts import gTTS
import asyncio

from cogs.common import Common
from cogs.lists import Lists

class MusicCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '96',
        }],
    }   

    voice_clients = {}
    
    @commands.slash_command(name="join", description="join voice channel")
    async def join(self, ctx):
        voice_client = await ctx.author.voice.channel.connect()
        self.voice_clients[voice_client.guild.id] = voice_client


    @commands.slash_command(name="tts", description="Generate TTS audio from text and play it in a voice channel.")
    async def tts(self, ctx, text: str):
        if ctx.author.voice is None:
            await ctx.send("You must be in a voice channel to use this command.")
            return
        
        voice_client = None

        if not self.voice_clients[ctx.guild.id]:
            voice_client = await ctx.author.voice.channel.connect()
            self.voice_clients[voice_client.guild.id] = voice_client
        else:
            voice_client = self.voice_clients[ctx.guild.id]

        tts = gTTS(text=text, lang='en')
        tts.save("tts.mp3")

        voice_client.play(discord.FFmpegPCMAudio("tts.mp3"))

        while voice_client.is_playing():
            await asyncio.sleep(1)

            
    @commands.slash_command(name="leave", description="bot leave voice channel")
    async def leave(self, ctx):
        await ctx.author.voice.channel.disconnect()
        self.voice_clients[ctx.guild.id] = None
        

    #@commands.command(pass_context=True, brief="stop the currently playing music")
    #async def rejoin(self, ctx):
    #    channel = ctx.message.author.voice.channel
    #    voice = get(self.client.voice_clients, guild=ctx.guild)
    #    if voice and voice.is_connected():
    #        await voice.disconnect()
    #    channel = ctx.message.author.voice.channel
    #    voice = get(self.client.voice_clients, guild=ctx.guild)
    #    if voice and voice.is_connected():
    #        await voice.move_to(channel)
    #    else:
    #        voice = await channel.connect()
    #    await voice.disconnect()
    #    if voice and voice.is_connected():
    #        await voice.move_to(channel)
    #    else:
    #        voice = await channel.connect()



    #@commands.command(pass_context=True, brief=";play [YouTube url or search term]")
    #async def play(self, ctx, *url: str):
    #    if "index" in url:
    #        await ctx.send("Sorry, but you can't use a playlist link.")
    #        return
    #    song_there = os.path.isfile("song.mp3")
    #    try:
    #        if song_there:
    #            os.remove("song.mp3")
    #    except PermissionError:
    #        await ctx.send("Wait for the current playing music to end or use the 'leave' command")
    #        return
    #    await ctx.send("Getting audio from YouTube... this may take a long time (and maybe even crash the entire bot)")
    #    await Common.log(self, f'played {str(url)}', ctx)
    #    print("Someone wants to play music let me get that ready for them...")
    #    voice = get(self.client.voice_clients, guild=ctx.guild)
    #    ydl_opts = {
    #        'format': 'bestaudio/best',
    #        'postprocessors': [{
    #            'key': 'FFmpegExtractAudio',
    #            'preferredcodec': 'mp3',
    #            'preferredquality': '192',
    #        }],
    #    }
    #    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #        try:
    #            ydl.download([url])
    #        except:
    #            search_term = " ".join(url[:])
    #            ydl.extract_info(f"ytsearch:{search_term}", download=True)['entries'][0]
    #    for file in os.listdir("./"):
    #        if file.endswith(".mp3"):
    #            os.rename(file, 'song.mp3')
    #    try:
    #        voice.play(discord.FFmpegPCMAudio("song.mp3"))
    #    except:
    #        channel = ctx.message.author.voice.channel
    #        voice = get(self.client.voice_clients, guild=ctx.guild)
    #        if voice and voice.is_connected():
    #            await voice.disconnect()
    #        channel = ctx.message.author.voice.channel
    #        voice = get(self.client.voice_clients, guild=ctx.guild)
    #        if voice and voice.is_connected():
    #            await voice.move_to(channel)
    #        else:
    #            voice = await channel.connect()
    #        await voice.disconnect()
    #        if voice and voice.is_connected():
    #            await voice.move_to(channel)
    #        else:
    #            voice = await channel.connect()
    #        voice.play(discord.FFmpegPCMAudio("song.mp3"))
    #    voice.volume = 100
    #    voice.is_playing()

    #@commands.slash_command(name="play", description="play tts")
    #async def play(self, ctx):
    #    channel = ctx.author.voice.channel
    #    vc = await channel.connect()
    #    vc.play(discord.FFmpegPCMAudio('C:\\Users\\Nick\\Documents\\bot_of_deatg\\PYCORD\\tts.mp3'))

    
    #@commands.command(pass_context=True, brief="plays a totally random song from youtube")
    #async def playrandom(self, ctx):
    #    url = random.choice(Lists.youtube_song_list)
    #    song_there = os.path.isfile("song.mp3")
    #    try:
    #        if song_there:
    #            os.remove("song.mp3")
    #    except PermissionError:
    #        await ctx.send("Wait for the current playing music to end or use the 'leave' command")
    #        return
    #    await ctx.send("Getting audio from YouTube... this may take a long time (and maybe even crash the entire bot)")
    #    Common.log(self, f'played {str(url)} from Updated', ctx)
    #    print("Someone wants to play music let me get that ready for them...")
    #    voice = get(self.client.voice_clients, guild=ctx.guild)
    #    ydl_opts = {
    #        'format': 'bestaudio/best',
    #        'postprocessors': [{
    #            'key': 'FFmpegExtractAudio',
    #            'preferredcodec': 'mp3',
    #            'preferredquality': '192',
    #        }],
    #    }
    #    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #        ydl.download([url])
    #    for file in os.listdir("./"):
    #        if file.endswith(".mp3"):
    #            os.rename(file, 'song.mp3')
    #    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    #    voice.volume = 100
    #    voice.is_playing()

def setup(client):
    client.add_cog(MusicCommands(client))