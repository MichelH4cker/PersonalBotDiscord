import discord 
from discord.ext import commands

client = commands.Bot(command_prefix = "-f", case_insensitive = True)

@client.event
async def on_ready():
    print('Entramos como {0.user}'.format(client))

client.run('ODgzNTA1NDM0NTcxNDY4ODEx.YTK6jg.8eqV8SuJwLUdspES3KKaogVHXlA')

