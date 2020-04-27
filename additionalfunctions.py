#This file was created to help organize the code outside the core file


def removeCommand(instring):
    instring = instring.split()
    print(instring)
    outstring = " ".join(instring[1:])
    return outstring