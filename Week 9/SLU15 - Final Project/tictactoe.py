from typing import List, Tuple

from constants import (
    BALL,
    CROSS,
    NO_WINNER,
    DRAW,
    EMPTY,
    LEFT_CORNERS,
)

from pygame_utils import (
    set_up_screen,
    load_images,
    show_message,
    show_image
)


class TicTacToe():
    def __init__(self, state=None, setup_pygame: bool = True):
        # The game stage is a 3x3 matrix.
        # Each entry is the state of the corresponding square
        self.state = state
        if self.state is None:
            self.state = [
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
            ]

        # Boolean variable that indicates if the game stills running
        self.running = True

        # Cross player starts to play
        self.turn = CROSS

        if setup_pygame:
            self.screen = set_up_screen()
            self.ball_image, self.cross_image = load_images()

    def quit(self):
        """
            This method stops the game.
        """
        self.running = False

    @staticmethod
    def _get_square_left_corner(square_pos: Tuple[int, int]):
        row = square_pos[0]
        col = square_pos[1]
        return LEFT_CORNERS[row][col]

    @staticmethod
    def get_row_col_from_pixels(
        pixel_coord: Tuple[int, int]
    ) -> Tuple[int, int]:
        """
            Convert pixel coordinates to the corresponding square on
            our game

        Arguments:
            pixel_coord {Tuple[int, int]} -- Pixel coordinates that we receive
            from pygame (x, y). Referer to the image ./assets/coordinates.png
            in order to find the axis orientation.

        Returns:
            Tuple -- Row Col coordinates (row, col)
        """
        row, col = None, None

        # compute row
        # row =

        # compute col
        # col =

        return row, col

    def _fill_square(self, square_pos: Tuple[int, int], symbol: int):
        """
            This function fill the square on the position square_pos with
            the symbol provided.
        Arguments:
            square_pos {Tuple[int, int]} -- Position to fill
            symbol {int} -- Symbol, CROSS or BALL

        Raises:
            ValueError: If the provided value is not CROSS or BALL, we will
            generate a ValueError exception.
        """
        if symbol == BALL:
            image = self.ball_image
        elif symbol == CROSS:
            image = self.cross_image
        else:
            raise ValueError("Invalid Symbol")
        show_image(
            self.screen,
            TicTacToe._get_square_left_corner(square_pos),
            image
        )

    def _print_winner(self, symbol: int):
        """
           Print the winner on the screen
        Arguments:
            symbol {int} -- [The winner, CROSS or BALL]
        """
        if symbol == CROSS:
            show_message(self.screen, "Cross Player has won")
        else:
            show_message(self.screen, "Ball Player has won")

    def _print_draw(self):
        """
           Print DRAW on the screen
        """
        show_message(self.screen, "Draw")

    def check_winner(self) -> int:
        """
            This function checks if there is a winner on the game.
            If there is a winner, we should return an integer that represents
            the winner. CROSS or BALL
            If there is no more empty positions, we have a draw and we should
            return DRAW.
            If there is empty positions and there is no winner, we should return
            NO_WINNER.
            Plese make sure to use the constants that are defined on the constants
            file. Take a look on it in order to understand the result for the
            tests.
        Returns:
            [int] -- the winner (CROSS or BALL), DRAW or NO_WINNER
        """
        # check in someone have win in rows

        # check in someone have win in columns

        # check in someone have win in Diagonals
        # return BALL
        # return CROSS

        # Check for a draw
        # empty_positions = self.get_empty_positions()
        # return DRAW
        return NO_WINNER

    def check_valid_move(self, square_pos: Tuple[int, int]) -> bool:
        """
            This function receives the square where the user have clicked
            and tells if it is a valid click or not.
            For now, a valid click is a click on a Empty Square.

        Arguments:
            square_pos {Tuple[int, int]} -- Square Clicked by the user

        Returns:
            bool -- Is a valid click?
        """
        (row, col) = square_pos
        if (row is not None) and (col is not None):
            if self.state[row][col] == EMPTY:
                return True
            else:
                return False
        else:
            return False

    def get_empty_positions(self) -> List[Tuple[int, int]]:
        """
            This method return all the empty board positions.
        Returns:
            List[Tuple[int, int]] -- [Empty positions]
        """
        empty_pos = []
        # Your code goes here
        # append to the list all the empty positions on the board
        return empty_pos

    def play(self, square_pos: Tuple[int, int], symbol: int):
        """ This method allows

        Arguments:
            square_pos {Tuple[int, int]} -- [description]
            symbol {int} -- [description]
        """
        # update internal game state
        (row, col) = square_pos
        self.state[row][col] = symbol
        # update screen
        self._fill_square(square_pos, self.turn)
        # change turn
        if self.turn == CROSS:
            self.turn = BALL
        else:
            self.turn = CROSS
        # Check winner
        winner = self.check_winner()
        if winner != NO_WINNER:
            self.turn = CROSS  # Enable clicks to close the screen
            if winner == CROSS:
                show_message(self.screen, 'Cross Player won')
            elif winner == BALL:
                show_message(self.screen, 'Ball Player won')
            else:
                show_message(self.screen, 'Draw')
