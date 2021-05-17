import discord
from discord.ext import commands
with open('token.txt','r') as file:
	token=file.read()
client=commands.Bot(command_prefix='_')
@client.event
async def on_ready():
    print("Spreman!")
@client.command()
async def Borodino(ctx):
    await ctx.send("Bitka kod Borodina se dogodila 1813. godine")
client.run(token)
