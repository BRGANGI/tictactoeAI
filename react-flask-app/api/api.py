from py_scripts.game import Game
from py_scripts.constants import NOT_FINISHED
from flask import Flask, request

app = Flask(__name__)

SIDE = None
FIRST = None
GAME = None



#choose side
@app.route('/symbol', methods=['POST'])
def choose_side():
    global SIDE
    data = request.get_json()
    SIDE = data.get('symbol')
    print(SIDE)
    return 'side:success'

#choose who goes first
@app.route('/first', methods=['POST'])
def choose_first():
    global FIRST
    data = request.get_json()
    FIRST = data.get('first')
    print(FIRST)
    return 'first:success'

#game = Game(player_name, player_symbol, first)
@app.route('/start')
def start():
    print("here")
    global GAME
    GAME = Game(SIDE, FIRST)
    return 'game:success'


@app.route('/move', methods=['POST'])
def move():
    if GAME.board.turn == SIDE:
        data = request.get_json()
        move = str(data.get('coord'))
        print("chosen move")
        print(move)
        GAME.get_move(move)
    if GAME.board.check_end() != NOT_FINISHED:
        return {'opp_move' : "", 'winner': GAME.get_winner()}
    opp_move = GAME.get_move()
    print("opp_move")
    print(opp_move)
    return {'opp_move' : opp_move, 'winner': GAME.get_winner()}

    # while game.board.check_end() == NOT_FINISHED:
    #     game.get_move()
    # game.get_winner()




if __name__ == '__main__':
    app.run(debug=True)
