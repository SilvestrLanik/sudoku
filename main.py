from Sudoku.board import Board
from Sudoku.solver import Solver


def main():
    sudoku = Board(9)
    solver = Solver(sudoku)

    sudoku.grid = [
        [0, 8, 0, 0, 6, 3, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 9],
        [4, 6, 1, 9, 0, 0, 3, 0, 0],
        [8, 0, 0, 0, 2, 0, 6, 0, 0],
        [2, 7, 0, 0, 0, 0, 0, 9, 1],
        [0, 0, 6, 0, 9, 0, 0, 0, 7],
        [0, 0, 9, 0, 0, 8, 4, 1, 6],
        [7, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 5, 1, 0, 0, 2, 0],
    ]
    sudoku.print_board()

    solver.solve()

    sudoku.print_board()


if __name__ == '__main__':
    main()
