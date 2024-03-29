import unittest.mock
from TicTacGame import TicTacGame
import io


class TestTicTacGame(unittest.TestCase):

    def setUp(self) -> None:
        self.game = TicTacGame()

    def test_validate_input(self):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()):
            self.assertEqual(self.game.validate_input(3, 4), False)
            self.assertEqual(self.game.validate_input(4, 2), False)
            self.assertEqual(self.game.validate_input(" ", " "), False)
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
        with unittest.mock.patch('sys.stdout', new=io.StringIO()):
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

    @unittest.mock.patch("TicTacGame.TicTacGame.coord_input")
    def test_start_game(self, coord_input_mock):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()):
            self.game.cls_gameField = [[-1, 1, 0],
                                       [-1, 1, 1],
                                       [-1, 1, 1]]
            coord_input_mock.return_value = [1, 1]
            self.assertEqual(self.game.start_game(), True)

            self.game.cls_gameField = [[0, 1, 0],
                                       [0, 1, 1],
                                       [0, 1, 1]]
            coord_input_mock.return_value = [" ", 1]
            self.assertEqual(self.game.start_game(), True)

            self.game.cls_gameField = [[-1, 1, -1],
                                       [-1, 1, 1],
                                       [1, -1, 1]]
            coord_input_mock.return_value = [" ", 1]
            self.assertEqual(self.game.start_game(), True)


if __name__ == '__main__':
    unittest.main()
