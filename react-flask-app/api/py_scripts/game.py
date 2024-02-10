from py_scripts.ai import PlayerAI
from py_scripts.board import Board
from py_scripts.constants import SWITCH_TURN, X, O, DRAW, NOT_FINISHED

class Game:
    def __init__(self, player_symbol, first):
        self.player_name = "default"
        # while True:
        self.player_symbol = player_symbol
        #     if self.player_symbol == X or self.player_symbol == O:
        #         break
        #     print("Please input 'X' or 'O'")
        # while True:
        self.board = Board(first)
            # if first == X or first == O:
            #     
            #     break
            # print("Please input 'X' or 'O'")
        self.ai_player = PlayerAI("AI", SWITCH_TURN[self.player_symbol], first)
        print("Game start!")

        # print("Player name: " + self.player_name)
        # print("Player symbol: " + player_symbol)
        # print("first: " + first)
        self.board.print_board()

    def get_move(self, move_chosen = None):
        print(f"----{self.board.turn}'s turn----")
        if self.board.turn == self.ai_player.symbol:
            if self.board.turn_no <= 1:
                self.ai_player.check_minimax(self.board)
            cur_name = self.ai_player.name
            move = self.ai_player.choose_move(self.board)
            self.board.make_move(move, True)   
        else:
            cur_name = self.player_name
            # while True:
                
            #     #move = input("Where would you like to move? Input coordinate in format <X> <Y>: ")
            #     if  != 1:
            #         break
            move = move_chosen
            self.board.make_move(move, False)
        print(f"\n{cur_name} moved to {move[0]},{move[2]}")
        #self.board.print_board()
        return str(move)

    def get_winner(self):
        if self.board.check_end() == NOT_FINISHED:
            return ""
        if self.board.check_end() == DRAW:
            #print("Tied game!")
            return "tie"
        if self.board.turn == self.ai_player.symbol:
            winner = self.player_symbol
        else:
            winner = self.ai_player.symbol
       # print(f"{winner} has won the game!")
        return winner
