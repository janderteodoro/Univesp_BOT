import discord
from discord.ext import commands
from src import config
from src.responses import responses

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
            f'''Olá {message.author.name}, Eu sou o **UniDroid** 🤖\nO assistente virtual da Univesp, Estou aqui para tirar suas dúvidas!\n\n**1** - Sobre o Vestibular\n**2** - Já é aluno? Consulte o Manual do Aluno\n**3** - Sobre a Univesp\n**4** - Sobre meu Criador\n\nPara voltar aqui digite **!menu**'''
        )

    if message.content == '1': 
        await message.channel.send(responses['item1'])

    if message.content == '2': 
        await message.channel.send(responses['item2'])
    
    if message.content == '3':
        await message.channel.send(responses['item3'])
    
    if message.content == '4':
        await message.channel.send(responses['item4'])


    await bot.process_commands(message)


@bot.command(name='menu')
async def send_hello(ctx):
    name = ctx.author.name 
    response = f'''Olá {name}, Eu sou o **UniDroid** 🤖\nO assistente virtual da Univesp, Estou aqui para tirar suas dúvidas!\n\n**1** - Sobre o Vestibular\n**2** - Já é aluno? Consulte o Manual do Aluno\n**3** - Sobre a Univesp\n**4** - Sobre meu Criador\n\nPra Voltar aqui digite **!menu**'''
    await ctx.send(response)



bot.run(config.token)