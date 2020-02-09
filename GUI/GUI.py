import pygame

from Sudoku.GUI.Colors import *
from Sudoku.Logic.constants import SIZE
from Sudoku.Tests.examples import *
from Sudoku.Logic.board import Board
from Sudoku.Logic.solver import Solver

from Sudoku.GUI.Grid import Grid

pygame.init()


def redraw(display, grid):
    display.fill(BLACK)
    grid.draw()

def main():
    display_w = 600
    display_h = 600

    game_display = pygame.display.set_mode((display_w, display_h))
    pygame.display.set_caption("Sudoku")

    sudoku = Board(SIZE)
    solver = Solver(sudoku)
    sudoku.grid = test_sudokus[0]

    grid = Grid(game_display, display_w, sudoku.grid)
    run = True
    key = None

    grid.draw()
    pygame.display.update()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    pass
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_RETURN: #enter
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = grid.click(pos)
                if clicked:
                    grid.select(clicked[0], clicked[1])

        if grid.selected and key:
            grid.insert(key)
            key = None

        redraw(game_display, grid)
        pygame.display.update()

main()
pygame.quit()


