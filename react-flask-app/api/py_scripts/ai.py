from py_scripts.constants import WIN, LOSE, DRAW, NOT_FINISHED, LENGTH, EMPTY, SWITCH_TURN
from py_scripts.board import Board
from copy import deepcopy
from random import choice as rand_choice

class Node:
    def __init__(self, board, last_move, is_terminal):
        self.board = board
        self.last_move = last_move
        self.children = []
        self.is_terminal = is_terminal
        self.val = float('inf')

class PlayerAI:
    def __init__(self, name, symbol, first):
        self.name = name
        self.symbol = symbol
        self.nodes = 0
        if first == self.symbol:
            board = Board(self.symbol)
        else:
            board = Board(SWITCH_TURN[self.symbol])
        print(f"AI is generating their tree...")
        self.game_tree = self.generate_game_tree(board, None)
        
    def generate_game_tree(self, board, root):
        if root == None:
            root = Node(board, None, False) # root node
        node_count = 0
        potential_boards, potential_moves = self.get_potential_moves(board)
        for cur_board, cur_move in zip(potential_boards, potential_moves):
            if cur_board.check_end() == NOT_FINISHED:
                node = Node(cur_board, cur_move, False)
            else:
                node = Node(cur_board, cur_move, True)
            root.children.append(node)
            self.nodes+=1
            if node.is_terminal == False:
                node = self.generate_game_tree(cur_board, node)
            else:
                if cur_board.check_end() == DRAW:
                    node.val = DRAW
                elif cur_board.turn == self.symbol:
                    node.val = LOSE
                else:
                    node.val = WIN
            
        return root
    
    def minimax(self, node, is_max):
        if node.is_terminal:
            return node.val
        if is_max:
            max_eval = float('-inf')
            for child in node.children:
                eval = self.minimax(child, False)
                max_eval = max(eval, max_eval)
            node.val = max_eval
            return max_eval
        else:
            min_eval = float('inf')
            for child in node.children:
                eval = self.minimax(child, True)
                min_eval = min(eval, min_eval)
            node.val = min_eval
            return min_eval
        
    def check_minimax(self, board):
        if board.turn_no == 1:
            self.game_tree = self.move_down(self.game_tree, board.state)
        self.minimax(self.game_tree, True)
    
    def get_potential_moves(self, board):
        potential_boards = []
        potential_moves = []
        unique_states = []
        first = True
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

    def duplicate_board(self, board):
        tmp_board = Board(board.turn)
        tmp_board.state = deepcopy(board.state)
        tmp_board.turn_no = board.turn_no
        return tmp_board
    
    def choose_move(self, board):
        if board.state != self.game_tree.board.state:
            self.game_tree = self.move_down(self.game_tree, board.state)

        nodes_sorted = sorted(self.game_tree.children, key=lambda child: (child.val,child.is_terminal), reverse=True)
        best_nodes = [node for node in nodes_sorted if (node.is_terminal == nodes_sorted[0].is_terminal and node.val == nodes_sorted[0].val)]

        best_node = rand_choice(best_nodes)
        self.game_tree = self.move_down(self.game_tree, best_node.board.state)

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
    
    def move_down(self, node, state):
        for child in node.children:
            if child.board.state == state:
                return child

        



