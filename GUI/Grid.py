import pygame

from Sudoku.GUI.Box import Box
from Sudoku.GUI.Colors import *
from Sudoku.Logic.constants import *


class Grid:
    def __init__(self, display, width, grid):
        self.display = display
        self.width = width
        self.grid = grid
        self.selected = None
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

    def select(self, row, col):
        if self.boxes[row][col].unchangeable:
            return False

        if self.selected:
            old_row = self.selected[0]
            old_col = self.selected[1]
            self.boxes[old_row][old_col].selected = False

        self.boxes[row][col].selected = True
        self.selected = (row, col)

        return True

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.width:
            size_of_element = self.width / SIZE
            x = pos[0] // size_of_element
            y = pos[1] // size_of_element
            return int(y), int(x)  # indexing is different
        else:
            return None

    def insert(self, key):
        row, col = self.selected
        self.boxes[row][col].set_value(key)

