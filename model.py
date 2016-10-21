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
    user_name = ndb.KeyProperty(required=True, kind="User")
    remaining_attempts =  ndb.IntegerProperty(default=6)
    target = ndb.StringProperty(default=randomWord())
    guessed_letters = ndb.StringProperty(default="")
    matched_letters = ndb.StringProperty(default="")
    over = ndb.BooleanProperty(default=False)

    @classmethod
    def new_game(self, user):
        """Creates a new game for a given user"""
        game = Game(user_name=user)
        game.put()
        return game

    def to_form(self, number_of_remaining_attempts):
        """Returns GameMessage for Hangman game"""
        form = GameMessage()
        form.a = printTop()
        form.b = printRope()
        form.c = printRope()

        if (number_of_remaining_attempts == 5):
            form.d = printHead()
            form.e = printFill()
            form.f = printFill()
            form.g = printFill()
            form.h = printFill()
            form.i = printFill()
            form.j = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        if (number_of_remaining_attempts == 4):
            form.d = printHead()
            form.e = printBody()
            form.f = printBody()
            form.g = printFill()
            form.h = printFill()
            form.i = printFill()
            form.j = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        if (number_of_remaining_attempts == 3):
            form.d = printHead()
            form.e = printLeftArm()
            form.f = printBody()
            form.g = printFill()
            form.h = printFill()
            form.i = printFill()
            form.j = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        if (number_of_remaining_attempts == 2):
            form.d = printHead()
            form.e = printRightArm()
            form.f = printBody()
            form.g = printFill()
            form.h = printFill()
            form.i = printFill()
            form.j = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        if (number_of_remaining_attempts == 1):
            form.d = printHead()
            form.e = printRightArm()
            form.f = printBody()
            form.g = printLeftLeg()
            form.h = printFill()
            form.i = printFill()
            form.j = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        if (number_of_remaining_attempts == 0):
            form.d = printHead()
            form.e = printRightArm()
            form.f = printBody()
            form.g = printRightLeg()
            form.h = printFill()
            form.i = printFill()
            form.j = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        else:
            form.e=printFill()
            form.f=printFill()
            form.g=printFill()
            form.h=printFill()
            form.i=printFill()
            form.j=printGrass()
            form.k_guesses=printSpaces(self),
            form.k_spaces=printGuesses(self),
            form.l_key=self.key.urlsafe()
        return form

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
