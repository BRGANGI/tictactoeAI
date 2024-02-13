# game.py
# Keeps track of the overall game state. 
# Can get move and call board to apply the move.
# Can also determine who the winner of the game is.

from py_scripts.ai import PlayerAI
from py_scripts.board import Board
from py_scripts.constants import SWITCH_TURN, DRAW, NOT_FINISHED

class Game:
    def __init__(self, player_symbol, first):
        self.player_symbol = player_symbol                                          # symbol of the main player
        self.board = Board(first)                                                   # main board used for the game
        self.ai_player = PlayerAI(SWITCH_TURN[self.player_symbol], first)     # AI player for the game state

    # Gets move from player or AI and applies it to the board.
    # If a move is passed, it implies that the move being made is that 
    # of the player, otherwise a move is chosen for the AI.
    def get_move(self, move_chosen = None):
        if self.board.turn == self.ai_player.symbol:
            move = self.ai_player.choose_move(self.board)
            self.board.make_move(move, True)   
        else:
            move = move_chosen
            self.board.make_move(move, False)
        return str(move)

    # Determines who won the game
    def get_winner(self):
        if self.board.check_end() == NOT_FINISHED:
            return ""
        elif self.board.check_end() == DRAW:
            return "tie"
        
        return SWITCH_TURN[self.board.turn]
