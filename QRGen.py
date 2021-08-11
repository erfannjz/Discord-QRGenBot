import discord
from datetime import datetime
from discord.ext import commands
from pyqrcode import create
from os import remove

class CONFIG:
    PREFIX = 'c'
    TOKEN = ''
 
    
bot = commands.Bot(command_prefix = CONFIG.PREFIX , case_insensitive = True , help_command = None)


@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching , name = 'cqr Command!'))
    print(datetime.today().replace(microsecond=0) ,'\n\nBot is online\nDeveloped by ErfanNJZ')

@bot.event
async def on_command_error(ctx , error):
    pass

@bot.command()
async def qr(ctx , * ,text):
    cimg = create(text)
    cimg.png('qr.png' , scale = 6)
    embed = discord.Embed(title = 'Your QRCode:' , colour = 0xffffff)
    embed.set_author(name = ctx.author.name)
    embed.set_image(url = "attachment://qr.png")
    await ctx.send(ctx.author.mention , file = discord.File('qr.png') , embed = embed)
    remove('qr.png')


bot.run(CONFIG.TOKEN)