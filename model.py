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

    def to_form(self):
        """Returns GameMessage for Hangman game"""
        form = GameMessage()
        if self.over:
            form.a0 = " G A M E O V E R        "
            form.a1 = "   G A M E O V E R      "
            form.a2 = "     G A M E O V E R    "
            form.a3 = "       G A M E O V E R  "
            form.a4 = "         G A M E O V E R"
            form.a5 = "       G A M E O V E R  "
            form.a6 = "     G A M E O V E R    "
            form.a7 = "   G A M E O V E R      "
            form.a8 = " G A M E O V E R        "
            form.a9 = "                        "
            form.k_guesses=printSpaces(self)
            form.k_spaces=printGuesses(self)
            form.l_key=self.key.urlsafe()
            return form
        else:
            form.a0 = printTop()
            form.a1 = printRope()
            form.a2 = printRope()

        if self.remaining_attempts == 6:
            form.a3=printFill()
            form.a4=printFill()
            form.a5=printFill()
            form.a6=printFill()
            form.a7=printFill()
            form.a8=printFill()
            form.a9=printGrass()
            form.k_guesses=printSpaces(self)
            form.k_spaces=printGuesses(self)
            form.l_key=self.key.urlsafe()
        elif self.remaining_attempts == 5:
            form.a3 = printHead()
            form.a4 = printFill()
            form.a5 = printFill()
            form.a6 = printFill()
            form.a7 = printFill()
            form.a8 = printFill()
            form.a9 = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        elif self.remaining_attempts == 4:
            form.a3 = printHead()
            form.a4 = printBody()
            form.a5 = printBody()
            form.a6 = printFill()
            form.a7 = printFill()
            form.a8 = printFill()
            form.a9 = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        elif self.remaining_attempts == 3:
            form.a3 = printHead()
            form.a4 = printLeftArm()
            form.a5 = printBody()
            form.a6 = printFill()
            form.a7 = printFill()
            form.a8 = printFill()
            form.a9 = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        elif self.remaining_attempts == 2:
            form.a3 = printHead()
            form.a4 = printRightArm()
            form.a5 = printBody()
            form.a6 = printFill()
            form.a7 = printFill()
            form.a8 = printFill()
            form.a9 = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        elif self.remaining_attempts == 1:
            form.a3 = printHead()
            form.a4 = printRightArm()
            form.a5 = printBody()
            form.a6 = printLeftLeg()
            form.a7 = printFill()
            form.a8 = printFill()
            form.a9 = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        else:
            form.a3 = printHead()
            form.a4 = printRightArm()
            form.a5 = printBody()
            form.a6 = printRightLeg()
            form.a7 = printFill()
            form.a8 = printFill()
            form.a9 = printGrass()
            form.k_guesses = printSpaces(self)
            form.k_spaces = printGuesses(self)
            form.l_key = self.key.urlsafe()
        return form


class StringMessage(messages.Message):
    """Convenience class for single line responses"""
    message = messages.StringField(1, required=True)

class GameMessage(messages.Message):
    """Visual representation of a game"""
    a0 = messages.StringField(1, required=True)
    a1 = messages.StringField(2, required=True)
    a2 = messages.StringField(3, required=True)
    a3 = messages.StringField(4, required=True)
    a4 = messages.StringField(5, required=True)
    a5 = messages.StringField(6, required=True)
    a6 = messages.StringField(7, required=True)
    a7 = messages.StringField(8, required=True)
    a8 = messages.StringField(9, required=True)
    a9 = messages.StringField(10, required=True)
    k_guesses = messages.StringField(11, required=True)
    k_spaces = messages.StringField(12, required=True)
    l_key = messages.StringField(13, required=True)

class ScoreTable(messages.Message):
    """Table for the topscores"""
    pass
