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
        try:
            x = int(x)
        except ValueError:
            print("Incorrect value: x coordinate")
            return False
        try:
            y = int(y)
        except ValueError:
            print("Incorrect value: y coordinate")
            return False

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

    def coord_input(self):
        print("x coordinate")
        x = input()
        print("y coordinate")
        y = input()

        return x, y

    def start_game(self):

        step = True
        while True:
            self.show_board()
            print("Enter coordinates")
            if step:
                print("X step:")
            else:
                print("O step:")

            x, y = self.coord_input()

            if self.validate_input(x, y):
                x = int(x)
                y = int(y)
                self.cls_gameField[x][y] = 1 if step else -1
                step = not step

            if self.check_winner() == 1:
                self.show_board()
                print("X wins")
                return True
            if self.check_winner() == 2:
                self.show_board()
                print("O wins")
                return True

            if self.check_draw():
                print("Draw")
                return True


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
