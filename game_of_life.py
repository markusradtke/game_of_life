import numpy as np
import matplotlib.pyplot as plt


# initialize a board with 50/50 distribution
def init_random_board():
    # board = np.random.randint(0, 2, (100, 100), int)
    board = np.random.choice(2, (5, 5), p=[0.5, 0.5])
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
    # p_board = np.copy(board)
    # for i in range(p_board.shape[0]):
    #     for j in range(p_board.shape[1]):
    #         p_board[i][j] = (p_board[i][j] + 1) % 2
    plt.imshow(board, cmap='binary')
    plt.show()


def run_boy_run(board):
    for i in range(0, 1000):
        gen100 = apply_rules(board)
    return gen100


def how_many_live(board):
    wholesum = board.sum()
    print("all alive cells: ", wholesum)
    return wholesum


def user_input_configuration():
    dummy_grid = np.zeros((10, 10))

    fig = plt.figure(figsize=(5, 5))

    ax = plt.axes()
    # plotting this grid, it's boring for now, all white, since the grid is nothing but zeros
    im = ax.imshow(dummy_grid, cmap='binary')
    # Plotting lines to demarcate the cells in the grid
    for n in range(0, len(dummy_grid)):
        plt.axvline(.5 + n)
        plt.axhline(.5 + n)
    # to track selected/deselected points
    startup_points = []
    # keeping input live indefinitely
    while True:
        # ginput, looking for 1 value at a time, setting timeout to -1 means it will wait indefinetely
        pt = plt.ginput(1, timeout=-1)
        # getting coordinates, rounded to whole numbers
        p_1 = int(round(pt[0][1], 0))
        p_2 = int(round(pt[0][0], 0))
        coord = (p_2, len(dummy_grid) - p_1 - 1)
        # updating the tracking of which points have been selected, and changing the display grid
        if coord in startup_points:
            dummy_grid[p_1][p_2] = 0
            startup_points.remove(coord)
        else:
            dummy_grid[p_1][p_2] = 1
            startup_points.append(coord)
        # update the displayed grid
        plt.imshow(dummy_grid, cmap='binary')
        try:
            x = 0
        except KeyboardInterrupt:
            break
    return startup_points


if __name__ == '__main__':
    user_input_configuration()

    # start_board = init_random_board()
    # how_many_live(start_board)
    # plot_board(start_board)
    # gen100 = run_boy_run(start_board)
    # plot_board(gen100)
    # how_many_live(gen100)