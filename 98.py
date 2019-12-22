#!/usr/local/env python3

"""
This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]


def check_coordinate(word, checked_coordinates, x, y):
    """
    O(4*mn^l) (call^depth)
    O(MN)
    """

    # check the validity of coordinates
    if x < 0 or x > (len(board) - 1) or y < 0 or y > (len(board[0]) - 1):
        return False

    # end of the process successfuly
    if len(word) == 0:
        return True

    # not a chain, end the process
    if board[x][y] != word[0]:
        return False

    # if already checked end the process
    if (x, y) in checked_coordinates:
        return False

    checked_coordinates.append((x, y))

    # up
    if check_coordinate(word[1::], checked_coordinates, x - 1, y):
        return True

    # down
    if check_coordinate(word[1::], checked_coordinates, x + 1, y):
        return True

    # left
    if check_coordinate(word[1::], checked_coordinates, x, y - 1):
        return True

    # right
    if check_coordinate(word[1::], checked_coordinates, x, y + 1):
        return True

    # no adjacents, end the process
    return False


def exists(board, word):
    for x, row in enumerate(board):
        for y, _ in enumerate(row):
            if check_coordinate(word, [], x, y):
                return True

    return False


print(exists(board, "ABCCED"))
print(exists(board, "SEE"))
print(exists(board, "ABCB"))

