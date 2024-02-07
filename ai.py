from contants import X, O, EMPTY, LENGTH
from board import Board
from copy import deepcopy
from random import choice as rand_choice

class Node:
    def __init__(self, board, last_move, parent, is_terminal):
        self.board = board
        self.last_move = last_move
        self.children = []
        self.parent = parent
        self.is_terminal = is_terminal
        self.val = 2

class PlayerAI:
    def __init__(self, name, symbol, is_auto):
        self.name = name

        self.symbol = symbol

        self.is_auto = is_auto
        
        
        self.game_tree = None

    
    def generate_game_tree(self, board, root):
        if root == None:
            root = Node(board, None, None, False) # root node

        potential_boards, potential_moves = self.get_potential_moves(board)

        for cur_board, cur_move in zip(potential_boards, potential_moves):
            if cur_board.check_end():
                node = Node(cur_board, cur_move, root, True)
            else:
                node = Node(cur_board, cur_move, root, False)
            root.children.append(node)
            if node.is_terminal == False:
                node = self.generate_game_tree(cur_board, node)
            else:
                if cur_board.check_end() == -1:
                    node.val = 0
                elif cur_board.turn == self.symbol:
                    node.val = -1
                else:
                    node.val = 1
        root.children.sort(key=lambda x: x.val)
        return root
    
    def minimax(self, node, is_max):
        if node.is_terminal:
            return node.val

        if is_max:
            max_eval = -2
            for child in node.children:
                eval = self.minimax(child, False)
                max_eval = max(eval, max_eval)
            node.val = max_eval
            return max_eval
        else:
            min_eval = 2
            for child in node.children:
                eval = self.minimax(child, True)
                min_eval = min(eval, min_eval)
            node.val = min_eval
            return min_eval
    
    def get_potential_moves(self, board):
        
        potential_boards = []
        potential_moves = []
        for i in range(LENGTH):
            for j in range(LENGTH):
                tmp_board = self.duplicate_board(board)
                move = f"{i} {j}"
                if tmp_board.make_move(move, True) != 1:
                    potential_boards.append(tmp_board)
                    potential_moves.append(move)
        return potential_boards, potential_moves


    def duplicate_board(self, board):
        tmp_board = Board(board.turn)
        tmp_board.state = deepcopy(board.state)
        #tmp_board.turn = board.turn
        #tmp_board.opp_turn = board.opp_turn
        tmp_board.turn_no = board.turn_no
        return tmp_board
    
    def choose_move(self, board):
        if board.state != self.game_tree.board.state:
            self.game_tree = self.move_down(self.game_tree, board.state)

        best_val = -2
        best_nodes = []
        for child in self.game_tree.children:
            if child.val > best_val:
                best_val = child.val
                best_nodes = []
                best_nodes.append(child)
            elif child.val == best_val:
                best_nodes.append(child)
        best_node = rand_choice(best_nodes)
        self.game_tree = self.move_down(self.game_tree, best_node.board.state)
        return best_node.last_move

    def move_down(self, node, state):
        for child in node.children:
            if child.board.state == state:
                return child

    def win_game(self):
        print(f"{self.name} has won the game!")



