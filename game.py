
def printGuesses():
    # Get the guessed letters
    pass

def printTargetSpaces():
    pass
    # Get the target word, loop through it, printing an underscore at each
    # letter


def printNewGame():
    """Prints the gallows"""
    resStr = ""
    resStr += printTop()
    resStr += printFill()
    resStr += printFill()
    resStr += printFill()
    resStr += printFill()
    resStr += printGrass()
    print (resStr)


def printHangman():
    """Prints the endgame picture"""
    resStr = ""
    resStr += printTop()
    resStr += printHead()
    resStr += printRightArm()
    resStr += printBody()
    resStr += printRightLeg()
    resStr += printGrass()
    print (resStr)


def printGameHead():
    """Adds character head to gallows"""
    resStr = ""
    resStr += printTop()
    resStr += printHead()
    resStr += printFill()
    resStr += printFill()
    resStr += printFill()
    resStr += printGrass()
    print (resStr)


def printGameBody():
    """Adds character body to gallows"""
    resStr = ""
    resStr += printTop()
    resStr += printHead()
    resStr += printBody()
    resStr += printBody()
    resStr += printFill()
    resStr += printGrass()
    print (resStr)


def printGameLeftArm():
    """Adds left arm to gallows"""
    resStr = ""
    resStr += printTop()
    resStr += printHead()
    resStr += printLeftArm()
    resStr += printBody()
    resStr += printFill()
    resStr += printGrass()
    print (resStr)

def printGameRightArm():
    """Adds right arm to gallows"""
    resStr = ""
    resStr += printTop()
    resStr += printHead()
    resStr += printRightArm()
    resStr += printBody()
    resStr += printFill()
    resStr += printGrass()
    print (resStr)

def printGameLeftLeg():
    """Adds left leg to gallows"""
    resStr = ""
    resStr += printTop()
    resStr += printHead()
    resStr += printRightArm()
    resStr += printBody()
    resStr += printLeftLeg()
    resStr += printGrass()
    print (resStr)


def printFromRemGuess(number_of_guesses_remaining):
    """Prints correct scene based on remaining guesses"""
    if (number_of_guesses_remaining == 6):
        return printNewGame
    if (number_of_guesses_remaining == 5):
        return printGameHead
    if (number_of_guesses_remaining == 4):
        return printGameBody
    if (number_of_guesses_remaining == 3):
        return printGameLeftArm
    if (number_of_guesses_remaining == 2):
        return printGameRightArm
    if (number_of_guesses_remaining == 1):
        return printGameLeftLeg
    if (number_of_guesses_remaining == 0):
        return printHangman


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
