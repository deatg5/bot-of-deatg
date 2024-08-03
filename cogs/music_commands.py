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

    async def ensure_voice_state(self, ctx):
        """Ensure the bot's voice state is consistent with reality."""
        if ctx.guild.id in self.voice_clients:
            voice_client = self.voice_clients[ctx.guild.id]
            if not voice_client.is_connected():
                del self.voice_clients[ctx.guild.id]
            elif voice_client.channel != ctx.author.voice.channel:
                await voice_client.move_to(ctx.author.voice.channel)

    @commands.slash_command(contexts={discord.InteractionContextType.private_channel}, integration_types={discord.IntegrationType.user_install}, name="join", description="join voice chanel :dove:")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.respond("you is not in a voice channel!!!")
            return
        await self.ensure_voice_state(ctx)

        voice_channel = ctx.author.voice.channel
        if ctx.guild.id in self.voice_clients:
            await self.voice_clients[ctx.guild.id].move_to(voice_channel)
        else:
            self.voice_clients[ctx.guild.id] = await voice_channel.connect()
        await ctx.respond(f"joined {voice_channel.name} :3")

    @commands.slash_command(contexts={discord.InteractionContextType.private_channel}, integration_types={discord.IntegrationType.user_install}, name="leave", description="get OUT of the voice channel")
    async def leave(self, ctx):
        await self.ensure_voice_state(ctx)
        if ctx.guild.id in self.voice_clients:
            await self.voice_clients[ctx.guild.id].disconnect()
            del self.voice_clients[ctx.guild.id]
            await ctx.respond("bye bye..")
        else:
            await ctx.respond("ERROUR: i can't leave something i'm not in !!!!")

    @commands.slash_command(contexts={discord.InteractionContextType.private_channel}, integration_types={discord.IntegrationType.user_install}, name="tts", description="make bot of deatg speak!")
    async def tts(self, ctx, *, text, language="en", is_slow=False):
        await self.ensure_voice_state(ctx)
        if ctx.guild.id not in self.voice_clients:
            await ctx.respond("this command is for playing tts audio in voice channels :3")
            return
        tts = gtts.gTTS(text, slow=is_slow, lang=language)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        self.voice_clients[ctx.guild.id].play(discord.FFmpegPCMAudio(fp, pipe=True))
        await ctx.respond("i speak!!", ephemeral=True)
        
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member == self.client.user:
            if after.channel is None:
                guild_id = before.channel.guild.id
                if guild_id in self.voice_clients:
                    del self.voice_clients[guild_id]
            elif before.channel != after.channel:
                guild_id = after.channel.guild.id
                self.voice_clients[guild_id] = member.guild.voice_client



def setup(client):
    client.add_cog(MusicCommands(client))