
def printGuesses():
    # Get the guessed letters
    pass

def printTargetSpaces():
    pass
    # Get the target word, loop through it, printing an underscore at each
    # letter

def printHangman():
    resStr = ""
    resStr += printTop()
    resStr += printHead()
    resStr += printRightArm()
    resStr += printBody()
    resStr += printRightLeg()
    resStr += printGrass()
    print (resStr)

def printNewGame():
    resStr = ""
    resStr += printTop()
    resStr += printFill()
    resStr += printFill()
    resStr += printFill()
    resStr += printFill()
    resStr += printGrass()
    print (resStr)

def printTop():
    return("\t===================\n\t||/\t\t  |\n\t||\t\t  |\n")

def printGrass():
    grassStr = printFill()
    grassStr += printFill()
    grassStr += ",,,,,,,,||,,,,,,,,,,,,,,,,,,,"
    return(grassStr)

def printHead():
    return("\t||\t\t ( )\n")

def printBody():
    return("\t||\t\t  |\n")

def printLeftArm():
    return("\t||\t\t\ |\n")

def printRightArm():
    return("\t||\t\t\ | /\n")

def printLeftLeg():
    return("\t||\t\t /\n")

def printRightLeg():
    return ("\t||\t\t / \ \n")

def printFill():
    return("\t||\n")
