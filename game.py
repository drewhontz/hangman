import linecache
import endpoints
from random import randint


def str_match(history, target):
    """Compares 2 strings and returns if the unordered contents of the first can
    be assembled to form the target. Ex. str_match("abc", "cab") == True"""
    if " " in target:
        target = target.replace(" ", "")
    for c in target:
        if c not in history:
            return False
    return True


def guess(game, letter):
    """Game guessing logic"""
    if len(letter) > 1:
        raise endpoints.BadRequestException("Please only guess one character")
    if letter in game.history:
        raise endpoints.BadRequestException("You already guessed that")
    else:
        game.history += letter
        if letter in game.target:
            if str_match(game.history, game.target):
                game.game_end(True)
        else:
            game.remaining_attempts -= 1
            if game.remaining_attempts == 0:
                game.game_end(False)
        game.put()


def random_word():
    """Opens the wordbank and returns the word from a random line"""
    file_name = "wordbank.txt"
    number_of_lines = file_len(file_name) - 1
    target_line = randint(0, number_of_lines)
    target_word = linecache.getline(file_name, target_line)
    return target_word.replace("\n", "")


def file_len(fname):
    """Returns the number of lines in a file. Found on StackOverflow"""
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def get_status(game):
    """Returns the status of the game, win-lose-or remaining_attempts"""
    if game.over == True:
        if game.won == True:
            return "Game over, you win!"
        else:
            return "Game over, try again!"
    else:
        return "Keep guessing, you have " + str(game.remaining_attempts) + " guesses left."


def print_guesses(game):
    """Returns the guesses up to this point"""
    returnStr = "Guessed: "
    for c in game.history:
        if c not in game.target:
            returnStr += c + " "
    return returnStr


def print_spaces(game):
    """Prints the blank spaces left during your game"""
    returnStr = ""
    for c in game.target:
        if c == " ":
            returnStr += "  "
        else:
            if c in game.target and c in game.history:
                returnStr += c
            else:
                returnStr += "_ "
    return returnStr
