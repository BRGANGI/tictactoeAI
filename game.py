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

        self.ai_symbol = SWITCH_TURN[self.player_symbol]

        self.player = PlayerAI(self.player_name, self.player_symbol, False)
        self.ai_player = PlayerAI("AI", self.ai_symbol, True)

        self.board = Board(input("Who do you want to go first (X / O)? "))

        print("Game start!")
        self.board.print_board()

    def get_move(self):
        if self.board.turn == self.ai_player.symbol and (self.board.turn_no == 0 or self.board.turn_no == 1): 
            print(f"AI is generating their tree...")
            self.ai_player.game_tree = self.ai_player.generate_game_tree(self.board, None)
            self.ai_player.minimax(self.ai_player.game_tree, True)
        

        if self.board.turn == self.ai_player.symbol:
            player = self.ai_player
        else:
            player = self.player

        print(f"----{self.board.turn}'s turn----")
        if self.board.turn == self.ai_player.symbol:

            move = player.choose_move(self.board)
            self.board.make_move(move, player.is_auto)   
        else:
            move = input("Where would you like to move? Input coordinate in format <X> <Y>: ")
            while self.board.make_move(move, player.is_auto) == 1:
                move = input("Where would you like to move? Input coordinate in format <X> <Y>: ")

        print(f"\n{player.name} moved to {move[0]},{move[2]}")
        self.board.print_board()

    def get_winner(self):
        if self.board.check_end() == DRAW:
            print("Tied game!")
        elif self.board.turn == self.ai_player.symbol:
            self.player.win_game()
        else:
            self.ai_player.win_game()