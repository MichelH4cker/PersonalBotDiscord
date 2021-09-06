import discord 
from discord.ext import commands

client = commands.Bot(command_prefix = ">", case_insensitive = True)

@client.event
async def on_ready():
    print('Entramos como {0.user}' .format(client))


@client.command()
async def ola(ctx):
    await ctx.send(f'hello, {ctx.author}')

@client.command()
async def tchau(ctx):
    await ctx.send(f'VAZA, {ctx.author}')


####### RODANDO LOCALMENTE
from secret_keys import TOKEN   # IMPORTA O TOKEN DO BOT NO ARQUIVO SECRET_KEYS.PY
secret_token = TOKEN            # VARIÁVEL RECEBE O TOKEN SECRETO

client.run(secret_token)