import discord
from discord.ext import commands
import io
import pyttsx3
import asyncio
import os

class VoiceCog(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.voice_clients = {}
        self.tts_engine = pyttsx3.init()
        self.setup_voice()

    def setup_voice(self):
        voices = self.tts_engine.getProperty('voices')
        sam_voice = next((voice for voice in voices if "sam" in voice.name.lower()), None)
        if sam_voice:
            self.tts_engine.setProperty('voice', sam_voice.id)
            print(f"Using voice: {sam_voice.name}")
        else:
            print("Microsoft Sam-like voice not found. Using default voice.")
        self.tts_engine.setProperty('rate', 150)
        self.tts_engine.setProperty('volume', 0.9)

    async def ensure_voice_state(self, ctx):
        if ctx.guild.id in self.voice_clients:
            voice_client = self.voice_clients[ctx.guild.id]
            if not voice_client.is_connected():
                del self.voice_clients[ctx.guild.id]
            elif voice_client.channel != ctx.author.voice.channel:
                await voice_client.move_to(ctx.author.voice.channel)

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You need to be in a voice channel to use this command.")
            return

        await self.ensure_voice_state(ctx)

        voice_channel = ctx.author.voice.channel
        if ctx.guild.id not in self.voice_clients:
            self.voice_clients[ctx.guild.id] = await voice_channel.connect()
            await ctx.send(f"Joined {voice_channel.name}")
        else:
            await ctx.send(f"Already in {self.voice_clients[ctx.guild.id].channel.name}")

    @commands.command()
    async def leave(self, ctx):
        await self.ensure_voice_state(ctx)

        if ctx.guild.id in self.voice_clients:
            await self.voice_clients[ctx.guild.id].disconnect()
            del self.voice_clients[ctx.guild.id]
            await ctx.send("Left the voice channel.")
        else:
            await ctx.send("I'm not in a voice channel.")

    @commands.command()
    async def tts(self, ctx, *, text):
        await self.ensure_voice_state(ctx)

        if ctx.guild.id not in self.voice_clients:
            await ctx.send("I'm not in a voice channel. Use the join command first.")
            return

        # Generate speech
        output_file = f"tts_{ctx.guild.id}.mp3"
        await asyncio.to_thread(self.generate_speech, text, output_file)

        # Play the generated speech
        audio_source = discord.FFmpegPCMAudio(output_file)
        self.voice_clients[ctx.guild.id].play(audio_source, after=lambda e: os.remove(output_file))

    def generate_speech(self, text, output_file):
        self.tts_engine.save_to_file(text, output_file)
        self.tts_engine.runAndWait()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member == self.bot.user:
            if after.channel is None:
                guild_id = before.channel.guild.id
                if guild_id in self.voice_clients:
                    del self.voice_clients[guild_id]
            elif before.channel != after.channel:
                guild_id = after.channel.guild.id
                self.voice_clients[guild_id] = member.guild.voice_client

def setup(client):
    client.add_cog(VoiceCog(client))