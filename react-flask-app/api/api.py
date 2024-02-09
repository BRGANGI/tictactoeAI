from py_scripts.game import Game
from py_scripts.constants import NOT_FINISHED
from flask import Flask, request

app = Flask(__name__)

NAME = None
SIDE = None
FIRST = None
GAME = None

#enter name

@app.route('/name', methods=['POST'])
def input_name():
    global NAME
    data = request.get_json()
    NAME = data.get('name')
    return 'name:success'



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
    game = Game(NAME, SIDE, FIRST)

    return 'game:success'





    # while game.board.check_end() == NOT_FINISHED:
    #     game.get_move()
    # game.get_winner()




if __name__ == '__main__':
    app.run(debug=True)
