import discord
import random
from random import randint
from discord.ext import commands

class Items(commands.Cog):

    def __init__(self, client):
        self.client = client

    item_list = [
        {
        	'id': 1,
            'name': 'egg',
        	'friendly_name': 'Egg',
            'description': 'Can I offer you a nice egg in this trying time?',
        	'use_messages': ['Here are your eggs, sir!'],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [],
            'damage': 0,
            'heal_amount': 50
        },
        {
        	'id': 2,
            'name': 'terrydrawing',
        	'friendly_name': 'Drawing of Terry Crews',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 3,
            'name': 'soup',
        	'friendly_name': 'Soup',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 4,
            'name': 'the',
        	'friendly_name': '**The**',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 5,
            'name': 'lasaga',
        	'friendly_name': 'Lasaga',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 6,
            'name': 'laptop',
        	'friendly_name': '$15 Laptop from Wish.com',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 7,
            'name': 'brazil',
        	'friendly_name': 'Brazil',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 8,
            'name': 'keyboardcontroller',
        	'friendly_name': 'GameCube Keyboard Controller',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 9,
            'name': 'godstatue',
        	'friendly_name': 'God Statue',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 10,
            'name': 'demfextablet',
        	'friendly_name': 'Demfex Tablet',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 11,
            'name': 'dinnerblaster',
        	'friendly_name': 'Dinner Blaster',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 12,
            'name': 'salad',
        	'friendly_name': 'Pizza Pasta Salad With Chicken Breast Halves',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 13,
            'name': 'tree',
        	'friendly_name': 'Tree',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 14,
            'name': 'sledgehammer',
        	'friendly_name': 'Sledgehammer',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 15,
            'name': 'cableandrouter',
        	'friendly_name': 'Network Cable and Router',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 16,
            'name': 'sqlsoup',
        	'friendly_name': 'Derek\'s SQL Soup',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 17,
            'name': 'bup',
        	'friendly_name': 'BUP',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 18,
            'name': 'hemoglobin',
        	'friendly_name': 'Hemoglobin',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 19,
            'name': 'compressedair',
        	'friendly_name': 'Compressed Air',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 20,
            'name': 'harpoon',
        	'friendly_name': 'Harpoon',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 21,
            'name': 'manymanymeats',
        	'friendly_name': 'Many Many Meats',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 22,
            'name': 'manymanymeatsflavourful',
        	'friendly_name': 'Many Many Meats (Flavourful)',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 23,
            'name': 'buttor',
        	'friendly_name': 'Buttor',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 24,
            'name': 'ape',
        	'friendly_name': 'Ape',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 25,
            'name': 'recyclebin',
        	'friendly_name': 'Recycle Bin',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 26,
            'name': 'stopsign',
        	'friendly_name': 'Stop Sign',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 27,
            'name': 'spongebob',
        	'friendly_name': 'SpongeBob SquarePants',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 28,
            'name': 'sign',
        	'friendly_name': 'Sign',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 29,
            'name': 'donkeykongbarrelblast',
        	'friendly_name': 'Donkey Kong Barrel Blast',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 30,
            'name': 'femboy',
        	'friendly_name': 'Femboy',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 31,
            'name': 'spritecranberry',
        	'friendly_name': 'Sprite® Cranberry',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 32,
            'name': 'fidgetspinner',
        	'friendly_name': 'Fidget Spinner',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 33,
            'name': 'glassofwater',
        	'friendly_name': 'Glass of Water',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 34,
            'name': 'brainage',
        	'friendly_name': 'Brain Age',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 35,
            'name': 'tire',
        	'friendly_name': 'Tire',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 36,
            'name': 'glassofmilk',
        	'friendly_name': 'Glass of Milk',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 37,
            'name': 'jollizoom',
        	'friendly_name': 'Jollizoom',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 38,
            'name': 'bingus',
        	'friendly_name': 'Bingus',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 39,
            'name': 'totemofundying',
        	'friendly_name': 'Totem of Undying',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 40,
            'name': 'nautilusshell',
        	'friendly_name': 'Nautilus Shell',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 41,
            'name': 'warioshamburger',
        	'friendly_name': 'Wario\'s Hamburger',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        },
        {
        	'id': 42,
            'name': 'headphones',
        	'friendly_name': 'Headphones',
            'description': '',
        	'use_messages': [''],
        	'consume_chance': 1.0,
        	'cost': 50,
        	'sell_price': 10,
        	'rarity': 'Common',
            'available_in_shop': True,
            'battle_use_messages': [''],
            'damage': 0,
            'heal_amount': 0
        }
    ]

def setup(client):
    client.add_cog(Items(client))


