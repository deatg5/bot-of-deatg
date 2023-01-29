import asyncio
from datetime import date, datetime
from lib2to3.pgen2 import token
from math import fabs
import math
import re
import string
import random
from random import randint
import discord
import os
from discord.ext import commands
import asyncpg
import textwrap
import sys
import inspect

from cogs.items import Items
from cogs.common import Common
from cogs.lists import Lists

token_lol = ""
database_address_lol = ""
database_password_lol = ""

#bye heroku
#DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
#DATABASE_ADDRESS = os.environ['DATABASE_ADDRESS']

#windows
if os.name == "nt":
    token_lol = open("M:\\the\\token.txt").readline()
    database_address_lol = open("M:\\the\\database_address.txt").readline()
    database_password_lol = open("M:\\the\\database_password.txt").readline()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix=commands.when_mentioned_or(';'), intents=intents, help_command=None)


#@client.command()
#async def load(ctx, extension):
#    client.load_extension(f'cogs.{extension}')

#@client.command()
#async def unload(ctx, extension):
#    client.unload_extension(f'cogs.{extension}')

@client.command(brief="quickly restart the bot (effectively stopping spam)")
async def stop(self):
    os.execv(sys.executable, ['python'] + sys.argv)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

        

#I wish there was a bot named the tag bot, if you @ someone and say tag after it (example: @deatg tag) then they are it, then they can then @ someone else, 
# this would repeat for awhile but after 5 minutes the person who is tagged doesn't get a point while everyone else who participated does.



@client.slash_command(name="mint", description="teest")
async def mint(ctx):
    await ctx.respond("HOLY SHIT!!!")

@client.command()
async def mint(ctx):
    await mint

#database stuff handled in main bot file, because i'm not sure if it will create multiple connections to the same database, or if i can access the pg_con variable from other cogs
#i'm totally fine with having all the database stuff here, i don't really care if it's not best practice.
async def create_db_pool():
        global pg_con 
        pg_con = await asyncpg.create_pool(host = database_address_lol, database ="egypt", user ="cleopatra", password = database_password_lol)

@client.command(aliases=["lb"], brief="the global bot of deatg leaderboard (1 xp = 1 message sent)")
async def leaderboard(ctx, amount=30):
    board = discord.Embed(title="leaderboard", description="1 XP is equal to 1 message sent\njust an ID means the user has been deleted or is inaccessable", color=Common.random_color())
    db_user = await pg_con.fetch(f"SELECT * FROM users ORDER BY xp DESC LIMIT {amount}")
    for index, user in enumerate(db_user):
        gamer = client.get_user(int(user['userid']))
        gamer = str(gamer)
        gamer_notag = gamer[:-5]
        if len(gamer_notag) == 0:
            board.add_field(name = f"{str(index + 1)} - {user['userid']}", value=f"level {str(user['level'])}, {str(user['xp'])} XP", inline = True)
            #board += f"{str(index + 1)} - {user['userid']} (username unavailable): level {str(user['level'])}, {str(user['xp'])} XP\n"
        else:
            board.add_field(name = f"{str(index + 1)} - {str(gamer)}", value=f"level {str(user['level'])}, {str(user['xp'])} XP", inline = True)
            #board += f"{str(index + 1)} - {str(gamer)}: level {str(user['level'])}, {str(user['xp'])} XP\n"

    await ctx.send(embed=board)

    # if len(board) > 2000:
    #     for line in textwrap.wrap(board, 2000, drop_whitespace=False, replace_whitespace=False):
    #         async with ctx.typing():
    #             await ctx.send(f'{line}')
    # else:
    #     await ctx.send(board)
