def calculate_fishes(day):
    with open('../input/D6') as file:
        contents = file.readlines()

    timer = []
    for line in contents:
        timer = [int(i) for i in line.strip().split(',')]

    fishes = {}
    for d in range(0, 9):
        fishes[d] = 0

    for time in timer:
        fishes[time] += 1

    for day in range(1, day+1):
        old_6 = 0
        new_8 = 0
        for d in range(0, 9):
            if d == 0:
                old_6 = fishes[d]
                new_8 = fishes[d]
                fishes[d] = 0
            else:
                fishes[d - 1] += fishes[d]
                fishes[d] = 0
        fishes[6] += old_6
        fishes[8] += new_8

    total_fishes = 0
    for key in fishes.keys():
        total_fishes += fishes[key]

    return total_fishes


def run(part=0):
    if part == 1 or part == 0:
        day_nr = 80
        print('Part 1:', calculate_fishes(day_nr))

    if part == 2 or part == 0:
        day_nr = 256
        print('Part 2:', calculate_fishes(day_nr))


if __name__ == '__main__':
    run()



