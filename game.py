from player import Player
from board import Board
from contants import X, O, EMPTY, LENGTH

class Game:
    def __init__(self):
        self.x_player = Player(input("Who's playing as crosses?: "), X, input("Would you like them to be an AI player? (y/n): "))
        self.o_player = Player(input("Who's playing as naughts?: "), O, input("Would you like them to be an AI player? (y/n): "))

        self.board = Board(input("Who do you want to go first (X / O)? "))

        print("Game start!")
        self.board.print_board()

    def get_move(self):

        if self.board.turn == X and self.x_player.is_auto and self.board.turn_no == (0 | 1): 
            print(f"Player {self.x_player.name} is generating their tree...")
            self.x_player.game_tree = self.x_player.generate_game_tree(self.board, None)
            self.x_player.minimax(self.x_player.game_tree, True)
        
        if self.board.turn == O and self.x_player.is_auto and self.board.turn_no == (0 | 1):
            print(f"Player {self.o_player.name} is generating their tree...")
            self.o_player.game_tree = self.o_player.generate_game_tree(self.board, None)
            self.o_player.minimax(self.o_player.game_tree, True)

        if self.board.turn == X:
            player = self.x_player
        else:
            player = self.o_player

        print(f"----{player.symbol}' turn----")
        if player.is_auto == False:
            move = input("Where would you like to move? Input coordinate in format <X> <Y>: ")
            while self.board.make_move(move, player.is_auto) == 1:
                move = input("Where would you like to move? Input coordinate in format <X> <Y>: ")
        else:
            move = player.choose_move(self.board)
            self.board.make_move(move, player.is_auto)
        print(f"\n{player.name} moved to {move[0]},{move[2]}")
        self.board.print_board()

    def get_winner(self):
        if self.board.check_end() == -1:
            print("Tied game!")
        elif self.board.turn == O:
            self.x_player.win_game()
        else:
            self.o_player.win_game()