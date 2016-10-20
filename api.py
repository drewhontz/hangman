""" Creation of the Hangman API. """


import endpoints
from protorpc import remote, messages
from models import User, StringMessage

NEW_GAME_REQUEST = endpoints.ResourceContainer(NewGameForm)
GET_GAME_REQUEST = endpoints.ResourceContainer(
        urlsafe_game_key=messages.StringField(1),)
GUESS_REQUEST = endpoints.ResourceContainer(
    MakeMoveForm,
    urlsafe_game_key=messages.StringField(1),)
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
        if User.query(User.name == request.user_name).get():
            raise endpointsConflictException("Try again with a new handle, that one is taken.")
        user = User(user_name = request.user_name, email_address = request.email_address)
        user.put()
        return StringMessage(message="Welcome to Hangman, {}".format(request.user_name))
