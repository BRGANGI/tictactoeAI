# ai.py
# Contains object for AI player. Currently using minimax algorithm to determine moves

from py_scripts.constants import WIN, LOSE, DRAW, NOT_FINISHED, LENGTH, EMPTY
from py_scripts.board import Board
from copy import deepcopy
from random import choice as rand_choice

# Node for the minimax tree.
class Node:
    def __init__(self, board, last_move, is_terminal):
        self.board = board              # The state of the board
        self.last_move = last_move      # Move made to get to this state
        self.is_terminal = is_terminal  # Whether or not the node is terminal (game finished)
        self.val = None                 # Evaluation of node


class PlayerAI:
    def __init__(self, symbol, first):
        self.symbol = symbol            
        board = Board(first)            # keeps own version of game board to keep track of game

    # Minimax algorithm
    # inspiration from <enter geeksforgeeks url here>
    def minimax(self, node, is_max, alpha, beta):
        potential_boards, potential_moves = self.get_potential_moves(node.board)
        if node.is_terminal:
            node.val = self.assess_board(node.board)
            return node.val, node 
            
        if is_max:
            max_eval = float('-inf')
            max_node = None 
            for cur_board, cur_move in zip(potential_boards, potential_moves):
                child = Node(cur_board, cur_move, cur_board.check_end() != NOT_FINISHED)
                eval, _ = self.minimax(child, False, alpha, beta)
                if eval > max_eval:
                    max_eval = eval
                    max_node = child
                alpha = max(alpha, max_eval)

                if beta <= alpha:
                    break
            node.val = max_eval
            return max_eval, max_node  
        else:
            min_eval = float('inf')
            min_node = None 
            for cur_board, cur_move in zip(potential_boards, potential_moves):
                child = Node(cur_board, cur_move, cur_board.check_end() != NOT_FINISHED)
                eval, _ = self.minimax(child, True, alpha, beta)
                if eval < min_eval: 
                    min_eval = eval
                    min_node = child
                beta = min(beta, min_eval)
                if beta <= alpha:
                    break
            node.val = min_eval
            return min_eval, min_node  
        
    # function that provides the minimax algorithm with a valuation for a node
    def assess_board(self, board):
        if board.check_end() == DRAW:
            return DRAW
        elif board.turn == self.symbol:
            return LOSE
        else:
            return WIN

    # gets all potential moves and board states from a given board state
    def get_potential_moves(self, board):
        potential_boards = []
        potential_moves = []
        unique_states = []
        first = True
        # loop through all tiles and see if a move is possible
        for i in range(LENGTH):
            for j in range(LENGTH):
                tmp_board = self.duplicate_board(board)
                move = f"{i} {j}"
                if tmp_board.make_move(move, True) != 1:
                    # if first or not self.check_symmetric_states(unique_states, tmp_board.state):
                    #     first = False
                        # unique_states.append(tmp_board.state)
                    potential_boards.append(tmp_board)
                    potential_moves.append(move)
        return potential_boards, potential_moves

    # duplicate the game board, used for AI simulation in get_potential_moves 
    def duplicate_board(self, board):
        tmp_board = Board(board.turn)
        tmp_board.state = deepcopy(board.state)
        tmp_board.turn_no = board.turn_no
        return tmp_board
    
    # ai chooses best move given current board state. Does this by initialising a new tree, 
    # and running the minimax algorithm
    def choose_move(self, board):
        root = Node(board, None, False)
        best_val, best_node = self.minimax(root, True, float('-inf'), float('+inf'))
        return best_node.last_move
        
    def check_symmetric_states(self, unique_states, state):
        for _ in range(4):
            if state in unique_states:
                return True
            rotated = self.rotate(state)
            state = rotated
        return False
    
    def rotate(self, state):
        rotated = [[EMPTY] * LENGTH for _ in range(LENGTH)]
        for i in range(LENGTH):
            for j in range(LENGTH):
                rotated[j][LENGTH - 1 - i] = state[i][j]
        return rotated




