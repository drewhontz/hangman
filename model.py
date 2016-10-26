import endpoints
from protorpc import messages
from game import random_word, print_spaces, print_guesses, get_status
from google.appengine.ext import ndb


class User(ndb.Model):
    """User object"""
    user_name = ndb.StringProperty(required=True)
    email_address = ndb.StringProperty()


class Score(ndb.Model):
    """Model for score object"""
    user_name = ndb.KeyProperty(required=True, kind="User")
    score = ndb.IntegerProperty(required=True)

    def to_form(self):
        """Returns a single score"""
        return ScoreForm(user_name=self.user_name.get().user_name, score=self.score)


class Game(ndb.Model):
    """Game object"""
    user_name = ndb.KeyProperty(required=True, kind="User")
    remaining_attempts = ndb.IntegerProperty(default=6)
    target = ndb.StringProperty(default=random_word())
    history = ndb.StringProperty(default="")
    over = ndb.BooleanProperty(default=False)
    won = ndb.BooleanProperty(default=False)  # I guess this could be computed
    modified = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def new_game(self, user):
        """Creates a new game for a given user"""
        game = Game(user_name=user)
        game.put()
        return game

    def to_form(self):
        """Returns GameForm for Hangman game"""
        form = GameForm()
        form.a_key = self.key.urlsafe()
        form.b_status = get_status(self)
        form.c_spaces = print_spaces(self)
        form.d_guesses = print_guesses(self)
        return form

    def game_end(self, won):
        """Ends the game when a player wins or loses"""
        self.over = True
        self.won = won
        self.put()
        if won:
            score = Score(user_name=self.user_name,
                          score=self.remaining_attempts)
            score.put()

    def to_score(self):
        """Returns score string for a game"""
        form = ScoreForm()
        user = self.user_name.get().user_name

        wins = Score.query(Score.user_name == self.user_name).count()
        losses = Game.query().filter(
            Game.won == False and Game.remaining_attempts == 0).count()
        diff = wins - losses

        form.user_name = user
        form.score = diff
        return form

    def history_to_form(self):
        """Returns an array of move forms"""
        history = ""
        for guess in self.history:
            form = MoveForm()
            form.guess = guess
            form.result = if guess in self.target
            form.progress = # TODO finish this up
        return history


class StringMessage(messages.Message):
    """Convenience class for single line responses"""
    message = messages.StringField(1, required=True)


class GameForm(messages.Message):
    """Visual representation of a game"""
    a_key = messages.StringField(1, required=True)
    b_status = messages.StringField(2, required=True)
    d_guesses = messages.StringField(3, required=True)
    c_spaces = messages.StringField(4, required=True)


class GameList(messages.Message):
    """List of user's active games"""
    games = messages.MessageField(GameForm, 1, repeated=True)


class ScoreForm(messages.Message):
    """Form for returning a score, nested in ScoreTable"""
    user_name = messages.StringField(1, required=True)
    score = messages.IntegerField(2, required=True)


class ScoreTable(messages.Message):
    """Table for the topscores"""
    items = messages.MessageField(ScoreForm, 1, repeated=True)


class HistoryMessage(messages.Message):
    """Message for holding move forms"""
    history = messages.MessageField(MoveForm, 1, repeated=True)


class MoveForm(messages.Message):
    """Form representation of a move"""
    guess = messages.StringField(1, required=True)
    result = messages.BooleanField(2, required=True)
    progress = messages.StringField(3, required=True)
