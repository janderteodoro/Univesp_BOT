from json import load
from dotenv import dotenv_values
import discord 
from discord.ext import commands 
from time import sleep


config = dotenv_values('.env')

bot = commands.Bot('!')

@bot.event
async def on_ready():
    print(f'Estou pront!o Estou conectado como {bot.user}')

@bot.event 
async def on_message(message): 
    if message.author == bot.user:
        return 

    await bot.process_commands(message)


@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name 
    response = f'Olá {name}, sou assistente virtual da UNIVESP, qual a sua dúvida?'
    await ctx.send(response)



bot.run(config['TOKEN'])