import discord
import random
from random import randint
from discord.ext import commands

class Items(commands.Cog):

    def __init__(self, client):
        self.client = client

    egg = {
    	'id': 0,
    	'friendly_name': 'Egg',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    terrydrawing = {
    	'id': 0,
    	'friendly_name': 'Drawing of Terry Crews',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    soup = {
    	'id': 0,
    	'friendly_name': 'Soup',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    the = {
    	'id': 0,
    	'friendly_name': '**The**',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    lasaga = {
    	'id': 0,
    	'friendly_name': 'Lasaga',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    laptop = {
    	'id': 0,
    	'friendly_name': '$15 Laptop from Wish.com',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    brazil = {
    	'id': 0,
    	'friendly_name': 'Brazil',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    keyboardcontroller = {
    	'id': 0,
    	'friendly_name': 'GameCube Keyboard Controller',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    godstatue = {
    	'id': 0,
    	'friendly_name': 'God Statue',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    demfextablet = {
    	'id': 0,
    	'friendly_name': 'Demfex Tablet',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    dinnerblaster = {
    	'id': 0,
    	'friendly_name': 'Dinner Blaster',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    salad = {
    	'id': 0,
    	'friendly_name': 'Pizza Pasta Salad With Chicken Breast Halves',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    tree = {
    	'id': 0,
    	'friendly_name': 'Tree',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    sledgehammer = {
    	'id': 0,
    	'friendly_name': 'Sledgehammer',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    cableandrouter = {
    	'id': 0,
    	'friendly_name': 'Network Cable and Router',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    sqlsoup = {
    	'id': 0,
    	'friendly_name': 'Derek\'s SQL Soup',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    bup = {
    	'id': 0,
    	'friendly_name': 'BUP',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    hemoglobin = {
    	'id': 0,
    	'friendly_name': 'Hemoglobin',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    compressedair = {
    	'id': 0,
    	'friendly_name': 'Compressed Air',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    harpoon = {
    	'id': 0,
    	'friendly_name': 'Harpoon',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    manymanymeats = {
    	'id': 0,
    	'friendly_name': 'Many Many Meats',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    manymanymeatsflavourful = {
    	'id': 0,
    	'friendly_name': 'Many Many Meats (Flavourful)',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    buttor = {
    	'id': 0,
    	'friendly_name': 'Buttor',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    ape = {
    	'id': 0,
    	'friendly_name': 'Ape',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    recyclebin = {
    	'id': 0,
    	'friendly_name': 'Recycle Bin',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    stopsign = {
    	'id': 0,
    	'friendly_name': 'Stop Sign',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    spongebob = {
    	'id': 0,
    	'friendly_name': 'SpongeBob SquarePants',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    sign = {
    	'id': 0,
    	'friendly_name': 'Sign',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    donkeykongbarrelblast = {
    	'id': 0,
    	'friendly_name': 'Donkey Kong Barrel Blast',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    femboy = {
    	'id': 0,
    	'friendly_name': 'Femboy',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    spritecranberry = {
    	'id': 0,
    	'friendly_name': 'Sprite® Cranberry',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    fidgetspinner = {
    	'id': 0,
    	'friendly_name': 'Fidget Spinner',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    glassofwater = {
    	'id': 0,
    	'friendly_name': 'Glass of Water',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    brainage = {
    	'id': 0,
    	'friendly_name': 'Brain Age',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    tire = {
    	'id': 0,
    	'friendly_name': 'Tire',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    glassofmilk = {
    	'id': 0,
    	'friendly_name': 'Glass of Milk',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    jollizoom = {
    	'id': 0,
    	'friendly_name': 'Jollizoom',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    bingus = {
    	'id': 0,
    	'friendly_name': 'Bingus',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    totemofundying = {
    	'id': 0,
    	'friendly_name': 'Totem of Undying',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    nautilusshell = {
    	'id': 0,
    	'friendly_name': 'Nautilus Shell',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    warioshamburger = {
    	'id': 0,
    	'friendly_name': 'Wario\'s Hamburger',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }
    headphones = {
    	'id': 0,
    	'friendly_name': 'Headphones',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common'
    }


def setup(client):
    client.add_cog(Items(client))


