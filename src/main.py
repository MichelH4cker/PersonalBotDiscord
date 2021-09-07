import discord 
from discord.ext import commands

from dotenv import load_dotenv
import os

load_dotenv()

bot = commands.Bot(command_prefix = ">", case_insensitive = True)

@bot.event
async def on_ready():
    print('Entramos como {0.user}' .format(bot))


@bot.command()
async def ola(ctx):
    await ctx.send(f'hello, {ctx.author}')

@bot.command()
async def tchau(ctx):
    await ctx.send(f'VAZA, {ctx.author}')



####### RUN
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(DISCORD_TOKEN)