import discord
from discord.ext import commands
with open('token.txt','r') as file:
	token=file.read()
with open('bitke.txt','r') as file:
    bitke=list(file.read().split('\n'))
with open('vladari.txt','r',encoding='UTF-8') as file:
    vladari=list(file.read().split('\n'))
vi=['Napoleon','LujXIV','LudovikVeliki']
bi=['Borodino','Caporreto','Kursk']
client=commands.Bot(command_prefix='_')
@client.event
async def on_ready():
    print(bitke)
@client.command()
async def bitka(ctx,*,bit):
    await ctx.send(bitke[bi.index(bit)])
@client.command()
async def Vladar(ctx,*,vit):
    await ctx.send(vladari[vi.index(vit)])
@client.command()
async def dostupnebitke(ctx):
    await ctx.send(bi)
client.run(token)
