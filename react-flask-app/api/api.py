# api.py
# The bridge between the backend (python scripts) and frontend (react app)
# Uses flask to allow react to invoke functions that run various scripts in the backend

from py_scripts.game import Game
from py_scripts.constants import NOT_FINISHED
from flask import Flask, request

app = Flask(__name__)

# Global variables for a given gamestate
# Indicates which side the player chose (X/O), who goes first (X/O) and holds the Game object for the
# current game
SIDE = None
FIRST = None
GAME = None

# Choose symbol for player
@app.route('/symbol', methods=['POST'])
def choose_side():
    global SIDE
    data = request.get_json()
    SIDE = data.get('symbol')
    return 'side:success'

# Choose who goes first
@app.route('/first', methods=['POST'])
def choose_first():
    global FIRST
    data = request.get_json()
    FIRST = data.get('first')
    return 'first:success'

# Initialise game by creating a new Game object
@app.route('/start')
def start():
    global GAME
    GAME = Game(SIDE, FIRST)
    return 'game:success'


# Makes a move. React app sends data of which square was clicked. Coords are parsed 
# and sent to game object to make a move. Then makes a move for the ai player and returns
# that move to be displayed on react app.
# Returns dictionary with the opponents move, and the winner.
# If there is no winner it will return "", which indicates to the frontend that the game is
# still going, otherwise returns 'X'/'O'
# If the winner is the player, then opp_move will be returned as "", indicating to the fronted
# that an opposing move doesnt need to be parsed and the game can end.
@app.route('/move', methods=['POST'])
def move():
    if GAME.board.turn == SIDE:
        data = request.get_json()
        move = str(data.get('coord'))
        GAME.get_move(move)
    if GAME.board.check_end() != NOT_FINISHED:
        return {'opp_move' : "", 'winner': GAME.get_winner()}
    opp_move = GAME.get_move()
    return {'opp_move' : opp_move, 'winner': GAME.get_winner()}


if __name__ == '__main__':
    app.run(debug=True)
