import discord
from discord.ext import commands
from discord.utils import get
from additionalfunctions import *
from userclass import *
import asyncio

userobjs = list()
courseobjs = list()
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
    await ctx.send(ctx.message.author.mention)
    print(ctx.message.author.id)

@bot.command()
async def IndividualClass(ctx):
    men = ctx.message.mentions
    for person in men:
        await person.send("Please type in your classes in the following format, one class per message please. Finalize the message by sending .END")
        await person.send("Class name, course number, college, section number, professor")
        await person.send("Example:")
        await person.send("Statics, 2350, ME, 1, Coskun")
        await person.send("The order of this is very important as is the number of inputs, \n please check, double check and if neccessary edit, before sending the .END command")

@bot.command()
async def END(ctx):
    if ctx.message.guild is None and ctx.message.author.bot is False:
        #Insert code to run when someone dms
        past_msgs = list()
        async for message in ctx.history(limit=10):
            if message.author.bot == False:
                past_msgs.append(message)
            elif message.author.bot == True:
                break
        del past_msgs[0]
        newclassname = UIDtoAlpha(past_msgs[0].author.id)
        msgs_split = list()
        for num, msg in enumerate(past_msgs):
            msgs_split[num-1] = msg.content.split(',').trim().lower()
            if len(msgs_split) != 5:
                await ctx.author.send("There is something wrong with message number {}, please redo the command and fix the mistake").format(num))
                return
            #INSERT CODE HERE FOR ADDING COURSES AND USER OBJECTS
        for key in globals().keys():
            if key = newclassname:
                
            




    else:
        await ctx.send("This command is not supported here...")


bot.run(key)