@client.slash_command(name="leaderboard", description="the global bot of deatg leaderboard (1 xp = 1 message sent)")
async def leaderboard(ctx, amount=30):
    board = discord.Embed(title="leaderboard", description="1 XP is equal to 1 message sent\njust an ID means the user has been deleted or is inaccessable", color=Common.random_color())
    db_user = await pg_con.fetch(f"SELECT * FROM users ORDER BY xp DESC LIMIT {amount}")
    for index, user in enumerate(db_user):
        gamer = client.get_user(int(user['userid']))
        gamer = str(gamer)
        gamer_notag = gamer[:-5]
        if len(gamer_notag) == 0:
            board.add_field(name = f"{str(index + 1)} - {user['userid']}", value=f"level {str(user['level'])}, {str(user['xp'])} XP", inline = True)
        else:
            board.add_field(name = f"{str(index + 1)} - {str(gamer)}", value=f"level {str(user['level'])}, {str(user['xp'])} XP", inline = True)
    await ctx.respond(embed=board)


@client.command(brief="check the level of you or another user")
async def level(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    member_id = str(member.id)

    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    await ctx.send(f"{member.name}\nLevel: {db_user['level']}\nXP: {db_user['xp']}")

@client.slash_command(name="level", description="check the level of you or another user")
async def level(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    member_id = str(member.id)

    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    await ctx.respond(f"{member.name}\nLevel: {db_user['level']}\nXP: {db_user['xp']}")

    
#since i'll only be using this in code i won't take a member object, just the id
async def give_item(member_id, the_item, amount = 1):

    member_id = str(member_id)

    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    item_count = the_item + '_count'

    # if db_user[item_count] == None:
    #     await pg_con.execute("UPDATE users SET %s = %s WHERE userid = %s", (item_count, amount, member_id))
    # else:
    #     await pg_con.execute("UPDATE users SET %s = %s WHERE userid = %s", (item_count, db_user[item_count] + amount, member_id))
        
    if db_user[item_count] == None:
        await pg_con.execute(f"UPDATE users SET {item_count} = {amount} WHERE userid = '{member_id}'")
    else:
        await pg_con.execute(f"UPDATE users SET {item_count} = {db_user[item_count] + amount} WHERE userid = '{member_id}'")

async def give_cash(member_id, amount):

    member_id = str(member_id)

    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)
        
    if db_user['cash'] == None:
        await pg_con.execute(f"UPDATE users SET cash = $1 WHERE userid = $2", amount, member_id)
    else:
        await pg_con.execute(f"UPDATE users SET cash = $1 WHERE userid = $2", db_user['cash'] + amount, member_id)



@client.command(aliases=['inv'], brief="check your inventory")
async def inventory(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    member_id = str(member.id)

    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    
    embed=discord.Embed(title=f"{member.name}'s inventory", color=Common.random_color())

    for item in Items.item_list:
        if db_user[item['name'] + '_count'] != 0 and db_user[item['name'] + '_count'] != None:
            #inv += f"{item['friendly_name']}: {db_user[item['name'] + '_count']}\n"
            embed.add_field(name=item['friendly_name'], value=f"{item['emoji']} {db_user[item['name'] + '_count']}", inline=True)
    await ctx.send(embed=embed)

@client.slash_command(name="inventory", description="check your inventory")
async def inventory(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    member_id = str(member.id)
    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)
    embed=discord.Embed(title=f"{member.name}'s inventory", color=Common.random_color())
    for item in Items.item_list:
        if db_user[item['name'] + '_count'] != 0 and db_user[item['name'] + '_count'] != None:
            #inv += f"{item['friendly_name']}: {db_user[item['name'] + '_count']}\n"
            embed.add_field(name=item['friendly_name'], value=f"{item['emoji']} {db_user[item['name'] + '_count']}", inline=True)
    await ctx.respond(embed=embed)

@client.command(brief="opens the shop")
async def shop(ctx):
    
    embed=discord.Embed(title=f"the shop", description="use ;buy [item name] to buy something", color=Common.random_color())

    for item in Items.item_list:
        if (item['cost'] != 0):
            if item['heal_amount'] == 0 and item['damage'] == 0:
                embed.add_field(name=f"{item['emoji']} {item['friendly_name']} [{item['name']}]", value=f"${item['cost']}\n{item['description']}")
            elif item['heal_amount'] == 0:
                embed.add_field(name=f"{item['emoji']} {item['friendly_name']} [{item['name']}]", value=f"${item['cost']}\n{item['description']}\ndamage: {item['damage']}")
            elif item['damage'] == 0:
                embed.add_field(name=f"{item['emoji']} {item['friendly_name']} [{item['name']}]", value=f"${item['cost']}\n{item['description']}\nheal amount: {item['heal_amount']}")
            else:
                embed.add_field(name=f"{item['emoji']} {item['friendly_name']} [{item['name']}]", value=f"${item['cost']}\n{item['description']}\nheal amount: {item['heal_amount']}\ndamage: {item['damage']}")
    await ctx.send(embed=embed)

@client.slash_command(name="shop", description="opens the shop")
async def shop(ctx):
    
    embed=discord.Embed(title=f"the shop", description="use ;buy [item name] to buy something", color=Common.random_color())

    for item in Items.item_list:
        if (item['cost'] != 0):
            if item['heal_amount'] == 0 and item['damage'] == 0:
                embed.add_field(name=f"{item['emoji']} {item['friendly_name']} [{item['name']}]", value=f"${item['cost']}\n{item['description']}")
            elif item['heal_amount'] == 0:
                embed.add_field(name=f"{item['emoji']} {item['friendly_name']} [{item['name']}]", value=f"${item['cost']}\n{item['description']}\ndamage: {item['damage']}")
            elif item['damage'] == 0:
                embed.add_field(name=f"{item['emoji']} {item['friendly_name']} [{item['name']}]", value=f"${item['cost']}\n{item['description']}\nheal amount: {item['heal_amount']}")
            else:
                embed.add_field(name=f"{item['emoji']} {item['friendly_name']} [{item['name']}]", value=f"${item['cost']}\n{item['description']}\nheal amount: {item['heal_amount']}\ndamage: {item['damage']}")
    await ctx.respond(embed=embed)


#failed the daily
#@client.command(brief="open daily box")
#async def daily(ctx):
#
#    
#
#    member_id = str(ctx.author.id)
#    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)
#
#    if db_user['most_recent_daily'] == None:
#        the_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#        await pg_con.execute(f"UPDATE users SET most_recent_daily = {the_date} WHERE userid = '{member_id}'")
#    
#    most_recent_daily = db_user['most_recent_daily']
#    
#    if db_user['current_streak'] == None:
#        await pg_con.execute(f"UPDATE users SET current_streak = 0 WHERE userid = '{member_id}'")
#
#    streak = db_user['current_streak']
#
#
#    ready_again_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + datetime.hour(24)
#        
#    if (datetime.now().strftime("%Y-%m-%d %H:%M:%S") - most_recent_daily) > datetime.hour(24):
#        embed = discord.Embed(title="your daily reward", description=f"streak: {streak}\nready again at {ready_again_at}", color=Common.random_color())
#
#        #cash
#        cash_aquired = randint(100, 200) * (1 + ((streak * 2) * 0.1))
#        await give_cash(ctx.author.id, cash_aquired)
#        embed.add_field(name="Cash Received", value=f"${cash_aquired}", inline=False)
#
#        #common items
#        common_items_recieved = ""
#        if randint(0, 100) >= 2:
#            common_items = []
#            for item in Items.item_list:
#                if item['rarity'] == "Common":
#                    common_items.append(item['name'])
#
#            for i in range(randint(1, 5)):
#                item_aquired = random.choice(common_items)
#                #amount_aquired = random.choice[1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 8, 16, 32]
#                amount_aquired = randint(1, 4)
#                await give_item(ctx.author.id, item_aquired, amount_aquired)
#                common_items_recieved += f"{item_aquired}: {amount_aquired}\n"
#
#        embed.add_field(name="Common Items Received", value=common_items_recieved, inline=False)
#
#        await ctx.send(embed=embed)
#        await pg_con.execute(f"UPDATE users SET most_recent_daily = {str(datetime.now())} WHERE userid = '{member_id}'")
#        if (datetime.now() - most_recent_daily) < datetime.hour(48):
#            await pg_con.execute(f"UPDATE users SET current_streak = 0 WHERE userid = '{member_id}'")
#        else:
#            await pg_con.execute(f"UPDATE users SET current_streak = {streak + 1} WHERE userid = '{member_id}'")
#    else:
#        await ctx.send(f"your daily is ready again in {str(datetime.now()) - most_recent_daily}")



@client.command(brief="buy an item")
async def buy(ctx, item_name, amount = 1):
    if amount < 1:
        await ctx.send(f"You cannot buy 0 or a negative number of items! {random.choice(Lists.all_face_emoji)}")
        return

    member_id = str(ctx.author.id)

    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    for item in Items.item_list:
        if item['name'] == item_name:
            if db_user['cash'] >= (item['cost'] * amount):
                await give_item(ctx.author.id, item_name, amount)
                await give_cash(ctx.author.id, (-item['cost'] * amount))
                await ctx.send(f"You bought {amount} {item['friendly_name']} for ${item['cost'] * amount} {random.choice(Lists.all_face_emoji)}")
                return
            else:
                await ctx.send(f"You don't have enough money to buy this item! {random.choice(Lists.all_face_emoji)}")
                return
    await ctx.send(f"Item {item_name} was not found! {random.choice(Lists.all_face_emoji)} Make sure you spell it how it's displayed within the [] in the shop.")

@client.slash_command(name="buy", description="buy an item")
async def buy(ctx, item_name, amount = 1):
    if amount < 1:
        await ctx.send(f"You cannot buy 0 or a negative number of items! {random.choice(Lists.all_face_emoji)}")
        return

    member_id = str(ctx.author.id)

    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    for item in Items.item_list:
        if item['name'] == item_name:
            if db_user['cash'] >= (item['cost'] * amount):
                await give_item(ctx.author.id, item_name, amount)
                await give_cash(ctx.author.id, (-item['cost'] * amount))
                await ctx.send(f"You bought {amount} {item['friendly_name']} for ${item['cost'] * amount} {random.choice(Lists.all_face_emoji)}")
                return
            else:
                await ctx.send(f"You don't have enough money to buy this item! {random.choice(Lists.all_face_emoji)}")
                return
    await ctx.respond(f"Item {item_name} was not found! {random.choice(Lists.all_face_emoji)} Make sure you spell it how it's displayed within the [] in the shop.")
        
@client.command(aliases=["dc"], brief="give some money to another user")
async def donate_cash(ctx, member: discord.Member, amount = 1):
    member_id = str(ctx.author.id)
    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    if db_user['cash'] >= amount: 
        await give_cash(ctx.author.id, -amount)
        await give_cash(member.id, amount)
        await ctx.send(f"You gave ${amount} to {member.name}. How kind!")
    else:
        await ctx.send(f"You don't have that much money! {random.choice(Lists.all_face_emoji)}")

@client.slash_command(name="donate_cash", description="give some money to another user")
async def donate_cash(ctx, member: discord.Member, amount = 1):
    member_id = str(ctx.author.id)
    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    if db_user['cash'] >= amount: 
        await give_cash(ctx.author.id, -amount)
        await give_cash(member.id, amount)
        await ctx.respond(f"You gave ${amount} to {member.name}. How kind!")
    else:
        await ctx.respond(f"You don't have that much money! {random.choice(Lists.all_face_emoji)}")
        

@client.command(aliases=["di"], brief="give an item to another user")
async def donate_item(ctx, member: discord.Member, item_name, amount = 1):
    member_id = str(ctx.author.id)
    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)
    item_count = item_name + '_count'
    
    if db_user[item_count] >= amount:
        await give_item(ctx.author.id, item_name, -amount)
        await give_item(member.id, item_name, amount)
        await ctx.send(f"You gave {amount} {[sub['friendly_name'] for sub in Items.item_list if sub['name'] == item_name]} to {member.name}. How nice!")
    elif db_user[item_count] <= 0:
        await ctx.send(f"You don't have that item! {random.choice(Lists.all_face_emoji)}")
    else:
        await ctx.send(f"You don't enough of that item! {random.choice(Lists.all_face_emoji)} (You have {db_user[item_count]} and are trying to give {amount})")

@client.slash_command(name="donate_item", description="give an item to another user")
async def donate_item(ctx, member: discord.Member, item_name, amount = 1):
    member_id = str(ctx.author.id)
    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)
    item_count = item_name + '_count'
    
    if db_user[item_count] >= amount:
        await give_item(ctx.author.id, item_name, -amount)
        await give_item(member.id, item_name, amount)
        await ctx.send(f"You gave {amount} {[sub['friendly_name'] for sub in Items.item_list if sub['name'] == item_name]} to {member.name}. How nice!")
    elif db_user[item_count] <= 0:
        await ctx.respond(f"You don't have that item! {random.choice(Lists.all_face_emoji)}")
    else:
        await ctx.respond(f"You don't enough of that item! {random.choice(Lists.all_face_emoji)} (You have {db_user[item_count]} and are trying to give {amount})")



