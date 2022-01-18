from math import fabs
import math
import re
import string
import random
import discord
import os
from discord.ext import commands
import asyncpg
import textwrap
import sys

from cogs.items import Items
from cogs.common import Common
from cogs.lists import Lists

DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=commands.when_mentioned_or(';'), intents=intents)

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





#database stuff handled in main bot file
async def create_db_pool():
        global pg_con 
        pg_con = await asyncpg.create_pool(host = "ec2-52-44-31-100.compute-1.amazonaws.com", database ="d9sog7i18caten", user ="bkpsbvehfzmaip", password = DATABASE_PASSWORD)

@client.command(brief="the global bot of deatg leaderboard (1 xp = 1 message sent)")
async def leaderboard(ctx, amount=30):

    board = discord.Embed(title="leaderboard", description="1 XP is equal to 1 message sent\njust an ID means the user has been deleted or is inaccessable", color=Common.random_color())
    embed.add_field(name="field", value="value", inline=False)

    board = ""
    db_user = await pg_con.fetch(f"SELECT * FROM users ORDER BY xp DESC LIMIT {amount}")
    for index, user in enumerate(db_user):
        gamer = client.get_user(int(user['userid']))
        gamer = str(gamer)
        gamer_notag = gamer[:-5]
        if len(gamer_notag) == 0:
            board.add_field(name = f"{str(index + 1)} - {user['userid']}", value=f"level {str(user['level'])}, {str(user['xp'])} XP")
            #board += f"{str(index + 1)} - {user['userid']} (username unavailable): level {str(user['level'])}, {str(user['xp'])} XP\n"
        else:
            board.add_field(name = f"{str(index + 1)} - {str(gamer)}", value=f"level {str(user['level'])}, {str(user['xp'])} XP")
            #board += f"{str(index + 1)} - {str(gamer)}: level {str(user['level'])}, {str(user['xp'])} XP\n"

    await ctx.send(embed=board)

    # if len(board) > 2000:
    #     for line in textwrap.wrap(board, 2000, drop_whitespace=False, replace_whitespace=False):
    #         async with ctx.typing():
    #             await ctx.send(f'{line}')
    # else:
    #     await ctx.send(board)

@client.command(brief="check the level of you or another user")
async def level(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    member_id = str(member.id)

    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    await ctx.send(f"{member.name}\nLevel: {db_user['level']}\nXP: {db_user['xp']}")

    
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
        await ctx.send(f"You don't enough of that item! {random.choice(Lists.all_face_emoji)} (You have {db_user[item_count]} and are trying to give {amount}")



@client.command(aliases=["bal"], brief="check your balance")
async def balance(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    member_id = str(member.id)
    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    await ctx.send(embed=discord.Embed(title=f"{member.name}'s balance", description=f"${str(db_user['cash'])}", color=Common.random_color()))

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

    

client.loop.run_until_complete(create_db_pool())

client.run(os.environ['TOKEN'])