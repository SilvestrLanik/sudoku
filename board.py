import math
import numpy as np
from Sudoku.constants import *


class Board:
    # size is the maximum value in sudoku. For traditional one it is 9
    def __init__(self, size):
        self.grid = [[EMPTY] * size for i in range(size)]
        self.size = size
        self.square_size = int(math.sqrt(self.size))  # size of inner square, for traditional sudoku it is 3

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.grid[i][j], " ", end='')  # prevent from printing each number on different line
                if j % self.square_size == self.square_size - 1:
                    print("|  ", end='')
            print()
            if i % self.square_size == self.square_size - 1:
                print("-----------------------------------")  # for bigger sudoku it must be rewritten to loop

    def print_board_commas(self):
        for i in range(self.size):
            print("[", end='', sep = '')
            for j in range(self.size):
                if j != self.size - 1:
                    # prevent from printing each number on different line
                    print(self.grid[i][j], ", ", end='', sep='')
                else:
                    print(self.grid[i][j], end='', sep='')
            print("],")
