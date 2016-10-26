# Full Stack Nanodegree Project 4: Hangman

## Set-Up Instructions:

1. Download the repository from GitHub. Update the value of application in app.yaml to the app ID you have registered in the App Engine admin console and would like to use to host your instance of this sample.
2. Run the app with the devserver using dev_appserver.py DIR, and ensure it's running by visiting the API Explorer - by default localhost:8080/_ah/api/explorer.
3. (Optional) Generate your client library(ies) with the endpoints tool. Deploy your application.

## Game Description:

Hangman is a simple letter guessing game. Each game begins with a random 'target' word drawn randomly from a wordbank (included on server). 'Guesses' are sent to the `guess_a_letter` endpoint which will reply with either updating the target string's blank spaces (if the letter guessed is in the string) or decrementing the 'remaining_attempts' field (if the letter is not in the string). In both cases, the game's history is updated. Many different Hangman games can be played by many different Users at any given time. Each game can be retrieved or played by using the path parameter `urlsafe_game_key`.

**NOTE**

- This project's architecture was provided by Udacity and has only been slightly modified to meet the logical concerns of the game Hangman. Many names, function patterns, and logic has been borrowed from this provided 'Skeleton'

## Scoring

Hangman has two forms of scoring, single game scores and user rankings. Your  single game score is the number of remaining guesses when a user wins a game; no score is recorded if the user fails to guess the target in fewer than 6 guesses. For user rankings, users are ranked by the difference between their number of wins and losses. EX: User "Drew" has 5 wins and 2 losses, his ranking score is 3. The higher the ranking (compared to other users) the higher a user will place on the scoreboard. 

## Files Included:

- api.py: Contains endpoints and calls to the game playing logic.
- app.yaml: App configuration.
- cron.yaml: Cronjob configuration for email reminders.
- main.py: Handler for Cronjob.
- game.py: Logic for the Hangman game.
- models.py: Entity and message definitions including helper methods.
- utils.py: get_url_safe method from Udacity's Skeleton Project
- wordbank.txt: List of words that will be used as the target in each game

## Endpoints Included:

- **create_user**

  - Description: Creates a new User. user_name provided must be unique. Will raise a ConflictException if a User with that user_name already exists.

- **create_game**

  - Description: Creates a new Game. user_name provided must correspond to an existing user - will raise a NotFoundException if not.

- **guess_a_letter**

  - Description: Accepts a 'guess' and returns the updated state of the game. If this results in winning a game, a corresponding Score entity will be created.

- **get_high_scores**

  - Description: Returns all Scores in the database ordered from high to low.

- **get_user_scores**

  - Description: Returns all Scores recorded by the provided player (unordered). Will raise a NotFoundException if the User does not exist.

- **get_user_games**

  - Description: Retrieves all the active games for the provided user

- **cancel_game**

  - Description: When given a urlsafe_game_key, this endpoint will delete the corresponding game

- **get_user_rankings**

  - Description: Returns an ordered list of users, ranked from highest win-loss differential to lowest.

- **get_game_history**

  - Description: Returns a string of characters that have been guessed during the course of a game

## Models Included:

- **User**

  - Stores unique user_name and (optional) email address.

- **Game**

  - Stores unique game states. Associated with User model via KeyProperty.
  - Includes methods for creating new games, ending a game, returning a game's score, and outputting the game state for a message class

- **Score**

  - Records completed games. Associated with Users model via KeyProperty.
  - Includes methods for outputting the Score in a message class

## Forms Included:

- **StringMessage**

  - General purpose String container.

- **GameForm**

  - Representation of a Game's state (urlsafe_key, attempts_remaining, previous guesses, and filled/remaining matches).

- **GameList**

  - Message class meant to hold multiple game forms.

- **ScoreForm**

  - Message used to represent a score entry.

- **ScoreTable**

  - Multiple ScoreForm container.
