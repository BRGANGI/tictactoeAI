from game import Game

def main():
    game = Game()

    while not game.board.check_end():
        game.get_move()

    game.get_winner()


if __name__ == "__main__":
    main()