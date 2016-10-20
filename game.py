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

def printGuesses(game_key):
    # Get the guessed letters
    pass

def printTargetSpaces(game_key):
    pass
    # Get the target word, loop through it, printing an underscore at each
    # letter

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
