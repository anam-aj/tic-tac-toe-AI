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
    # Variable to count player moves
    X_moves = 0
    O_moves = 0

    # Count the player moves for current state of board
    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                X_moves += 1
            elif board[row][col] == O:
                O_moves += 1

    # Return whose turn it is
    if X_moves <= O_moves:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Set of actions
    action_set = set()

    # Find the available position on board and add them to action_set
    for row in range(3):
        for col in range(3):
            if board[row][col] is EMPTY:
                cell = (row, col)
                action_set.add(cell)

    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Create a deep copy of the current board
    cpy_board = copy.deepcopy(board)

    # Check validity of move
    if action not in actions(cpy_board):
        raise InvalidMoveError('Invalid Move')

    # Get whose turn it is
    mark = player(cpy_board)

    # Update the board
    row, col = action
    cpy_board[row][col] = mark

    return cpy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check for winner by row or column
    for i in range(3):
        if board[i][i] is not EMPTY:
            mark = board[i][i]

            # By row
            winner_found = True
            for j in range(3):
                if board[i][j] != mark:
                    winner_found = False
                    break
            if winner_found:
                return mark

            # By column
            winner_found = True
            for j in range(3):
                if board[j][i] != mark:
                    winner_found = False
                    break
            if winner_found:
                return mark

    # Check for winner by left diagonal
    if board[0][0] is not EMPTY:
        winner_found = True
        mark = board[0][0]
        for i in range(3):
            if board[i][i] != mark:
                winner_found = False
                break
        if winner_found:
            return mark

    # Check for winner by right diagonal
    if board[0][2] is not EMPTY:
        winner_found = True
        mark = board[0][2]
        for i in range(3):
            if board[i][2 - i] != mark:
                winner_found = False
                break
        if winner_found:
            return mark

    # No winner found(tie or incomplete game)
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is None:
        # Unfinished game with no winner
        for i in range(3):
            for j in range(3):
                if board[i][j] is EMPTY:
                    return False
        # Finished game with a Tie
        return True
    else:
        # Finshed game with a Winner
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winning_player = winner(board)

    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    else:
        if player(board) == X:
            return (max_value(board)[1])
        elif player(board) == O:
            return (min_value(board)[1])


def max_value(board):
    """
    Returns the maximum value for the current state.
    """

    if terminal(board):
        return (utility(board), None)
    else:
        # Initialize variale for maximum value and optimal choice
        v = float('-inf')
        best_action = None

        # Recursivly check all valid actions for optimal value
        for action in actions(board):
            v1 = max(v, ((min_value(result(board, action)))[0]))
            if v1 > v:
                best_action = action
                v = v1

        return (v, best_action)


def min_value(board):
    """
    Returns the minimum value for the current state.
    """

    if terminal(board):
        return (utility(board), None)
    else:
        # Initialize variale for maximum value and optimal choice
        v = float('inf')
        best_action = None

        # Recursivly check all valid actions for optimal value
        for action in actions(board):
            v1 = min(v, ((max_value(result(board, action)))[0]))
            if v1 < v:
                best_action = action
                v = v1

        return (v, best_action)
