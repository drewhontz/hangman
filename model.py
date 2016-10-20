from protorpc import messages
from google.appengine.ext import ndb

class User(ndb.Model):
    """User object"""
    user_name = ndb.StringProperty(required=True)
    email_address = ndb.StringProperty()

class Game(ndb.Model):
    """Game object"""
    user_name = ndb.KeyProperty(required=True, kind="User")
    remaining_attempts =  ndb.IntegerProperty(default=6)
    target = ndb.StringProperty()
    guessed_letters = ndb.StringProperty()
    matched_letters = ndb.StringProperty()

    @classmethod
    def new_game(class, user):
        """Creates a new game for a given user"""
        pass

    @classmethod
    def to_form(class):
        """Returns GameMessage for Hangman game"""
        pass

class StringMessage(messages.Message):
    """Convenience class for single line responses"""
    message = messages.StringField(1, required=True)

class GameMessage(messages.Message):
    """ASCII art representation of Hangman game"""
