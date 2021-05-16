import discord
from discord.ext import commands
client=commands.Bot(command_prefix='_')
@client.event
async def on_ready():
    print("Spreman!")
@client.command()
async def Borodino(ctx):
    await ctx.send("Bitka kod Borodina se dogodila 1813. godine")
client.run('ODQzNDc4NzgzNDU3ODg2MjA5.YKEc1Q.k4OGZRRjHu9ucX1BxV1BsQ88zxQ')
