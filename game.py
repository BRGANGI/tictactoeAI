from ai import PlayerAI
from board import Board
from constants import SWITCH_TURN, X, O, DRAW

class Game:
    def __init__(self):
        self.player_name = input("What is your name? ")
        while True:
            self.player_symbol = input("Would you like to go naughts or crosses (X / O)? ")
            if self.player_symbol == X or self.player_symbol == O:
                break
            print("Please input 'X' or 'O'")
        while True:
            first = input("Who do you want to go first (X / O)? ")
            if first == X or first == O:
                self.board = Board(first)
                break
            print("Please input 'X' or 'O'")
        self.ai_player = PlayerAI("AI", SWITCH_TURN[self.player_symbol], True)
        print(f"AI is generating their tree...")
        self.ai_player.game_tree = self.ai_player.generate_game_tree(self.board, None)
        print("Game start!")
        self.board.print_board()

    def get_move(self):
        print(f"----{self.board.turn}'s turn----")
        if self.board.turn == self.ai_player.symbol:
            if self.board.turn_no == 1:
                self.ai_player.game_tree = self.ai_player.move_down(self.ai_player.game_tree, self.board.state)
            if self.board.turn_no <= 1:
                self.ai_player.minimax(self.ai_player.game_tree, True)
            cur_name = self.ai_player.name
            move = self.ai_player.choose_move(self.board)
            self.board.make_move(move, True)   
        else:
            cur_name = self.player_name
            while True:
                move = input("Where would you like to move? Input coordinate in format <X> <Y>: ")
                if move != 1:
                    self.board.make_move(move, False) == 1
                    break

        print(f"\n{cur_name} moved to {move[0]},{move[2]}")
        self.board.print_board()

    def get_winner(self):
        if self.board.check_end() == DRAW:
            print("Tied game!")
            return
        
        if self.board.turn == self.ai_player.symbol:
            winner = self.player_name
        else:
            winner = self.ai_player.name

        print(f"{winner} has won the game!")