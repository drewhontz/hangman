import linecache
import endpoints
from random import randint


def guess(game, letter):
    """Game guessing logic"""
    if letter in game.guessed_letters or letter in game.matched_letters:
        raise endpoints.BadRequestException("You already guessed that")
    else:
        if letter in game.target:
            game.matched_letters += letter
            unique_match = "".join(set(game.matched_letters))
            unique_target = "".join(set(game.target))
            if len(unique_match) == len(unique_target):
                game.game_end(True)
        else:
            game.guessed_letters+= letter
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
    return target_word.replace("\n","")


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
    guesses = game.guessed_letters
    for c in guesses:
        returnStr += c + " "
    return returnStr


def print_spaces(game):
    """Prints the blank spaces left during your game"""
    matched_letters = game.matched_letters
    target = game.target  # we can hit parts of the model now so this is gone
    returnStr = ""
    for c in target:
        if c == " ":
            returnStr += "  "
        else:
            if c in matched_letters:
                returnStr += c
            else:
                returnStr += "_ "
    return returnStr
