import discord
from discord.ext import commands
with open('token.txt','r') as file:
	token=file.read()
with open('bitke.txt','r',encoding='UTF-8') as file:
    bitke=list(file.read().split('\n'))
with open('vladari.txt','r',encoding='UTF-8') as file:
    vladari=list(file.read().split('\n'))
vi=['Napoleon','LujXIV','LudovikVeliki','SulejmanVeličanstveni','FranjoJosip']
bi=['Borodino','Caporreto','Kursk','Mohačka','Lepand']
client=commands.Bot(command_prefix='_')
@client.event
async def on_ready():
    print('Spreman!')
@client.command()
async def bitka(ctx,*,bit):
    await ctx.send(bitke[bi.index(bit)])
@client.command()
async def Vladar(ctx,*,vit):
    await ctx.send(vladari[vi.index(vit)])
@client.command()
async def dostupnebitke(ctx):
    await ctx.send(bi)
@client.command()
async def Vladari(ctx):
    await ctx.send(vi)
@client.command()
async def pomoć(ctx):
    await ctx.send('bitka,Vladar,dostupnebitke,Vladari')
#@client.command()
client.run(token)
