def run(part=0):
    with open('../input/D1') as file:
        contents = file.readlines()

    depth_values = []
    for line in contents:
        depth_values.append(int(line.strip()))

    if part == 1 or part == 0:
        count = 0
        for pos, entry in enumerate(depth_values):
            if pos < len(depth_values) - 1 and entry < depth_values[pos+1]:
                count += 1
        print('Part 1: ', count)

    if part == 2 or part == 0:
        count = 0
        for pos, entry in enumerate(depth_values):
            if pos < len(depth_values) - 3 and sum(depth_values[pos:pos+3]) < sum(depth_values[pos+1:pos+4]):
                count += 1
        print('Part 2: ', count)


if __name__ == '__main__':
    run()



