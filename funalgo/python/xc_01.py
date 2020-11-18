import itertools
import numpy as np

level = 8
board = [[0 for i in range(level)] for j in range(level)]
res = None


def sudoku():
    return backtrack(0)


def backtrack(index):
    if index >= level * level:
        return True
    next_row = index // level
    next_col = index % level
    for num in range(1, level + 1):
        if not is_valid(num, next_row, next_col):
            continue
        board[next_row][next_col] = num
        if backtrack(index + 1):
            return True
        board[next_row][next_col] = 0
    return False


def is_valid(num, row, col):
    for i in itertools.chain(range(0, row), range(row, level)):
        if board[i][col] == num:
            return False

    for j in itertools.chain(range(0, col), range(col, level)):
        if board[row][j] == num:
            return False

    return True


if __name__ == '__main__':
    if sudoku():
        print(np.array(board))
