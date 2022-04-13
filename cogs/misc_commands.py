import string
import discord
from discord.ext import commands
from discord.ext.commands.core import Command
import inspect
from datetime import date, datetime

from cogs.common import Common

class MiscCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def typing(self, ctx):
        await ctx.trigger_typing()

    #@commands.command(brief="spam @minecraftman69")
    #async def infinite_spam_minecraftman(self, ctx):
    #    while True:
    #        await ctx.send(f'<@745827166058578000> {Common.random_message(self)}')
    #        await Common.log(self, 'started infinite spam minecraftman', ctx)


    #@commands.command(brief="spam @deatg")
    #async def infinite_spam_deatg(self, ctx):
    #    while True:
    #        await ctx.send(f'<@822658667845386240> {Common.random_message(self)}')
    #        await Common.log(self, 'started infinite spam deatg', ctx)

    @commands.command(brief=";spam [message] 10 times")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def spam(self, ctx, *message):
        message = " ".join(message[:])
        for i in range(10):
            async with ctx.typing():
                if "<@900139807181770772>" not in message:
                    await ctx.send(message)
        #await Common.log(self, f'Spammed {message} 10 times', ctx)

    @commands.command(brief="DO NOTTTTTTTTTT")
    async def infinite_spam_everyone(self, ctx):
        if ctx.guild.id in Common.spammable_servers:
            while True:
                await ctx.send(f'@everyone {Common.random_message(self)}')
                Common.log(self, '**infinite_spam_everyone is happening be scared**', ctx)
        else:
            await ctx.send("this command can only be used in certain servers")


    #@commands.command()
    #async def test_join(self, ctx):
    

    @commands.command()
    async def change_all_nicknames(self, ctx, server_id : int):
        if ctx.author.id == Common.deatg_id:
            the_server = self.client.get_guild(server_id)
            for user in the_server.members:
                newname = Common.random_message(self)
                if len(newname) >= 30:
                    newname = f"{newname[0:30]}…"
                try:
                    await user.edit(nick=f'{newname}')
                except:
                    aa = 3

    @commands.command()
    async def reset_all_nicknames(self, ctx, server_id : int):
        if ctx.author.id == Common.deatg_id:
            the_server = self.client.get_guild(server_id)
            for user in the_server.members:
                try:
                    await user.edit(nick=f'{str(user.name)}')
                except:
                    aa = 3

    @commands.command()
    async def change_all_nicknames2(self, ctx, server_id : int, newname):
        if ctx.author.id == Common.deatg_id:
            the_server = self.client.get_guild(server_id)
            for user in the_server.members:
                if len(newname) >= 30:
                    newname = f"{newname[0:30]}…"
                try:
                    await user.edit(nick=f'{newname}')
                except:
                    aa = 3


    @commands.command()
    async def matt(self, ctx):
        await ctx.send("oh god why am i in that server")

    @commands.command()
    async def getinvites(self, ctx):
        if ctx.author.id == Common.deatg_id or ctx.author.id == 573285573968527402:
            for guild in self.client.guilds:
                try:
                    for invite in await guild.invites():
                        await ctx.send(str(invite))
                        break
                except:
                    await ctx.send(f"{guild.name} errpr")
        else:
            await ctx.send('you not deatg :skull:')

def setup(client):
    client.add_cog(MiscCommands(client))