from random import randint
import linecache

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
    pass # should return comma separated chars that have been guessed

def printSpaces(game):
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


def printGrass():
    return(",,,,||,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")


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
