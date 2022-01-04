import numpy as np


def run(part=0):
    with open('../input/D4') as file:
        contents = file.readlines()

    boards = []
    board = []
    markers = []
    marker = []
    numbers = None
    for line in contents:
        if numbers is None:
            numbers = [int(i) for i in line.strip().split(',')]
        else:
            if line != '\n':
                board.append([int(i) for i in line.strip().split()])
                marker.append([0] * len(board[0]))
            else:
                if board:
                    boards.append(board)
                    markers.append(marker)
                board = []
                marker = []

    if board:
        boards.append(board)
        markers.append(marker)

    boards = np.array(boards)
    markers = np.array(markers)

    if part == 1 or part == 0:
        winning_number = 0
        winning_board = []
        for number in numbers:
            for pos, board in enumerate(boards):
                if number in board:
                    index = np.where(board == number)
                    index = (index[0], index[1])
                    markers[pos][index] = 1

                    for row in range(len(markers[pos])):
                        if sum(markers[pos][row, :]) == len(markers[pos]):
                            winning_number = number
                            winning_board = board
                            marker = markers[pos]
                            break

                    for col in range(len(markers[pos][0])):
                        if sum(markers[pos][:, col]) == len(markers[pos]):
                            winning_number = number
                            winning_board = board
                            marker = markers[pos]
                            break

            if len(winning_board) > 0:
                break

        indices = np.where(marker == 0)
        sum_unmarked_numbers = 0
        for p in range(len(indices[0])):
            index = (indices[0][p], indices[1][p])
            sum_unmarked_numbers += winning_board[index]

        print('Part 1:', sum_unmarked_numbers*winning_number)

    if part == 2 or part == 0:
        winning_number = 0
        winning_board = []
        completed_boards = []
        for number in numbers:
            for pos, board in enumerate(boards):
                if number in board and pos not in completed_boards:
                    index = np.where(board == number)
                    index = (index[0], index[1])
                    markers[pos][index] = 1

                    for row in range(len(markers[pos])):
                        if sum(markers[pos][row, :]) == len(markers[pos]) and pos not in completed_boards:
                            if len(completed_boards) == len(boards) - 1:
                                winning_number = number
                                winning_board = board
                                marker = markers[pos]
                            completed_boards.append(pos)
                            break

                    for col in range(len(markers[pos][0])):
                        if sum(markers[pos][:, col]) == len(markers[pos]) and pos not in completed_boards:
                            if len(completed_boards) == len(boards) - 1:
                                winning_number = number
                                winning_board = board
                                marker = markers[pos]
                            completed_boards.append(pos)
                            break

            if len(winning_board) > 0:
                break

        indices = np.where(marker == 0)
        sum_unmarked_numbers = 0
        for p in range(len(indices[0])):
            index = (indices[0][p], indices[1][p])
            sum_unmarked_numbers += winning_board[index]

        print('Part 2:', sum_unmarked_numbers * winning_number)


if __name__ == '__main__':
    run()



