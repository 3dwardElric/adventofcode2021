import numpy as np

def run(part=0):
    with open('../input/D5') as file:
        contents = file.readlines()

    coordinates = []
    for line in contents:
        start, end = line.strip().split(' -> ')
        x_1, y_1 = start.split(',')
        x_2, y_2 = end.split(',')
        coordinates.append([int(x_1), int(x_2), int(y_1), int(y_2)])
    coordinates = np.array(coordinates)
    x_max = max(max(coordinates[:, 0]), max(coordinates[:, 1]))
    y_max = max(max(coordinates[:, 2]), max(coordinates[:, 3]))
    zero_grid = []
    for i in range(x_max + 1):
        zero_grid.append([0] * (y_max + 1))


    if part == 1 or part == 0:
        grid = np.array(zero_grid)
        for entry in coordinates:
            if entry[0] == entry[1]:
                y_start = min(entry[2], entry[3])
                y_end = max(entry[2], entry[3])
                for r in range(y_start, y_end+1):
                    grid[r, entry[0]] += 1

            if entry[2] == entry[3]:
                x_start = min(entry[0], entry[1])
                x_end = max(entry[0], entry[1])
                for c in range(x_start, x_end + 1):
                    grid[entry[2], c] += 1

        print('Part 1:', np.count_nonzero(grid > 1))

    if part == 2 or part == 0:
        grid = np.array(zero_grid)
        for entry in coordinates:
            if entry[0] == entry[1]:
                y_start = min(entry[2], entry[3])
                y_end = max(entry[2], entry[3])
                for r in range(y_start, y_end+1):
                    grid[r, entry[0]] += 1

            if entry[2] == entry[3]:
                x_start = min(entry[0], entry[1])
                x_end = max(entry[0], entry[1])
                for c in range(x_start, x_end + 1):
                    grid[entry[2], c] += 1

            if abs(entry[0] - entry[1]) == abs(entry[2] - entry[3]):
                if entry[0] < entry[1]:
                    x_start = entry[0]
                    y_start = entry[2]
                    x_end = entry[1]
                    y_end = entry[3]
                else:
                    x_start = entry[1]
                    y_start = entry[3]
                    x_end = entry[0]
                    y_end = entry[2]

                while x_start <= x_end:
                    grid[y_start, x_start] += 1
                    x_start += 1
                    if y_start < y_end:
                        y_start += 1
                    else:
                        y_start -= 1

                    if x_start > x_end:
                        break
        print('Part 2:', np.count_nonzero(grid > 1))



if __name__ == '__main__':
    run()



