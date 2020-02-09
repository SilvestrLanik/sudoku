import math
from Sudoku.constants import *


class Board:
    #TODO comment size
    def __init__(self, size):
        self.grid = [[EMPTY] * size for i in range(size)]
        self.size = size
        self.square_size = int(math.sqrt(self.size))  #size of inner square, for traditional sudoku it is 3

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.grid[i][j], " ", end='')  # prevent from printing each number on different line
                if j % self.square_size == self.square_size - 1:
                    print("|  ", end='')
            print()
            if i % self.square_size == self.square_size - 1:
                print("-----------------------------------")  # for bigger sudoku it must be rewritten to loop
