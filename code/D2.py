def run(part=0):
    with open('../input/D2') as file:
        contents = file.readlines()

    directions = []
    for line in contents:
        values = line.strip().split(' ')
        directions.append([values[0], int(values[1])])

    if part == 1 or part == 0:
        horizontal_position = 0
        depth = 0
        for pos, entry in enumerate(directions):
            if entry[0] == 'forward':
                horizontal_position += entry[1]

            if entry[0] == 'down':
                depth += entry[1]
            elif entry[0] == 'up':
                depth -= entry[1]

        print('Part 1:', horizontal_position * depth)

    if part == 2 or part == 0:
        horizontal_position = 0
        depth = 0
        aim = 0
        for pos, entry in enumerate(directions):
            if entry[0] == 'forward':
                horizontal_position += entry[1]
                depth += aim * entry[1]

            if entry[0] == 'down':
                aim += entry[1]
            elif entry[0] == 'up':
                aim -= entry[1]

        print('Part 2:', horizontal_position * depth)


if __name__ == '__main__':
    run()



