from protorpc import messages
from game import *
from google.appengine.ext import ndb

class User(ndb.Model):
    """User object"""
    user_name = ndb.StringProperty(required=True)
    email_address = ndb.StringProperty()

class Score(ndb.Model):
    user_name = ndb.KeyProperty(required=True, kind="User")
    score = ndb.IntegerProperty(required=True)

class Game(ndb.Model):
    """Game object"""
    secret = randomWord()
    user_name = ndb.KeyProperty(required=True, kind="User")
    remaining_attempts =  ndb.IntegerProperty(default=6)
    target = ndb.StringProperty(default=secret)
    guessed_letters = ndb.StringProperty(default="")
    matched_letters = ndb.StringProperty(default="")

    @classmethod
    def new_game(self, user):
        """Creates a new game for a given user"""
        game = Game(user_name=user)
        return game

    @classmethod
    def to_form(self):
        """Returns GameMessage for Hangman game"""
        return GameMessage(
            game__1=printTop(),
            game__2=printRope(),
            game__3=printRope(),
            game__4=printFill(),
            game__5=printFill(),
            game__6=printFill(),
            game__7=printFill(),
            game__8=printFill(),
            game__9=printFill(),
            grass___=printGrass(),
            guesses=printSpaces(self),
            zspaces=printGuesses(self)
        )

class StringMessage(messages.Message):
    """Convenience class for single line responses"""
    message = messages.StringField(1, required=True)

class GameMessage(messages.Message):
    """Visual representation of a game"""
    game__1 = messages.StringField(1, required=True)
    game__2 = messages.StringField(2, required=True)
    game__3 = messages.StringField(3, required=True)
    game__4 = messages.StringField(4, required=True)
    game__5 = messages.StringField(5, required=True)
    game__6 = messages.StringField(6, required=True)
    game__7 = messages.StringField(7, required=True)
    game__8 = messages.StringField(8, required=True)
    game__9 = messages.StringField(9, required=True)
    grass___ = messages.StringField(10, required=True)
    guesses = messages.StringField(11, required=True)
    zspaces = messages.StringField(12, required=True)

class ScoreTable(messages.Message):
    """Table for the topscores"""
    pass
