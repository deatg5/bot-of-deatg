from math import fabs
import discord
import os
from discord.ext import commands
import asyncpg
import textwrap
import sys



DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=commands.when_mentioned_or(';'), intents=intents)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def stop(self):
    os.execv(sys.executable, ['python'] + sys.argv)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

        


#database stuff handled in main bot file
async def create_db_pool():
        global pg_con 
        pg_con = await asyncpg.create_pool(host = "ec2-52-44-31-100.compute-1.amazonaws.com", database ="d9sog7i18caten", user ="bkpsbvehfzmaip", password = DATABASE_PASSWORD)


@client.command()
async def leaderboard(ctx, amount=30):
    board = ""
    db_user = await pg_con.fetch(f"SELECT * FROM users ORDER BY xp DESC LIMIT {amount}")
    for index, user in enumerate(db_user):
        gamer = client.get_user(int(user['userid']))
        gamer = str(gamer)
        gamer_notag = gamer[:-5]
        if len(gamer_notag) == 0:
            board += f"{str(index + 1)} - {user['userid']} (username unavailable): level {str(user['level'])}, {str(user['xp'])} XP\n"
        else:
            board += f"{str(index + 1)} - {str(gamer)}: level {str(user['level'])}, {str(user['xp'])} XP\n"

    if len(board) > 2000:
        for line in textwrap.wrap(board, 2000, drop_whitespace=False, replace_whitespace=False):
            async with ctx.typing():
                await ctx.send(f'{line}')
    else:
        await ctx.send(board)

@client.command()
async def level(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    member_id = str(member.id)

    db_user = await pg_con.fetchrow("SELECT * FROM users WHERE userid = $1", member_id)

    await ctx.send(f"{member.name}\nLevel: {db_user['level']}\nXP: {db_user['xp']}")

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