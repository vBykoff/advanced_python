class TicTacGame:

    def __init__(self):
        self.cls_gameField = [[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]

    def check_winner(self):
        # vertical check
        for i in range(3):
            sum_str = sum([self.cls_gameField[j][i] for j in range(3)])

            if sum_str == 3:
                return 1
            if sum_str == -3:
                return 2

        # horizontal check
        for i in self.cls_gameField:
            sum_str = sum(i)

            if sum_str == 3:
                return 1
            if sum_str == -3:
                return 2

        # diagonal check

        # first diagonal
        sum_diag = sum(self.cls_gameField[i][i] for i in range(3))
        if sum_diag == 3:
            return 1
        if sum_diag == -3:
            return 2

        # second diagonal
        sum_diag = sum(self.cls_gameField[i][2 - i] for i in range(3))
        if sum_diag == 3:
            return 1
        if sum_diag == -3:
            return 2

        return 0

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.cls_gameField[i][j] == 0:
                    return False
        return True

    def print_x_or_o(self, i, j):
        if self.cls_gameField[i][j] == 1:
            return "X"
        if self.cls_gameField[i][j] == -1:
            return "O"
        if self.cls_gameField[i][j] == 0:
            return " "

    def show_board(self):
        for i in range(3):
            print("| %s %s %s |" % (self.print_x_or_o(i, 0),
                                    self.print_x_or_o(i, 1),
                                    self.print_x_or_o(i, 2)))

    def validate_input(self, x, y):
        if x < 0 or x > 2:
            print("Out of dimension, X axis")
            return False

        if y < 0 or y > 2:
            print("Out of dimension, Y axis")
            return False

        if self.cls_gameField[x][y] != 0:
            print("This part of board is already in use")
            return False

        return True

    def start_game(self):

        step = True
        while True:
            self.show_board()
            print("Enter coordinates")
            if step:
                print("X step:")
            else:
                print("O step:")

            x, y = map(int, input().split())

            if self.validate_input(x, y):
                self.cls_gameField[x][y] = 1 if step else -1
                step = not step

            if self.check_winner() == 1:
                self.show_board()
                print("X wins")
                break
            if self.check_winner() == 2:
                self.show_board()
                print("O wins")
                break

            if self.check_draw():
                print("Draw")
                break


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
