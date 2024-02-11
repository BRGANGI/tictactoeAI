from py_scripts.game import Game
from py_scripts.constants import NOT_FINISHED
from flask import Flask, request

app = Flask(__name__)

SIDE = None
FIRST = None
GAME = None

@app.route('/symbol', methods=['POST'])
def choose_side():
    global SIDE
    data = request.get_json()
    SIDE = data.get('symbol')
    return 'side:success'

@app.route('/first', methods=['POST'])
def choose_first():
    global FIRST
    data = request.get_json()
    FIRST = data.get('first')
    return 'first:success'

@app.route('/start')
def start():
    global GAME
    GAME = Game(SIDE, FIRST)
    return 'game:success'


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
