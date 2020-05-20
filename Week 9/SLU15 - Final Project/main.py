from tictactoe import TicTacToe
from players import human_player, computer_player
from constants import CROSS


def main():
    # Create a new game
    game = TicTacToe()
    # Game loop
    while game.running:
        if game.turn == CROSS:
            human_player(game)
        else:
            computer_player(game)


if __name__ == "__main__":
    main()
