""" Creation of the Hangman API. """


import endpoints
from protorpc import remote, messages
from model import User, StringMessage

USER_REQUEST = endpoints.ResourceContainer(user_name=messages.StringField(1),
                                           email_address=messages.StringField(2))

@endpoints.api(name='hangman', version='v1')
class HangmanAPI(remote.Service):
    """Hangman API"""
    @endpoints.method(
        USER_REQUEST,
        StringMessage,
        path='user',
        http_method='POST',
        name='create_new_user'
    )
    def create_user(self, request):
        if User.query(User.user_name == request.user_name).get():
            raise endpoints.ConflictException("Try again with a new handle, that one is taken.")
        user = User(user_name = request.user_name, email_address = request.email_address)
        user.put()
        return StringMessage(message="Welcome to Hangman, {}".format(request.user_name))

api = endpoints.api_server([HangmanAPI])
