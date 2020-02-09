from Sudoku.constants import *


class Solver:

    def __init__(self, board):
        self.board = board

    # find first empty box and return its position. None otherwise
    def find_empty(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.grid[i][j] == EMPTY:
                    pos = i, j
                    return pos

        return None

    # checking if the row is correct with new inserted number on pos
    def check_row(self, pos, number):
        for j in range(self.board.size):
            if self.board.grid[pos[0]][j] == number and pos[1] != j:
                return False

        return True

    # checking if the column is correct with new inserted number on pos
    def check_column(self, pos, number):
        for i in range(self.board.size):
            if self.board.grid[i][pos[1]] == number and pos[0] != i:
                return False

        return True

    # checking if the inner square is correct with new inserted number on pos
    def check_square(self, pos, number):
        # compute the starting and ending coordinates of square in which the number was inserted
        start_i = pos[0] - ( pos[0] % self.board.square_size)
        end_i = start_i + self.board.square_size

        start_j = pos[1] - ( pos[1] % self.board.square_size)
        end_j = start_j + self.board.square_size

        for i in range(start_i, end_i):
            for j in range(start_j, end_j):
                if self.board.grid[i][j] == number and (pos[0] != i or pos[1] != j):
                    return False

        return True

    def solve(self):
        pos = self.find_empty()
        if not pos:

            return True

        for i in range(1, self.board.size + 1):
            if self.check_row(pos, i) and self.check_column(pos, i) and self.check_square(pos, i):
                self.board.grid[pos[0]][pos[1]] = i
                if self.solve():
                    return True

        self.board.grid[pos[0]][pos[1]] = EMPTY
        return False