@client.command(aliases=["bal"], brief="check your balance")
async def balance(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    member_id = str(member.id)
    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    await ctx.send(embed=discord.Embed(title=f"{member.name}'s balance", description=f"${str(db_user['cash'])}", color=Common.random_color()))

@client.slash_command(name="balance", description="check your balance")
async def balance(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    member_id = str(member.id)
    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    await ctx.respond(embed=discord.Embed(title=f"{member.name}'s balance", description=f"${str(db_user['cash'])}", color=Common.random_color()))

@client.command(brief="throw away an item")
async def toss(ctx):
    await ctx.send("template command")
    
@client.command(brief="rob someone :flushed:")
async def rob(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    member_id = str(member.id)
    author_id = str(ctx.author.id)

    #base odds to successfully rob somone or lose money: 20%
    #you will steal 1 - 4% of their cash
    #cooldown to try to rob is 1 minute
    #after a user has been successfully robbed from, they won't be able to be robbed from for 1 hour
    #10% chance to give the person you're robbing 1 - 4% of your current cash

    robber = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", author_id)
    robbee = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    result = random.randint(0, 100)

    if result <= 20:
        #success
        percentage = random.randint(2, 5) * 0.01
        cash_stolen = math.floor(robbee['cash'] * percentage)
        await give_cash(ctx.author.id, cash_stolen)
        await give_cash(member.id, -cash_stolen)
        await ctx.send(f'You stole ${cash_stolen} from {member.name}#{member.discriminator}')
    elif result >= 80:
        #failure
        percentage = random.randint(2, 5) * 0.01
        cash_to_give = math.floor(robber['cash'] * percentage)
        await give_cash(member.id, cash_to_give)
        await give_cash(ctx.author.id, -cash_to_give)
        await ctx.send(f'You got caught and somehow ended up giving ${cash_to_give} to {member.name}#{member.discriminator}')
    else:
        await ctx.send(random.choice(['Your rob attempt was unsuccessful.', 'Your rob failed.', 'You failed to rob. Try again next time!','yikes, you totally failed and got nothing']))




@client.command()
async def grant_item(ctx, member: discord.Member, the_item, amount = 1):
    if ctx.author.id == Common.deatg_id:
        try:
            await give_item(str(member.id), the_item, amount)
        except:
            await ctx.send("error!!!")
    else:
        await ctx.send("You are not authorized to use this command!")

@client.command()
async def grant_cash(ctx, member: discord.Member, amount = 1):
    if ctx.author.id == Common.deatg_id:
        try:
            await give_cash(str(member.id), amount)
        except:
            await ctx.send("error!!!")
    else:
        await ctx.send("You are not authorized to use this command!")


async def drop_item(ctx, drop_money = False):
    if drop_money:
        money_to_drop = randint(100, 300)
        the_emoji = random.choice(Lists.all_emoji)
        drop_message = await ctx.send(f"first person to react to this message with {the_emoji} gets ${money_to_drop}!")

        def check(reaction, user):
            return str(reaction.emoji) == the_emoji and user != client.user


        try:
            reaction, user = await client.wait_for("reaction_add", check=check, timeout=60)

            await drop_message.edit(content=f"{drop_message.clean_content}\n{user.name} got the ${money_to_drop}!")
            await give_cash(str(user.id), money_to_drop)

        except asyncio.TimeoutError:
            await drop_message.edit(content=f"{drop_message.clean_content}\ntime's up! nobody got the ${money_to_drop}. <:epic_fail:925849582506741770>")

        #else:
        #    drop_message.edit(content=f"{drop_message.clean_content}\nthat's the wrong emoji! <:epic_fail:925849582506741770>")

    else:
        item_aquired = random.choice(Items.item_list)
        amount_aquired = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 8, 16, 32])
        the_emoji = random.choice(Lists.all_emoji)
        drop_message = await ctx.send(f"first person to react to this message with {the_emoji} gets {amount_aquired} {item_aquired['friendly_name']}(s)!")

        def check(reaction, user):
            return str(reaction.emoji) == the_emoji and user != client.user

        try:
            reaction, user = await client.wait_for("reaction_add", check=check, timeout=60)

            await drop_message.edit(content=f"{drop_message.clean_content}\n{user.name} got the {amount_aquired} {item_aquired['friendly_name']}(s)!")
            await give_item(str(user.id), item_aquired['name'], amount_aquired)

        except asyncio.TimeoutError:
            await drop_message.edit(content=f"{drop_message.clean_content}\ntime's up! nobody got the {item_aquired['friendly_name']}(s). <:epic_fail:925849582506741770>")

        #else:
        #    drop_message.edit(content=f"{drop_message.clean_content}\nthat's the wrong emoji! <:epic_fail:925849582506741770>")
    
        
@commands.command(name='eval', pass_context=True)
async def eval(ctx, *, command):
    if ctx.author.id == Common.deatg_id:
        res = eval(command)
        if inspect.isawaitable(res):
            await ctx.send(await res)
        else:
            await ctx.send(res)
    else:
        await ctx.send("you not deatg :skull:")



@client.event
async def on_message(message):
    author_id = str(message.author.id)
    db_user = await pg_con.fetch("SELECT * FROM users WHERE userid = $1", author_id)

    if not db_user:
        await pg_con.execute("INSERT INTO users (userid, xp, level) VALUES ($1, 0, 1)", author_id)

    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", author_id)

    await pg_con.execute("UPDATE users SET XP = $1 WHERE userid = $2", db_user['xp'] + 1, author_id)

    if db_user['xp'] >= round((4 * (db_user['level'] ** 3)) / 5):
        await pg_con.execute("UPDATE users SET level = $1 WHERE userid = $2", db_user['level'] + 1, db_user['userid'])

        if db_user['level'] % 5 == 0:
            await message.channel.send(f"{message.author.name} is now level {db_user['level']} congrats")

    if randint(0, 1350) == 1:
        if randint(1, 2) == 1:
            await drop_item(message.channel, True)
        else:
            await drop_item(message.channel, False)

    



client.loop.run_until_complete(create_db_pool())

client.run(token_lol)