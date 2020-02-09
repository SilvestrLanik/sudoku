import pygame

from Sudoku.GUI.Colors import *
from Sudoku.Logic.constants import EMPTY


class Box:
    def __init__(self, display, width, value, row, column):
        self.row = row
        self.column = column
        self.display = display
        self.width = width
        self.value = value
        self.correct = True;
        self.selected = False
        self.unchangeable = False

        if value != EMPTY:
            self.unchangeable = True

    def set_value(self, value):
        if not self.unchangeable:
            self.value = value

    def draw(self):
        font = pygame.font.Font("freesansbold.ttf", 45)

        x = self.width * self.column
        y = self.width * self.row

        if self.value != EMPTY:
            if self.unchangeable:
                text = font.render(str(self.value), True, WHITE)
            else:
                if self.correct:
                    text = font.render(str(self.value), True, BLUE)
                else:
                    text = font.render(str(self.value), True, RED)
            self.display.blit(text, (x + (self.width/2 - text.get_width()/2), y + (self.width/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(self.display, RED, (x, y, self.width, self.width), 4)





