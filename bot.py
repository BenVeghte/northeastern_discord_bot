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

@bot.command()
async def IndividualClass(ctx):
    men = ctx.message.mentions
    for person in men:
        await person.send("Please type in your classes in the following format, one class per message please. Finalize the message by sending .END")
        await person.send("Class Name, course number, college, section number, professor")

@bot.command()
async def END(ctx):
    if ctx.message.guild is None:
        #Insert code to run when someone dms
        past_msgs = list()
        async for message in ctx.history(limit=5):
            if message.author.bot == False:
                past_msgs.append(message)
        #ADD CODE HERE FOR DEALING WITH THE MESSAGE INPUTS
    else:
        await ctx.send("This command is not supported here...")


bot.run(key)