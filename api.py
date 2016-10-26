# TODO: Fix up get get history so that it returns a game state with each guess


""" Creation of the Hangman API. """
import endpoints
from protorpc import remote, messages
from game import guess
from utils import get_by_urlsafe
from model import (User, Game, Score,
                   StringMessage, GameForm, GameList, ScoreTable)

USER_REQUEST = endpoints.ResourceContainer(
    user_name=messages.StringField(1),
    email_address=messages.StringField(2)
)
MOVE_REQUEST = endpoints.ResourceContainer(
    urlsafe_game_key=messages.StringField(1),
    guess=messages.StringField(2)
)
NEW_GAME_REQUEST = endpoints.ResourceContainer(
    user_name=messages.StringField(1))
GAME_REQUEST = endpoints.ResourceContainer(key=messages.StringField(1))
SCORE_REQUEST = endpoints.ResourceContainer(number_of_results=messages.IntegerField(1))

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
        user = User(user_name=request.user_name,
                    email_address=request.email_address)
        user.put()
        return StringMessage(message="Welcome to Hangman, {}".
                             format(request.user_name))

    @endpoints.method(NEW_GAME_REQUEST, GameForm, path='game',
                      http_method='POST', name='create_game')
    def create_game(self, request):
        """Creates a new game for Hangman users"""
        user = User.query(User.user_name == request.user_name).get()
        if not user:
            raise endpoints.NotFoundException('User does not exist')
        game = Game(user_name=user.key, target=random_word())
        game.put()
        return game.to_form()

    @endpoints.method(MOVE_REQUEST, GameForm,
                      path="game/{urlsafe_game_key}", http_method='PUT',
                      name="guess_a_letter")
    def guess_a_letter(self, request):
        """Allows user to guess at the secret word"""
        game = get_by_urlsafe(request.urlsafe_game_key, Game)
        if game.over == True:
            raise endpoints.BadRequestException("GAME HAS ENDED")
        guess(game, request.guess)
        return game.to_form()

    @endpoints.method(SCORE_REQUEST, ScoreTable, path="scores",
                      http_method="GET", name="get_high_scores")
    def get_high_scores(self, request):
        """Returns a list of the high scores"""
        if request.number_of_results:
            scores = Score.query(limit=number_of_results).order(-Score.score)
        else:
            scores = Score.query().order(-Score.score)
        return ScoreTable(items=[score.to_form() for score in scores])

    @endpoints.method(USER_REQUEST, ScoreTable,
                      path="scores/{user_name}", http_method="GET",
                      name="get_user_scores")
    def get_user_scores(self, request):
        """Returns the users top 5 scores"""
        user = User.query(User.user_name == request.user_name).get()
        if not user:
            raise endpoints.NotFoundException("That user doesn't exist")
        scores = Score.query(user.key == Score.user_name).order(-Score.score)
        return ScoreTable(items=[score.to_form() for score in scores])

    @endpoints.method(USER_REQUEST, GameList, path="games/{user_name}",
                      http_method="GET", name="get_user_games")
    def get_user_games(self, request):
        """Retrieves all active games for a given user"""
        user = User.query(User.user_name == request.user_name).get()
        if not user:
            raise endpoints.NotFoundException("That user does not exist")
        games = Game.query(user.key == Game.user_name).filter(
            Game.over == False)
        return GameList(games=[game.to_form() for game in games])

    @endpoints.method(GAME_REQUEST, StringMessage,
                      path="games/delete/{key}", http_method="DELETE",
                      name="cancel_game")
    def cancel_game(self, request):
        """Cancels a given open game"""
        game = get_by_urlsafe(request.key, Game)
        if not game:
            raise endpoints.NotFoundException("Game does not exist")
        if game.over:
            raise endpoints.ForbiddenException(
                "You cannot cancel a completed game")
        else:
            game.key.delete()
        return StringMessage(message="Game deleted!")

    @endpoints.method(response_message=ScoreTable, path="rankings",
                      http_method="GET", name="get_user_rankings")
    def get_user_rankings(self, request):
        """Returns an ordered list of users with best win-loss differential"""
        games = Game.query(projection=[Game.user_name], distinct=True)
        items = [game.to_score() for game in games]
        items.sort(key=lambda x: x.score, reverse=True)
        return ScoreTable(items=items)

    @endpoints.method(GAME_REQUEST, HistoryMessage, path="/games/history/{key}",
                      http_method="GET", name="get_game_history")
    def get_game_history(self, request):
        """Returns a list of the users guesses"""
        game = get_by_urlsafe(request.key, Game)
        moves = game.history_to_form()
        return HistoryMessage(history=[move for move in moves])


api = endpoints.api_server([HangmanAPI])
