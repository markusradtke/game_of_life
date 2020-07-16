import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

iterations = 100
interval = 100
global_fig, ax1 = plt.subplots(figsize=(10, 10))

global board


def init_board(size):
    global board
    board = np.zeros((size, size))


def init_first():
    global first
    first = True


# initialize a board with a chosen distribution
def init_random_board(amt_living, size):
    global board
    minus_amt = 1.0 - amt_living
    board = np.random.choice(2, (size, size), p=[minus_amt, amt_living])
    return board


def create_frame_std(i: int):
    global board
    global first
    if i == iterations-1:
        how_many_live()
        last_frame = global_fig.savefig('last_frame.png')
        plt.close(global_fig)
    apply_standard_rules()
    ax1.set_title(f'Iteration: {i+1}')
    bla = ax1.imshow(board, cmap='gist_yarg')
    return [bla]


def create_frame_m_one(i: int):
    global board
    if i == iterations-1:
        plt.close(global_fig)
    apply_m_one_rules()
    bla = ax1.imshow(board, cmap='gist_yarg')
    return [bla]


def create_frame_p_one(i: int):
    global board
    apply_p_one_rules()
    if i == iterations-1:
        plt.close(global_fig)
    bla = ax1.imshow(board, cmap='gist_yarg')
    return [bla]


def apply_standard_rules():
    global board
    next_gen_board = np.zeros((board.shape[0], board.shape[1]), int)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
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
            tmp_sum = t + tr + r + br + b + bl + l + tl

            # rules and transfer to next generation
            # rule 1 survival
            if tmp_sum == 2 or tmp_sum == 3 and board[i][j] == 1:
                next_gen_board[i][j] = board[i][j]

            # rule 2 deaths
            elif (tmp_sum > 3 or tmp_sum < 2) and board[i][j] == 1:
                next_gen_board[i][j] = 0

            # rule 3 births
            elif tmp_sum == 3 and board[i][j] == 0:
                next_gen_board[i][j] = 1

            else:
                next_gen_board[i][j] = board[i][j]
    board = next_gen_board


def apply_m_one_rules():
    global board
    next_gen_board = np.zeros((board.shape[0], board.shape[1]), int)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
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
            tmp_sum = t + tr + r + br + b + bl + l + tl

            # rules and transfer to next generation
            # rule 1 survival
            if tmp_sum == 1 or tmp_sum == 2 and board[i][j] == 1:
                next_gen_board[i][j] = board[i][j]

            # rule 2 deaths
            elif (tmp_sum > 2 or tmp_sum < 1) and board[i][j] == 1:
                next_gen_board[i][j] = 0

            # rule 3 births
            elif tmp_sum == 2 and board[i][j] == 0:
                next_gen_board[i][j] = 1

            else:
                next_gen_board[i][j] = board[i][j]
    board = next_gen_board


def apply_p_one_rules():
    global board
    next_gen_board = np.zeros((board.shape[0], board.shape[1]), int)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
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
            tmp_sum = t + tr + r + br + b + bl + l + tl

            # rules and transfer to next generation
            # rule 1 survival
            if tmp_sum == 3 or tmp_sum == 4 and board[i][j] == 1:
                next_gen_board[i][j] = board[i][j]

            # rule 2 deaths
            elif (tmp_sum > 4 or tmp_sum < 3) and board[i][j] == 1:
                next_gen_board[i][j] = 0

            # rule 3 births
            elif tmp_sum == 4 and board[i][j] == 0:
                next_gen_board[i][j] = 1

            else:
                next_gen_board[i][j] = board[i][j]
    board = next_gen_board


def run_boy_run(rules):
    if rules == 'standard':
        for i in range(0, iterations):
            apply_standard_rules()
    elif rules == 'm_one':
        for i in range(0, iterations):
            apply_m_one_rules()
    elif rules == 'p_one':
        for i in range(0, iterations):
            apply_p_one_rules()


def how_many_live():
    global board
    wholesum = board.sum()
    print('all alive cells: ', wholesum)
    return wholesum


def user_input_configuration(size):
    dummy_grid = np.zeros((size, size))

    fig = plt.figure(figsize=(10, 10))

    ax = plt.axes()
    im = ax.imshow(dummy_grid, cmap='binary')
    for n in range(0, len(dummy_grid)):
        plt.axvline(.5 + n)
        plt.axhline(.5 + n)
    startup_points = []
    while True:
        pt = plt.ginput(1, timeout=-1)
        try:
            p_1 = int(round(pt[0][1], 0))
        except IndexError as e:
            break
        p_2 = int(round(pt[0][0], 0))
        coord = (p_1, p_2)
        print(coord)
        if coord in startup_points:
            dummy_grid[p_1][p_2] = 0
            startup_points.remove(coord)
        else:
            dummy_grid[p_1][p_2] = 1
            startup_points.append(coord)
        # update the displayed grid
        plt.imshow(dummy_grid, cmap='binary')
    plt.close()
    return dummy_grid


def txt_input(file):
    inp_array = np.loadtxt(file, dtype=int)
    return inp_array


def animate_std(frames, interval):
    global global_fig
    return FuncAnimation(global_fig, create_frame_std, frames=frames, interval=interval, blit=True, save_count=frames)


def animate_m_one(frames, interval):
    global global_fig
    return FuncAnimation(global_fig, create_frame_m_one, frames=frames, interval=interval, blit=True, save_count=frames)


def animate_p_one(frames, interval):
    global global_fig
    return FuncAnimation(global_fig, create_frame_p_one, frames=frames, interval=interval, blit=True, save_count=frames)


if __name__ == '__main__':
    rules = input('What ruleset do you want to use? (std/mone/pone)\n')
    mode = input('Do you want graphic, generated or text file input? (gra/gen/txt):\n')
    if mode == 'gen':
        percentage = input('The grid cells will be randomly chosen to be alive or dead.'
                           '\nHow many cells should be alive (in percent)?\n')
        percentage = int(percentage) / 100
        board_size = input('The grid will be quadratic, what should be the size of a side?\n')
        board_size = int(board_size)
        start_board = init_random_board(percentage, board_size)
        tmp_fig = plt.figure(figsize=(10, 10))
        plt.imshow(start_board, cmap='gist_yarg')
        plt.savefig('first_frame.png', cmap='gist_yarg')
        plt.close(tmp_fig)
        how_many_live()
    elif mode == 'gra':
        board_size = input('The grid will be quadratic, what should be the size of a side?\n')
        board_size = int(board_size)
        print('End input with the enter key.')
        grid = user_input_configuration(board_size)
        board = grid
        tmp_fig = plt.figure(figsize=(10, 10))
        plt.imshow(grid, cmap='gist_yarg')
        plt.savefig('first_frame.png', cmap='gist_yarg')
        plt.close(tmp_fig)
    elif mode == 'txt':
        filename = input('Name of your txt file: ')
        board = txt_input(filename)
        tmp_fig = plt.figure(figsize=(10, 10))
        plt.imshow(board, cmap='gist_yarg')
        plt.savefig('first_frame.png', cmap='gist_yarg')
        plt.close(tmp_fig)
    if rules == 'std':
        animate_std(iterations, interval)
    elif rules == 'mone':
        animate_m_one(iterations, interval)
    elif rules == 'pone':
        animate_p_one(iterations, interval)
    plt.show()
