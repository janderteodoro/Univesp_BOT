from json import load
from dotenv import dotenv_values
import discord 
from discord.ext import commands 

config = dotenv_values('.env')

bot = commands.Bot('!')

@bot.event
async def on_ready():
    print(f'Estou pront! Estou conectado como {bot.user}')

bot.run(config['TOKEN'])
