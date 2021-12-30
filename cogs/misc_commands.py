import discord
from discord.ext import commands
from discord.ext.commands.core import Command

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

    #@commands.command(brief="DO NOTTTTTTTTTT")
    #async def infinite_spam_everyone(self, ctx):
    #    while True:
    #        await ctx.send(f'@everyone {Common.random_message(self)}')
    #        Common.log(self, '**infinite_spam_everyone is happening be scared**', ctx)



    #@commands.command()
    #async def getinvites(self, ctx):
    #    if ctx.author.id == Common.deatg_id or ctx.author.id == 573285573968527402:
    #        for guild in self.client.guilds:
    #            try:
    #                for invite in await guild.invites():
    #                    await ctx.send(str(invite))
    #            except:
    #                await ctx.send("errpr")
    #    else:
    #        await ctx.send('you not deatg :skull:')

def setup(client):
    client.add_cog(MiscCommands(client))