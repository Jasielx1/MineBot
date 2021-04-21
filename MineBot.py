import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
from dont_die import dont_die
 

client = discord.Client()
client = commands.Bot(command_prefix='%', help_command=None, description='Prefijo %')

@client.event
async def on_ready():
  print("Estoy funcionando, soy: {0.user}"
  .format(client))

@client.command(brief='Mi prefijo es "%"', description='Para mas info usa "%ayuda"')
async def foo():
    await client.say('Ola')

@client.command()
async def avatar(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

@client.command()
#This is defining a '!hello' command
async def ola (ctx):
    #In this case you have to use the ctx to send the message
    #Good to remember that ctx is NOT a parameter wich the user will give
    msg = f'Klk ¿Cómo tú ta? 👋🏻 {ctx.author.mention}'
    await ctx.send(msg)

@client.command()
async def ayuda(ctx):
    embed=discord.Embed(title="Soy MineBot, klk", description="Soy un bot dominicano, mi prefijo es '%' actualmente mis comandos son `%klk`, `%ayuda (%help)`, `%minecraft` y `%avatar`", color=0x00ffff)
    embed.set_image(url="https://i.imgur.com/ORDnQyY.jpg")
    await ctx.send(embed=embed)

@client.command()
async def klk(ctx):
    embed1=discord.Embed(title="Klk mi loco 👋🏻", color=0x00ffff)
    
    await ctx.send(embed=embed1)

@client.command()
async def minecraft(ctx):
    embed2=discord.Embed(title="⛏ ¿Cómo descargo Minecraft?", url="https://tlauncher.org/en/", description="Facil solo da click el titulo!", color=0x00ff00)
    embed2.set_image(url="http://assets.stickpng.com/thumbs/580b57fcd9996e24bc43c2f1.png")
    await ctx.send(embed=embed2)

@client.command()
async def help(ctx):
    embed3=discord.Embed(title="Soy MineBot, klk", description="Soy un bot dominicano, mi prefijo es '%' actualmente mis comandos son `%klk (%help)`, `%ayuda`, `%minecraft` y `%avatar`", color=0x00ffff)
    embed3.set_image(url="https://i.imgur.com/ORDnQyY.jpg")
    embed3.add_field(name="Server weno", value="mc.universocraft.com")
    await ctx.send(embed=embed3)

@client.command()
async def insulto(ctx):
  tester = [
    "Mamaguevazo",
    "Singa fiao",
    "Recontra hijo de mil putas",
    "Come mierda",
    "Eres la pena de tu familia",
    "Azaroso",
    "Anormal del diablo"
  ]
  await ctx.send(random.choice(tester))

dont_die()
client.run(os.getenv('PASS'))
