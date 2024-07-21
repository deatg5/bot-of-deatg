import discord
from discord.ext import commands
from discord.utils import get
import gtts
import io

from cogs.common import Common
from cogs.lists import Lists

class MusicCommands(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.voice_clients = {}

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You is not in a voice channel!!!")
            return
        voice_channel = ctx.author.voice.channel
        if ctx.guild.id in self.voice_clients:
            await self.voice_clients[ctx.guild.id].move_to(voice_channel)
        else:
            self.voice_clients[ctx.guild.id] = await voice_channel.connect()
        await ctx.send(f"joined {voice_channel.name} :3")

    @commands.command()
    async def leave(self, ctx):
        if ctx.guild.id in self.voice_clients:
            await self.voice_clients[ctx.guild.id].disconnect()
            del self.voice_clients[ctx.guild.id]
            await ctx.send("bye bye..")
        else:
            await ctx.send("ERROUR: i can't leave something i'm not in !!!!")

    @commands.command()
    async def tts(self, ctx, *, text):
        if ctx.guild.id not in self.voice_clients:
            await ctx.send("this command is for playing tts audio in voice channels :3")
            return
        tts = gtts.gTTS(text)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        self.voice_clients[ctx.guild.id].play(discord.FFmpegPCMAudio(fp, pipe=True))

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member == self.client.user and after.channel is None:
            guild_id = before.channel.guild.id
            if guild_id in self.voice_clients:
                del self.voice_clients[guild_id]



def setup(client):
    client.add_cog(MusicCommands(client))