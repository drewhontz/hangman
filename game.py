import linecache
from random import randint

def randomWord():
    """Opens the wordbank and returns the word from a random line"""
    file_name = "wordbank.txt"
    number_of_lines = file_len(file_name)
    target_line = randint(0, number_of_lines)
    target_word = linecache.getline(file_name, target_line)
    return target_word.replace("\n","")

def file_len(fname):
    """Returns the number of lines in a file"""
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def printGuesses(game):
    """Returns the guesses up to this point"""
    returnStr = "Guessed: ")
    # guesses
    # for c in guesses returnStr += c
    return(returnStr)

def printSpaces(game):
    """Prints the blank spaces left during your game"""
    target = game.secret
    returnStr = ""
    for c in target:
        if c == " ":
            returnStr += "  "
        else:
            returnStr += "_ "
    return returnStr

def printTop():
    return("    ============        ")


def printRope():
    return("    ||                      |        ")


def printHead():
    return("    ||         ( )                   ")


def printBody():
    return("    ||          |                    ")


def printLeftArm():
    return("    ||        \ |                    ")


def printRightArm():
    return("    ||        \ | /                  ")


def printLeftLeg():
    return("    ||         /                     ")


def printRightLeg():
    return ("    ||         / \                  ")


def printFill():
    return("    ||                               ")


def printGrass():
    return(",,,,||,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
