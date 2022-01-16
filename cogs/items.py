import discord
import random
from random import randint
from discord.ext import commands

class Items(commands.Cog):

    def __init__(self, client):
        self.client = client

    egg = {
    	'id': 1,
    	'friendly_name': 'Egg',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    terrydrawing = {
    	'id': 2,
    	'friendly_name': 'Drawing of Terry Crews',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    soup = {
    	'id': 3,
    	'friendly_name': 'Soup',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    the = {
    	'id': 4,
    	'friendly_name': '**The**',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    lasaga = {
    	'id': 5,
    	'friendly_name': 'Lasaga',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    laptop = {
    	'id': 6,
    	'friendly_name': '$15 Laptop from Wish.com',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    brazil = {
    	'id': 7,
    	'friendly_name': 'Brazil',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    keyboardcontroller = {
    	'id': 8,
    	'friendly_name': 'GameCube Keyboard Controller',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    godstatue = {
    	'id': 9,
    	'friendly_name': 'God Statue',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    demfextablet = {
    	'id': 10,
    	'friendly_name': 'Demfex Tablet',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    dinnerblaster = {
    	'id': 11,
    	'friendly_name': 'Dinner Blaster',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    salad = {
    	'id': 12,
    	'friendly_name': 'Pizza Pasta Salad With Chicken Breast Halves',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    tree = {
    	'id': 13,
    	'friendly_name': 'Tree',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    sledgehammer = {
    	'id': 14,
    	'friendly_name': 'Sledgehammer',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    cableandrouter = {
    	'id': 15,
    	'friendly_name': 'Network Cable and Router',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    sqlsoup = {
    	'id': 16,
    	'friendly_name': 'Derek\'s SQL Soup',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    bup = {
    	'id': 17,
    	'friendly_name': 'BUP',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    hemoglobin = {
    	'id': 18,
    	'friendly_name': 'Hemoglobin',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    compressedair = {
    	'id': 19,
    	'friendly_name': 'Compressed Air',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    harpoon = {
    	'id': 20,
    	'friendly_name': 'Harpoon',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    manymanymeats = {
    	'id': 21,
    	'friendly_name': 'Many Many Meats',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    manymanymeatsflavourful = {
    	'id': 22,
    	'friendly_name': 'Many Many Meats (Flavourful)',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    buttor = {
    	'id': 23,
    	'friendly_name': 'Buttor',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    ape = {
    	'id': 24,
    	'friendly_name': 'Ape',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    recyclebin = {
    	'id': 25,
    	'friendly_name': 'Recycle Bin',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    stopsign = {
    	'id': 26,
    	'friendly_name': 'Stop Sign',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    spongebob = {
    	'id': 27,
    	'friendly_name': 'SpongeBob SquarePants',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    sign = {
    	'id': 28,
    	'friendly_name': 'Sign',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    donkeykongbarrelblast = {
    	'id': 29,
    	'friendly_name': 'Donkey Kong Barrel Blast',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    femboy = {
    	'id': 30,
    	'friendly_name': 'Femboy',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    spritecranberry = {
    	'id': 31,
    	'friendly_name': 'Sprite® Cranberry',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    fidgetspinner = {
    	'id': 32,
    	'friendly_name': 'Fidget Spinner',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    glassofwater = {
    	'id': 33,
    	'friendly_name': 'Glass of Water',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    brainage = {
    	'id': 34,
    	'friendly_name': 'Brain Age',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    tire = {
    	'id': 35,
    	'friendly_name': 'Tire',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    glassofmilk = {
    	'id': 36,
    	'friendly_name': 'Glass of Milk',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    jollizoom = {
    	'id': 37,
    	'friendly_name': 'Jollizoom',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    bingus = {
    	'id': 38,
    	'friendly_name': 'Bingus',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    totemofundying = {
    	'id': 39,
    	'friendly_name': 'Totem of Undying',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    nautilusshell = {
    	'id': 40,
    	'friendly_name': 'Nautilus Shell',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    warioshamburger = {
    	'id': 41,
    	'friendly_name': 'Wario\'s Hamburger',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }
    headphones = {
    	'id': 42,
    	'friendly_name': 'Headphones',
    	'use_messages': [''],
    	'consume_chance': 1.0,
    	'cost': 50,
    	'sell_price': 10,
    	'rarity': 'Common',
        'available_in_shop': True,
        'battle_use_messages': [''],
        'damage': 10
    }


def setup(client):
    client.add_cog(Items(client))


