""" Creation of the Hangman API. """
import endpoints
from protorpc import remote, messages
from model import *
from game import *
from utils import *

USER_REQUEST = endpoints.ResourceContainer(user_name=messages.StringField(1),
                                           email_address=messages.StringField(2))
NEW_GAME_REQUEST = endpoints.ResourceContainer(user_name=messages.StringField(1))
MOVE_REQUEST = endpoints.ResourceContainer(urlsafe_game_key=messages.StringField(1),
    guess=messages.StringField(2))
GAME_REQUEST = endpoints.ResourceContainer(key=messages.StringField(1))

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
        game = Game(user_name=user.key, target=random_word())
        game.put()
        return game.to_form()


    @endpoints.method(MOVE_REQUEST, GameMessage,
        path="game/{urlsafe_game_key}", http_method='POST',
        name="guess_a_letter")
    def guess_a_letter(self, request):
        """Allows user to guess at the secret word"""
        # TODO what if this fails?
        game = get_by_urlsafe(request.urlsafe_game_key, Game)
        if game.over == True:
            raise endpoints.BadRequestException("GAME HAS ENDED")
        guess(game, request.guess)
        return game.to_form()


    @endpoints.method(response_message=ScoreTable, path="scores",
        http_method="GET", name="get_high_scores")
    def get_scores(self, request):
        """Returns a list of the high scores"""
        scores = Score.query().order(-Score.score)
        # TODO: Better handling method for when there are no scores
        return ScoreTable(items=[score.to_form() for score in scores])


    @endpoints.method(USER_REQUEST, ScoreTable,
        path="scores/{user_name}", http_method="POST",
        name="get_user_scores")
    def get_user_scores(self, request):
        """Returns the users top 5 scores"""
        user = User.query(User.user_name == request.user_name).get()
        if not user:
            raise endpoints.NotFoundException("That user doesn't exist")
        scores = Score.query(user.key == Score.user_name).order(-Score.score)
        return ScoreTable(items=[score.to_form() for score in scores])


    @endpoints.method(USER_REQUEST, GameList, path="games/{user_name}",
        http_method="GET", name="get_games_by_user")
    def get_user_games(self, request):
        """Retrieves all active games for a given user"""
        user = User.query(User.user_name == request.user_name).get()
        if not user:
            raise endpoints.NotFoundException("That user does not exist")
        games = Game.query(user.key == Game.user_name).filter(Game.over == False)
        return GameList(games=[game.to_form() for game in games])


    @endpoints.method(GAME_REQUEST, StringMessage,
        path="games/delete/{key}", http_method="POST",
        name="cancel_game")
    def cancel_game(self, request):
        """Cancels a given open game"""
        game = get_by_urlsafe(request.key, Game)
        if not game:
            raise endpoints.NotFoundException("Game does not exist")
        game.key.delete()
        return StringMessage(message="Game deleted!")


    @endpoints.method(response_message=StandingsTable, path="rankings",
        http_method="GET", name="get_standings")
    def get_user_rankings(self, request):
        """Returns an ordered list of users with best win-loss differential"""
        games = Game.query().group_by((Game.user_name,))
        return StandingsTable(items=[game.to_score() for game in games])

    @endpoints.method(GAME_REQUEST, StringMessage, path="/games/history/{key}",
        http_method="POST", name="get_history")
    def get_game_history(self, request):
        """Returns a list of the users guesses"""
        game = get_by_urlsafe(request.key, Game)
        return StringMessage(message="history in order of guess: " + game.history)

    # TODO: ADD cron job; make sure it is in the yaml as well

api = endpoints.api_server([HangmanAPI])
