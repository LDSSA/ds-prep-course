import unittest
from tictactoe import TicTacToe
from constants import EMPTY, CROSS, BALL, NO_WINNER, DRAW


class TestTicTacToe(unittest.TestCase):
    def test_get_row_col_from_pixels(self):
        self.assertEqual(
            type(
                TicTacToe.get_row_col_from_pixels(
                    (100, 100)
                )
            ),
            tuple,
            msg='Please check that the return type of your function is Tupple'
        )
        self.assertEqual(
            TicTacToe.get_row_col_from_pixels(
                (100, 100)
            ),
            (0, 0),
            msg='Wrong position'
        )
        self.assertEqual(
            TicTacToe.get_row_col_from_pixels(
                (350, 350)
            ),
            (1, 1),
            msg='Wrong position'
        )
        self.assertEqual(
            TicTacToe.get_row_col_from_pixels(
                (550, 550)
            ),
            (2, 2),
            msg='Wrong position'
        )
        self.assertEqual(
            TicTacToe.get_row_col_from_pixels(
                (100, 100)
            ),
            (0, 0),
            msg='Wrong position'
        )
        self.assertEqual(
            TicTacToe.get_row_col_from_pixels(
                (350, 100)
            ),
            (0, 1),
            msg='Wrong position'
        )
        self.assertEqual(
            TicTacToe.get_row_col_from_pixels(
                (550, 100)
            ),
            (0, 2),
            msg='Wrong position'
        )
        self.assertEqual(
            TicTacToe.get_row_col_from_pixels(
                (100, 350)
            ),
            (1, 0),
            msg='Wrong position'
        )
        self.assertEqual(
            TicTacToe.get_row_col_from_pixels(
                (550, 350)
            ),
            (1, 2),
            msg='Wrong position'
        )
        self.assertEqual(
            TicTacToe.get_row_col_from_pixels(
                (100, 550)
            ),
            (2, 0),
            msg='Wrong position'
        )

    def test_check_winner(self):
        game = TicTacToe(
            state=[
                [BALL, EMPTY, CROSS],
                [BALL, CROSS, EMPTY],
                [BALL, CROSS, CROSS],
            ],
            setup_pygame=False,
        )
        self.assertEqual(
            game.check_winner(),
            BALL,
            msg="""
                wrong winner, BALL have won on columns
                [
                    [BALL, EMPTY, CROSS],
                    [BALL, CROSS, EMPTY],
                    [BALL, CROSS, CROSS],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [CROSS, EMPTY, BALL],
                [CROSS, BALL, EMPTY],
                [CROSS, BALL, BALL],
            ]
        )
        self.assertEqual(
            game.check_winner(),
            CROSS,
            msg="""
                wrong winner, CROSS have won on columns
                [
                    [CROSS, EMPTY, BALL],
                    [CROSS, BALL, EMPTY],
                    [CROSS, BALL, BALL],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [EMPTY, CROSS, BALL],
                [BALL,  CROSS, EMPTY],
                [BALL,  CROSS, BALL],
            ]
        )
        self.assertEqual(
            game.check_winner(),
            CROSS,
            msg="""
                wrong winner, CROSS have won on columns
                [
                    [EMPTY, CROSS, BALL],
                    [BALL,  CROSS, EMPTY],
                    [BALL,  CROSS, BALL],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [EMPTY, BALL, CROSS],
                [BALL, EMPTY, CROSS],
                [BALL, BALL, CROSS],
            ]
        )
        self.assertEqual(
            game.check_winner(),
            CROSS,
            msg="""
                wrong winner, CROSS have won on columns
                [
                    [EMPTY, BALL, CROSS],
                    [BALL,  EMPTY, CROSS],
                    [BALL,  BALL, CROSS],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [CROSS, CROSS, CROSS],
                [BALL, EMPTY, BALL],
                [BALL, BALL, CROSS],
            ]
        )
        self.assertEqual(
            game.check_winner(),
            CROSS,
            msg="""
                wrong winner, CROSS have won on rows
                [
                    [CROSS, CROSS, CROSS],
                    [BALL, EMPTY, BALL],
                    [BALL, BALL, CROSS],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [BALL, EMPTY, BALL],
                [CROSS, CROSS, CROSS],
                [BALL, BALL, CROSS],
            ]
        )
        self.assertEqual(
            game.check_winner(),
            CROSS,
            msg="""
                wrong winner, CROSS have won on rows
                [
                    [BALL, EMPTY, BALL],
                    [CROSS, CROSS, CROSS],
                    [BALL, BALL, CROSS],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [BALL, EMPTY, BALL],
                [BALL, BALL, CROSS],
                [CROSS, CROSS, CROSS],
            ]
        )
        self.assertEqual(
            game.check_winner(),
            CROSS,
            msg="""
                wrong winner, CROSS have won on rows
                [
                    [BALL, EMPTY, BALL],
                    [BALL, BALL, CROSS],
                    [CROSS, CROSS, CROSS],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [CROSS, EMPTY, BALL],
                [BALL, CROSS, BALL],
                [CROSS, BALL, CROSS],
            ]
        )
        self.assertEqual(
            game.check_winner(),
            CROSS,
            msg="""
                wrong winner, CROSS have won on diagonal
                [
                    [CROSS, EMPTY, BALL],
                    [BALL, CROSS, BALL],
                    [CROSS, BALL, CROSS],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [EMPTY, EMPTY, CROSS],
                [BALL, CROSS, BALL],
                [CROSS, BALL, EMPTY],
            ]
        )
        self.assertEqual(
            game.check_winner(),
            CROSS,
            msg="""
                wrong winner, CROSS have won on diagonal
                [
                    [EMPTY, EMPTY, CROSS],
                    [BALL, CROSS, BALL],
                    [CROSS, BALL, EMPTY],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, BALL],
                [CROSS, BALL, EMPTY],
            ]
        )
        self.assertEqual(
            game.check_winner(),
            NO_WINNER,
            msg="""
                wrong winner on game, there in NO_WINNER
                [
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, BALL],
                    [CROSS, BALL, EMPTY],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [CROSS, BALL, BALL],
                [BALL, CROSS, CROSS],
                [CROSS, BALL, BALL],
            ]
        )
        self.assertEqual(
            game.check_winner(),
            DRAW,
            msg="""
                wrong winner, we have a draw here
                [
                    [CROSS, BALL, BALL],
                    [BALL, CROSS, CROSS],
                    [CROSS, BALL, BALL],
                ]
            """
        )

    def test_get_empty_positions(self):
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
            ]
        )
        self.assertEqual(
            type(game.get_empty_positions()),
            list,
            msg="""
                wrong Return type. Your function needs to return a list
            """
        )
        self.assertGreater(
            len(game.get_empty_positions()),
            0,
            msg="""
                The empty positions array is empty. It should have 9 elements.
            """
        )
        self.assertEqual(
            type(game.get_empty_positions()[0]),
            tuple,
            msg="""
                Wrong elements type.
                The elements of your list should be tuples.
            """
        )
        self.assertEqual(
            set(game.get_empty_positions()),
            {
                (0, 0),
                (1, 1),
                (2, 2),
                (1, 2),
                (2, 1),
                (0, 2),
                (2, 0),
                (0, 1),
                (1, 0)
            },
            msg="""
                wrong empty positions
                [
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [CROSS, BALL, BALL],
                [BALL, EMPTY, CROSS],
                [CROSS, BALL, BALL],
            ]
        )
        self.assertEqual(
            set(game.get_empty_positions()),
            {
                (1, 1),
            },
            msg="""
                wrong empty positions
                [
                    [CROSS, BALL, BALL],
                    [BALL, EMPTY, CROSS],
                    [CROSS, BALL, BALL],
                ]
            """
        )
        game = TicTacToe(
            setup_pygame=False,
            state=[
                [CROSS, BALL, BALL],
                [BALL, CROSS, CROSS],
                [CROSS, BALL, BALL],
            ]
        )
        self.assertEqual(
            set(game.get_empty_positions()),
            set(),
            msg="""
                wrong empty positions
                [
                    [CROSS, BALL, BALL],
                    [BALL, CROSS, BALL],
                    [CROSS, BALL, CROSS],
                ]
            """
        )
