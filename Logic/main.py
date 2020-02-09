from Sudoku.Tests.examples import *
from Sudoku.Logic.board import Board
from Sudoku.Logic.solver import Solver


def main():
    sudoku = Board(9)
    solver = Solver(sudoku)

    for i in range(len(test_sudokus)):
        sudoku.grid = test_sudokus[i]
        solver.solve()
        if sudoku.grid != resolved_sudokus[i]:
            print("Dont past test no.", i, "!!!")
        else:
            print("Succesfully passed test no.", i)

if __name__ == '__main__':
    main()
