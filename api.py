""" Creation of the Hangman API. """
import endpoints
from protorpc import remote, messages
from model import *
from utils import *

USER_REQUEST = endpoints.ResourceContainer(user_name=messages.StringField(1),
                                           email_address=messages.StringField(2))
NEW_GAME_REQUEST = endpoints.ResourceContainer(user_name=messages.StringField(1))
MOVE_REQUEST = endpoints.ResourceContainer(urlsafe_game_key=messages.StringField(1),
    guess=messages.StringField(2))

@endpoints.api(name='hangman', version='v1')
class HangmanAPI(remote.Service):
    """Hangman API"""
    @endpoints.method(USER_REQUEST, StringMessage, path='user',
        http_method='POST', name='create_new_user')
    def create_user(self, request):
        """Create a new user for Hangman"""
        if User.query(User.user_name == request.user_name).get():
            raise endpoints.ConflictException(
            "Try again with a new handle, that one is taken.")
        user = User(user_name = request.user_name,
            email_address = request.email_address)
        user.put()
        return StringMessage(message="Welcome to Hangman, {}".\
            format(request.user_name))


    @endpoints.method(NEW_GAME_REQUEST, GameMessage, path='game',
        http_method='POST', name='create_game')
    def create_game(self, request):
        """Creates a new game for Hangman users"""
        user = User.query(User.user_name == request.user_name).get()
        if not user:
            raise endpoints.NotFoundException('User does not exist')
        game = Game.new_game(user.key)
        return game.to_form()


    @endpoints.method(MOVE_REQUEST, GameMessage,
        path="game/{urlsafe_game_key}", http_method='POST',
        name="guess_a_letter")
    def guess_a_letter(self, request):
        """Allows user to guess at the secret word"""
        game = get_by_urlsafe(request.urlsafe_game_key, Game)
        guess = request.guess
        secret = game.target
        if game.over == True:
            return game.to_form()
        if guess in secret:
            game.matched_letters += guess
        else:
            game.guessed_letters += guess
            game.remaining_attempts -= 1
            if game.remaining_attempts == 0:
                game.over = True
        game.put()
        return game.to_form()


    @endpoints.method(ScoreTable, path="scores",
        http_method="GET", name="get_high_scores")
    def get_scores(self, request):
        """Returns a list of the top 5 high scores"""
        # pass
        return ScoreTable


api = endpoints.api_server([HangmanAPI])
