from protorpc import messages
from google.appengine.ext import ndb

class User(ndb.Model):
    """User object"""
    user_name = messages.StringField(1)
    email_address = messages.StringField(2)

class StringMessage(messages.Message):
    """Convenience class for single line responses"""
    message = messages.StringField(1, required=True)
