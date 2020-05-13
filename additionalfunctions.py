#This file was created to help organize the code outside the core file


def removeCommand(instring):
    instring = instring.split()
    print(instring)
    outstring = " ".join(instring[1:])
    return outstring

def UIDtoAlpha(idnum):
    idnum = str(idnum)
    out = list()
    alphabet = "abcdefghij"
    for num in idnum:
        out.append(alphabet[int(num)])
    return ''.join(out)