import numpy as np

def run(part=0):
    with open('../input/D3') as file:
        contents = file.readlines()

    values = []
    for line in contents:
        values.append([int(i) for i in line.strip()])

    values = np.array(values)
    if part == 1 or part == 0:
        gamma_rate = ''
        epsilon_rate = ''
        for c in range(len(values[0])):
            zero_count = np.count_nonzero(values[:, c] == 0)
            one_count = np.count_nonzero(values[:, c] == 1)
            if zero_count < one_count:
                gamma_rate += '1'
                epsilon_rate += '0'
            else:
                gamma_rate += '0'
                epsilon_rate += '1'

        print('Part 1:', int(gamma_rate, 2) * int(epsilon_rate, 2))

    if part == 2 or part == 0:
        value_matrix = values.copy()
        for c in range(len(value_matrix[0])):
            zero_count = np.count_nonzero(value_matrix[:, c] == 0)
            one_count = np.count_nonzero(value_matrix[:, c] == 1)
            if zero_count <= one_count:
                indices = np.where(value_matrix[:, c] == 0)
                value_matrix = np.delete(value_matrix, indices[0], axis=0)
            else:
                indices = np.where(value_matrix[:, c] == 1)
                value_matrix = np.delete(value_matrix, indices[0], axis=0)
            if len(value_matrix) == 1: break
        oxygen_generator_rating = value_matrix.copy()

        value_matrix = values.copy()
        for c in range(len(value_matrix[0])):
            zero_count = np.count_nonzero(value_matrix[:, c] == 0)
            one_count = np.count_nonzero(value_matrix[:, c] == 1)
            if zero_count <= one_count:
                indices = np.where(value_matrix[:, c] == 1)
                value_matrix = np.delete(value_matrix, indices[0], axis=0)
            else:
                indices = np.where(value_matrix[:, c] == 0)
                value_matrix = np.delete(value_matrix, indices[0], axis=0)
            if len(value_matrix) == 1: break
        co2_scrubber_rating = value_matrix

        o2_rating = ''.join(list([str(i) for i in oxygen_generator_rating[0]]))
        co2_rating = ''.join(list([str(i) for i in co2_scrubber_rating[0]]))

        print('Part 2:', int(o2_rating, 2)*int(co2_rating, 2))

if __name__ == '__main__':
    run()



