import numpy as np
import matplotlib.pyplot as plt


# initialize
def init_random_board():
    board = np.random.randint(0, 2, (100, 100), int)
    print(board)
    return board


def apply_rules(board):
    next_gen_board = np.zeros((board.shape[0], board.shape[1]), int)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            # print(i, j, board[i][j])
            # rule 0 - survivals; two or three neighbouring counters survives
            tmp_sum = 0
            if i == 0:
                t = 0
            else:
                t = board[i - 1][j]
            if i == 0 or j == board.shape[1] - 1:
                tr = 0
            else:
                tr = board[i - 1][j + 1]
            if j == board.shape[1] - 1:
                r = 0
            else:
                r = board[i][j + 1]
            if i == board.shape[0] - 1 or j == board.shape[1] - 1:
                br = 0
            else:
                br = board[i + 1][j + 1]
            if i == board.shape[0] - 1:
                b = 0
            else:
                b = board[i + 1][j]
            if i == board.shape[0] - 1 or j == 0:
                bl = 0
            else:
                bl = board[i + 1][j - 1]
            if j == 0:
                l = 0
            else:
                l = board[i][j - 1]
            if i == 0 or j == 0:
                tl = 0
            else:
                tl = board[i - 1][j - 1]
            # print(t, tr, r, br, b, bl, l, tl)
            tmp_sum = t + tr + r + br + b + bl + l + tl

            # rules and transfer to next generation
            # rule 1 survival
            if tmp_sum == 2 or tmp_sum == 3 and board[i][j] == 1:
                next_gen_board[i][j] = board[i][j]

            # rule 2 deaths
            elif (tmp_sum > 4 or tmp_sum < 2) and board[i][j] == 1:
                next_gen_board[i][j] = 0

            # rule 3 births
            elif tmp_sum == 3 and board[i][j] == 0:
                next_gen_board[i][j] = 1

            else:
                next_gen_board[i][j] = board[i][j]
    return next_gen_board


def plot_board(board):
    p_board = np.copy(board)
    for i in range(p_board.shape[0]):
        for j in range(p_board.shape[1]):
            p_board[i][j] = (p_board[i][j] + 1) % 2
    plt.imshow(p_board, cmap='gray')
    plt.show()


if __name__ == '__main__':
    start_board = init_random_board()
    plot_board(start_board)
    ng_board = apply_rules(start_board)
    plot_board(ng_board)
    print(ng_board)