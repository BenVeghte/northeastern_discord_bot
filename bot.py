import discord
from discord.ext import commands
from discord.utils import get
from additionalfunctions import *
from userclass import *
import asyncio

#This section of code imports the key from the text file and saves it as variable key
keyfile = open('bot_key.txt')
key = str(keyfile.read())
keyfile.close()

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def Initialize(ctx):
    await ctx.send(removeCommand(str(ctx.message.content)))


bot.run(key)