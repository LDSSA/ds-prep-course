import random

import pygame

from tictactoe import TicTacToe
from pygame_utils import get_event
from constants import CROSS, BALL


def human_player(game: TicTacToe):
    """
        Function that handles the logic of an Human playing the game.
        We receive the pygame event, check if it is a click on the screen,
        an then, based on the clicked square, we update the game state and
        the screen.
    """
    while True:  # Wait for a valid movement
        event = get_event()
        if event.type == pygame.QUIT:
            game.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(
                f"mouse at pixels position x={event.pos[0]} y={event.pos[1]}"
            )
            square_pos = TicTacToe.get_row_col_from_pixels(event.pos)
            print(
                f"clicked on the square on row {square_pos[0]}"
                f"and column {square_pos[1]}"
            )
            # Check if the move is valid, i.e, the user clicked
            # on a empty position
            if game.check_valid_move(square_pos):
                game.play(square_pos, CROSS)
                break
        pygame.display.flip()


def computer_player(game: TicTacToe):
    """
        Function that handles the logic of the computer playing the game.
        This simple version choses a random empty position.
    """
    # Get all the free positions in the game
    free_pos = game.get_empty_positions()
    if len(free_pos) == 0:
        return
    square_pos = random.choice(free_pos)
    pygame.time.wait(500)
    game.play(square_pos, BALL)
