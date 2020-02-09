import pygame

from Sudoku.GUI.Box import Box
from Sudoku.GUI.Colors import *
from Sudoku.Logic.constants import *


class Grid:
    def __init__(self, display, width, grid):
        self.display = display
        self.width = width
        self.grid = grid
        self.boxes = [[EMPTY] * SIZE for i in range(SIZE)]
        self.boxes = [[Box(display, self.width / SIZE, self.grid[i][j], i, j) for j in range(SIZE)] for i in range(SIZE)]

    def draw(self):
        size_of_box = self.width / SIZE

        for i in range(SIZE + 1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.display, WHITE, (0, i * size_of_box), (self.width, i * size_of_box), thickness)
            pygame.draw.line(self.display, WHITE, (i * size_of_box, 0), (i * size_of_box, self.width), thickness)

        for i in range(SIZE):
            for j in range(SIZE):
                self.boxes[i][j].draw()
