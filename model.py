from protorpc import messages
from google.appengine.ext import ndb

class User(ndb.Model):
    """User object"""
    user_name = ndb.StringProperty(required=True)
    email_address = ndb.StringProperty()

class StringMessage(messages.Message):
    """Convenience class for single line responses"""
    message = messages.StringField(1, required=True)
