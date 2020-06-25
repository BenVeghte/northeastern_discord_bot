import discord
from discord.ext import commands
from discord.utils import get
from additionalfunctions import *
from userclass import *
from courseclass import *
import pickle
import asyncio
import atexit
import os


#This section of code imports the key from the text file and saves it as variable key
keyfile = open('bot_key.txt')
key = str(keyfile.read())
keyfile.close()



#Loading the pickle files with the stored objects from previous cycles of the program
try: #Try to open current version of pkl output for objects
    picklefile = open("pickleoutput/classes.pkl", 'rb')

except FileNotFoundError:
    try: #Try to open old version of pkl output for objects
        picklefile = open("pickleoutput/old.pkl", 'rb')

    except FileNotFoundError:
        print("There are not existing object pickle files to load")

    else: #If old pickle files does exist
        pklload  = pickle.load(picklefile)
        picklefile.close()

        for i in pklload:
            if type(i) is Course:
                globals()[generateCourseKey(i.courseName)] = i
                courseobjs.append(generateCourseKey(i.courseName))

            if type(i) is User:
                globals()[UIDtoAlpha(i.userid)] = i
                userobjs.append(UIDtoAlpha(i.userid))

else: #If current gen pickle file does exist
    pklload  = pickle.load(picklefile)
    picklefile.close()

    for i in pklload:
        if type(i) is Course:
            globals()[generateCourseKey(i.courseName)] = i
            courseobjs.append(generateCourseKey(i.courseName))

        if type(i) is User:
            globals()[UIDtoAlpha(i.userid)] = i
            userobjs.append(UIDtoAlpha(i.userid))





#Beginning of the code for running the discord bot
bot = commands.Bot(command_prefix='.')

#Function to alert when the bot is ready to accept commands
@bot.event
async def on_ready():
    print('Bot is ready.')

#This function mostly serves to test various discord interactions
@bot.command()
async def Initialize(ctx):
    await ctx.send(ctx.message.author.mention)
    print(ctx.message.author.id)

#Sends a DM to the person who used this command with the necessary information to correctly utilize the .End function
@bot.command()
async def IndividualClass(ctx):
    men = ctx.message.mentions
    for person in men:
        await person.send("Please type in your classes in the following format, one class per message please. Finalize the message by sending .END")
        await person.send("Class name, course number, college, section number, professor")
        await person.send("Example:")
        await person.send("Statics, 2350, ME, 1, Coskun")
        await person.send("The order of this is very important as is the number of inputs, \n please check, double check and if neccessary edit, before sending the .END command")

#This function serves to collect user sent data and turn it in to course and user objects, doesn't create channels yet
@bot.command()
async def END(ctx):
    past_msgs = list()
    #Ensures the message was in a DM channel and not from a bot so it doesn't get spammed
    if ctx.message.guild is None and ctx.message.author.bot is False:
        #Gathers past messages
        async for message in ctx.history(limit=10):
            #Once one of the past messages is a bots (sent by this bot), it stops reading
            if message.author.bot == False:
                past_msgs.append(message)
            elif message.author.bot == True:
                break

        #Deletes the first message as it is the .End command that triggered this sequence and we don't want to use that
        del past_msgs[0]

        #Gets the author id to store the user object under
        authID = past_msgs[0].author.id
        #Because variables cant have numbers, this function turns numbers to the corresponding letter
        newclassname = UIDtoAlpha(authID)
        
        #Iterates through the past messages
        msgs_split = list()
        for num, msg in enumerate(past_msgs):
        
            #Splits each message to a nested list, each row is a new message, each column is a different section, separated by a column with leading and trailing spaces removed
            msgs_split.append(msg.content.split(','))
            for num, mg in enumerate(msgs_split[-1]):
                msgs_split[-1][num] = mg.strip()
            del num
            
            #If there are to few or to many inputs, exit out of the function and make them call it again.
            if len(msgs_split[-1]) != 5:
                await ctx.author.send("There is something wrong with message number {}, please redo the command and fix the mistake".format(num))
                return

        match2 = False
        #For loop to add/adjust User Objects
        for key in globals().keys():                    ##EDIT HERE: CHANGE FROM A FOR LOOP LOOKING THROUGH ALL GLOBALS TO FOR LOOP LOOKING THROUGH LIST OF USER CLASSES
            #If the user class already exists
            if key == newclassname:
                match2 = True

                #goes through each row in the message history and gets the first item (coursename) and turns it into something that accounts for extra spaces and wierd captitalization
                for msg in msgs_split:
                    #Turns the name in to something that accounts for weird spaces and capitalization
                    coursenadj = msg[0].replace(" ", "").lower
                    match = False

                    #Checks to see if  the course already exists in the user class
                    for course in globals()[newclassname].classes:

                        #If the name is a match, over write old stored data in it incase someone is trying to make a modification
                        if course["Class Name"].replace(" ", "").lower == coursenadj:
                            match = True
                            course["Professor"] = msg[4]
                            course["Section"] = msg[3]
                            break

                    #If the course doesnt exist in the User class already, add it to the end of the list of classes    
                    if match is False:
                        globals()[newclassname].classes.append(
                            {"Class Name" : msg[0],
                            "Professor" : msg[4],
                            "Section" : msg[3]}
                        )

        #If the user class doesnt exist already, create it                
        if match2 is False:
            classlst = list()
            msgs_split = list()
            for msg in past_msgs:
                #Trims the messages and splits it at the commas
                msgs_split.append(msg.content.split(","))
                classlst.append({
                    "Class Name" : msg[0],
                    "Professor": msg[4], 
                    "Section" : msg[3]
                })
                #Splits each message to a nested list, each row is a new message, each column is a different section, separated by a column with leading and trailing spaces removed
                msgs_split[num-1] = msg.content.split(',').trim()
            globals()[newclassname] = User(userid = authID, classes= classlst)





        #For loop to add/adjust Course Objects
        for msg in msgs_split:
            match = False
            
            #Goes through each of  global variables and compares it to each of the course names in the past messages
            for key in globals().keys():

                #If there is a match
                if msg[0].replace(" ", "").lower == key:
                    match = True
                    #Add professors, sections, and members, builtin functions account for redundancy
                    globals()[key].addProf(msg[4])
                    globals()[key].addSection(msg[3])
                    globals()[key].addMember(authID)
                    
            #If there is no match, in any of the global variables
            if match is False:
                globals()[msg[0].replace(" ", "").lower] = Course(msg[0], msg[1], msg[2], msg[3], msg[4], authID)

    else:
        await ctx.send("This command is not supported here...")

#Code for saving variables in case of shutdown
@atexit.register
def shutdownPickle():
    try:
        os.rename(r'pickleoutput/classes.pkl', r'pickleoutput/old.pkl')
    except FileExistsError:
        os.remove(r'pickleoutput/old.pkl')
        os.rename(r'pickleoutput/classes.pkl', r'pickleoutput/old.pkl')
        

    picklefile = open("pickleoutput/classes.pkl", 'ab')
    print("One last thing...")
    picklelist = list()
    for key in globals().keys():
        if type(globals()[key]) is Course:
            picklelist.append(globals()[key])
        if type(globals()[key]) is User:
            picklelist.append(globals()[key])
    pickle.dump(picklelist, picklefile)
    picklefile.close()

bot.run(key)