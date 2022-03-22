from json import load
import discord 
from discord.ext import commands
import config
import responses

bot = commands.Bot('!')

@bot.event
async def on_ready():
    print(f'Estou pronto! Estou conectado como {bot.user}')



@bot.event 
async def on_message(message):
    #message.content = conteúdo da mensagem
    if message.author == bot.user:
        return 
    
    if message.content in config.greetingsWords:
        await message.channel.send(
            f'''Olá {message.author.name}, Eu sou o **UniDroid** 🤖\nO assistente virtual da **UNIVESP**, Estou aqui para **tirar suas dúvidas**!\n\n**1** - Sobre o Vestibular\n**2**- Informações sobre meu Criador'''
        )
    
    if message.content == '2':
        await message.channel.send(responses.item2)
    


    await bot.process_commands(message)


@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name 
    response = f'Olá {name}, sou assistente virtual da UNIVESP, qual a sua dúvida?'
    await ctx.send(response)



bot.run(config.token)