import discord
from discord.ext import commands
import random
from discord.utils import get
import youtube_dl
import os

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
    
    @commands.command(pass_context=True, brief="join voice channel")
    async def join(self, ctx):
        await Common.log(self, f'joined voice', ctx)
        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("NOT IN CHANNE;L")
            return
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        await voice.disconnect()
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        await ctx.send(f"time to play some epic tunes in {channel}")
        Common.log(self, f'joined {channel}', ctx)

    @commands.command(pass_context=True, brief="bot leave voice")
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f"oof i'm goned from {channel}")
            Common.log(self, f'left {channel}', ctx)
        else:
            await ctx.send("already left lmao")

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



    @commands.command(pass_context=True, brief=";play [YouTube url or search term]")
    async def play(self, ctx, *url: str):
        if "index" in url:
            await ctx.send("Sorry, but you can't use a playlist link.")
            return
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'leave' command")
            return
        await ctx.send("Getting audio from YouTube... this may take a long time (and maybe even crash the entire bot)")
        await Common.log(self, f'played {str(url)}', ctx)
        print("Someone wants to play music let me get that ready for them...")
        voice = get(self.client.voice_clients, guild=ctx.guild)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
            except:
                search_term = " ".join(url[:])
                ydl.extract_info(f"ytsearch:{search_term}", download=True)['entries'][0]
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, 'song.mp3')
        try:
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
        except:
            channel = ctx.message.author.voice.channel
            voice = get(self.client.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                await voice.disconnect()
            channel = ctx.message.author.voice.channel
            voice = get(self.client.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
            await voice.disconnect()
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
        voice.volume = 100
        voice.is_playing()
    
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