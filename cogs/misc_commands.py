import random
from random import randint
import string
import discord
from discord.ext import commands
from discord.ext.commands.core import Command
import inspect
from datetime import date, datetime
import os
import json

from cogs.common import Common
from cogs.lists import Lists

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


    @commands.command(brief="cool1_bot_number_1_opp")
    async def cool1_bot_number_1_opp(self, ctx):
        async for msg in ctx.channel.history(limit = 1000):
            if "@cool1 bot" in msg.clean_content:
                await msg.delete()


    @commands.slash_command(contexts={discord.InteractionContextType.private_channel}, integration_types={discord.IntegrationType.user_install}, name="time", description="the current time according to bot of deatg")
    async def time(self, ctx):
        await ctx.respond(str(datetime.now()))



    


    #@commands.command()
    #async def test_join(self, ctx):


    '''
    @commands.command()
    async def server_to_json(self, ctx, server_id = None):
        if ctx.author.id != Common.deatg_id:
            await ctx.send("you not deatg :skul;:")
            return
        else:
            if server_id == None:
                server_id = ctx.guild.id
            the_server = self.client.get_guild(server_id)
            for channel in the_server.channels:
                #add
            for member in the_server.members:
                #add
            for role in the_server.roles:
                #add
    '''     

    

    @commands.command()
    async def change_all_nicknames(self, ctx, server_id : int):
        if ctx.author.id == Common.deatg_id:
            the_server = self.client.get_guild(server_id)
            for member in the_server.members:
                newname = Common.random_message(self)
                if len(newname) >= 30:
                    newname = f"{newname[0:30]}…"
                try:
                    await member.edit(nick=f'{newname}')
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

    @commands.command(breif="kick a user from the server!!! rah!!!!!!!!")

    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member, *, reason: str = None) -> None:
        if reason == None:
            reason = f"{random.choice(Lists.messages)}"
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                title="AAAAAAAHHHHHHHHHHHHHHHHHH",
                description="user has admin permissions.",
                color=Common.random_color()
            )
            await context.send(embed=embed)
        else:
            try:
                embed = discord.Embed(
                    title="user KICKED!!!!!!!!!",
                    description=f"**{member}** was kicked by **{context.author}**!",
                    color=Common.random_color()
                )
                embed.add_field(
                    name="reason:",
                    value=reason
                )
                try:
                    await member.send(
                        f"you were kicked from  {context.guild} by **{context.author}** !!\nreason: {reason}"
                    )
                except discord.Forbidden:
                    # Couldn't send a message in the private messages of the user
                    pass
                await member.kick(reason=reason)
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="AAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
                    description="an error occurred while trying to kick the user. make sure my role is above the role of the user you want to kick!! {random.choice(Lists.all_face_emoji)}",
                    color=Common.random_color()
                )
                await context.send(embed=embed)

    @commands.command(brief="change the nickname of a user in da server")
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, context, member: discord.Member, *, nickname: str = None) -> None:
        if nickname == None:
            nickname = f"{random.choice(Lists.messages)}"
        try:
            await member.edit(nick=nickname)
            embed = discord.Embed(
                title="changed nickname!",
                description=f"**{member}'s** new nickname is **{nickname}**!!! {random.choice(Lists.all_emoji)}",
                color=Common.random_color()
            )
            await context.send(embed=embed)
        except:
            embed = discord.Embed(
                title="AHHHHHHHHHHHHHHHHHHHHH",
                description="an error occurred while trying to change the nickname of the user. Make sure my role is above the role of the user you want to change the nickname.",
                color=Common.random_color()
            )
            await context.send(embed=embed)

    @commands.command(brief="bans a user from the server!!!!")
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member: discord.Member, *, reason: str = None) -> None:
        if reason == None:
            reason = f"{random.choice(Lists.messages)}"
        try:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    title="AAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHH",
                    description="user has admin permissions..",
                    color=Common.random_color()
                )
                await context.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="user beaned!",
                    description=f"**{member}** was beaned by **{context.author}**! {random.choice(Lists.all_face_emoji)} {random.choice(Lists.sentence_enders)}",
                    color=Common.random_color()
                )
                embed.add_field(
                    name="reason:",
                    value=reason
                )
                try:
                    await member.send(f"you were beaned from {context.guild} by **{context.author}**! {random.choice(Lists.all_face_emoji)}\nreason: {reason}")
                except discord.Forbidden:
                    # Couldn't send a message in the private messages of the user
                    pass
                await member.ban(reason=reason)
                await context.send(embed=embed)
        except:
            embed = discord.Embed(
                title="AAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
                description=f"an error occurred while trying to ban the user!!!!!!!!!!! make sure my role is above the role of the user you want to ban ok? {random.choice(Lists.sentence_enders)}",
                color=Common.random_color()
            )
            await context.send(embed=embed)

    @commands.command(brief="warns a user in the server :scream:")
    @commands.has_permissions(kick_members=True)
    async def warn(self, context, member: discord.Member, *, reason: str = None):
        if reason == None:
            reason = f"{random.choice(Lists.messages)}"
        embed = discord.Embed(
            title="user warned!!!1!!! :scream:",
            description=f"**{member}** was warned by **{context.author}**!",
            color=Common.random_color()
        )
        embed.add_field(
            name="Reason:",
            value=reason
        )
        await context.send(embed=embed)
        try:
            await member.send(f"you were warned by **{context.author}** in {context.guild}!!!\nreason: {reason}")
        except discord.Forbidden:
            # Couldn't send a message in the private messages of the user
            await context.send(f"{member.mention}, you were warned by **{context.author}**!\nReason: {reason}")


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