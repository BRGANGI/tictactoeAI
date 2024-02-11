from py_scripts.ai import PlayerAI
from py_scripts.board import Board
from py_scripts.constants import SWITCH_TURN, X, O, DRAW, NOT_FINISHED

class Game:
    def __init__(self, player_symbol, first):
        self.player_symbol = player_symbol
        self.board = Board(first)
        self.ai_player = PlayerAI("AI", SWITCH_TURN[self.player_symbol], first)

    def get_move(self, move_chosen = None):
        if self.board.turn == self.ai_player.symbol:
            move = self.ai_player.choose_move(self.board)
            self.board.make_move(move, True)   
        else:
            move = move_chosen
            self.board.make_move(move, False)
        return str(move)

    def get_winner(self):
        if self.board.check_end() == NOT_FINISHED:
            return ""
        if self.board.check_end() == DRAW:
            return "tie"
        if self.board.turn == self.ai_player.symbol:
            winner = self.player_symbol
        else:
            winner = self.ai_player.symbol
        return winner
