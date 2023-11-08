"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_dif = sum(sublist.count(X) for sublist in board) - sum(sublist.count(O) for sublist in board)
    
    if X_dif == 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    none_positions = {(i, j) for i, row in enumerate(board) for j, element in enumerate(row) if element is None}
    return none_positions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise NameError('Invalid action.')
    # make a deep copy of the board first before making any changes
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    values = [X, O]
    for value in values:
        # Check rows
        for row in board:
            if all(cell == value for cell in row):
                return value

        # Check columns
        for col in range(len(board[0])):
            if all(board[row][col] == value for row in range(len(board))):
                return value

        # Check diagonal top-left to bottom-right
        if all(board[i][i] == value for i in range(len(board))):
            return value

        # Check diagonal top-right to bottom-left
        if all(board[i][len(board)-1-i] == value for i in range(len(board))):
            return value

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    none_count = 0
    for sublist in board:
        none_count += sublist.count(None)

    # in which situations is game OVER...either a win, or no more moves
    if winner(board) is not None or none_count == 0:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    
