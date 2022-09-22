import unittest
import unittest.mock
from TicTacGame import TicTacGame
import io
import sys


class TestTicTacGame(unittest.TestCase):

    def setUp(self) -> None:
        self.game = TicTacGame()

    def test_validate_input(self):
        self.assertEqual(self.game.validate_input(3, 4), False)
        self.assertEqual(self.game.validate_input(4, 2), False)
        self.game.cls_gameField[0][0] = 1
        self.assertEqual(self.game.validate_input(0, 0), False)

        self.assertEqual(self.game.validate_input(1, 1), True)

    def test_check_winner(self):
        # first diagonal
        self.game.cls_gameField = [[1, 0, 0],
                                   [0, 1, 0],
                                   [0, 0, 1]]
        self.assertEqual(self.game.check_winner(), 1)
        self.game.cls_gameField = [[-1, 0, 0],
                                   [0, -1, 0],
                                   [0, 0, -1]]
        self.assertEqual(self.game.check_winner(), 2)

        # second diagonal
        self.game.cls_gameField = [[0, 0, 1],
                                   [0, 1, 0],
                                   [1, 0, 0]]
        self.assertEqual(self.game.check_winner(), 1)
        self.game.cls_gameField = [[0, 0, -1],
                                   [0, -1, 1],
                                   [-1, 0, 1]]
        self.assertEqual(self.game.check_winner(), 2)

        # horizontal
        self.game.cls_gameField = [[1, 1, 1],
                                   [-1, 0, 0],
                                   [0, 0, -1]]
        self.assertEqual(self.game.check_winner(), 1)
        self.game.cls_gameField = [[-1, -1, -1],
                                   [-1, 0, 0],
                                   [0, 0, -1]]
        self.assertEqual(self.game.check_winner(), 2)

        # vertical
        self.game.cls_gameField = [[1, 0, 0],
                                   [1, 0, 0],
                                   [1, 0, 0]]
        self.assertEqual(self.game.check_winner(), 1)
        self.game.cls_gameField = [[-1, 0, 0],
                                   [-1, 0, 0],
                                   [-1, 0, 0]]
        self.assertEqual(self.game.check_winner(), 2)

    def test_check_draw(self):
        self.assertEqual(self.game.check_draw(), False)
        self.game.cls_gameField = [[-1, 1, 1],
                                   [-1, 1, 1],
                                   [-1, 1, 1]]
        self.assertEqual(self.game.check_draw(), True)

    def test_print_x_or_o(self):
        self.game.cls_gameField = [[-1, 1, 0],
                                   [-1, 1, 1],
                                   [-1, 1, 1]]
        self.assertEqual(self.game.print_x_or_o(0, 0), "O")
        self.assertEqual(self.game.print_x_or_o(1, 1), "X")
        self.assertEqual(self.game.print_x_or_o(0, 2), " ")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_show_board(self, mock_stdout):
        self.game.cls_gameField = [[1, -1, 1],
                                   [0, 0, 0],
                                   [0, 1, 0]]
        self.game.show_board()
        self.assertEqual(mock_stdout.getvalue(), "| X O X |\n"
                                                 "|       |\n"
                                                 "|   X   |\n")


if __name__ == '__main__':
    unittest.main()
