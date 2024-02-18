# constants.py

LENGTH = 3    # Length of a single dimension of the game board. Note increasing length can significantly increase 
              # minimax runtime. Implementation of higher lengths have not been implemented into react either.

EMPTY = " "                 # Denotes empty string (eg for an empty board space)
X = "X"                     # Crosses symbol
O = "O"                     # Naughts symbol
SWITCH_TURN = {X:O, O:X}    # Operation that allows quick switching of turns

# Minimax evaluation values
WIN = 1
LOSE = -1
DRAW = 0

# Game state evaluation values
FINISHED = 1
NOT_FINISHED = -1

