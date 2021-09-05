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

client.run('ODgzNTA1NDM0NTcxNDY4ODEx.YTK6jg.bGiSAPLaIe6NUX5Ln25PKhy_z_U')

