def run(part=0):
    with open('../input/D7') as file:
        contents = file.readlines()

    horizontal_pos = []
    for line in contents:
        horizontal_pos = [int(i) for i in line.strip().split(',')]
    horizontal_pos.sort()

    if part == 1 or part == 0:
        min_cost = None
        for p in horizontal_pos:
            cost = 0
            for i in horizontal_pos:
                distance = abs(p - i)
                cost += distance

            if not min_cost:
                min_cost = cost
            elif cost < min_cost:
                min_cost = cost

        print('Part 1:', int(min_cost))

    if part == 2 or part == 0:
        max_value = max(horizontal_pos)
        min_cost = None
        for p in range(max_value):
            cost = 0
            for i in horizontal_pos:
                distance = abs(p - i)
                step_cost = distance * (distance + 1) / 2
                cost += step_cost

            if not min_cost:
                min_cost = cost
            elif cost < min_cost:
                min_cost = cost

        print('Part 2:', int(min_cost))


if __name__ == '__main__':
    run()



