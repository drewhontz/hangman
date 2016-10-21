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
        game.put()
        return game

    def to_form(self):
        """Returns GameMessage for Hangman game"""
        return GameMessage(
            a=printTop(),
            b=printRope(),
            c=printRope(),
            d=printFill(),
            e=printFill(),
            f=printFill(),
            g=printFill(),
            h=printFill(),
            i=printFill(),
            j=printGrass(),
            k_guesses=printSpaces(self),
            k_spaces=printGuesses(self),
            l_key=self.key.urlsafe()
        )

    def guess(self):
        pass

class StringMessage(messages.Message):
    """Convenience class for single line responses"""
    message = messages.StringField(1, required=True)

class GameMessage(messages.Message):
    """Visual representation of a game"""
    a = messages.StringField(1, required=True)
    b = messages.StringField(2, required=True)
    c = messages.StringField(3, required=True)
    d = messages.StringField(4, required=True)
    e = messages.StringField(5, required=True)
    f = messages.StringField(6, required=True)
    g = messages.StringField(7, required=True)
    h = messages.StringField(8, required=True)
    i = messages.StringField(9, required=True)
    j = messages.StringField(10, required=True)
    k_guesses = messages.StringField(11, required=True)
    k_spaces = messages.StringField(12, required=True)
    l_key = messages.StringField(13, required=True)

class ScoreTable(messages.Message):
    """Table for the topscores"""
    pass
