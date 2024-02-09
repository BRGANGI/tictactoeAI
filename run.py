from py_scripts.game import Game
from py_scripts.constants import NOT_FINISHED
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

SYMBOL = 'X'  

@app.route('/button_click', methods=['POST'])
def button_click():
    global SYMBOL 
    if SYMBOL == 'X':
        SYMBOL = 'O'
    else:
        SYMBOL = 'X'
    return jsonify(SYMBOL)

@app.route('/main', methods=['POST'])
def main():
    print("here")
    game = Game()

    while game.board.check_end() == NOT_FINISHED:
        game.get_move()
    game.get_winner()

if __name__ == '__main__':
    app.run(debug=True)





