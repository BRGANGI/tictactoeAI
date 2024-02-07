from game import Game
from constants import NOT_FINISHED

def main():
    game = Game()

    while game.board.check_end() == NOT_FINISHED:
        game.get_move()

    game.get_winner()


if __name__ == "__main__":
    main()