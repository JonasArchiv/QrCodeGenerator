import numpy as np


def encode_data(data):
    return ''.join([format(ord(char), '08b') for char in data])


def create_qr_matrix(data, size=21):
    qr_matrix = np.zeros((size, size), dtype=int)

    # Adding finder patterns
    def add_finder_pattern(x, y):
        pattern = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        for dx in range(7):
            for dy in range(7):
                qr_matrix[x + dx, y + dy] = pattern[dx][dy]

    add_finder_pattern(0, 0)
    add_finder_pattern(0, size - 7)
    add_finder_pattern(size - 7, 0)

    binary_data = encode_data(data)
    index = 0
    for i in range(8, size - 8):
        for j in range(8, size - 8):
            if index < len(binary_data):
                qr_matrix[i, j] = int(binary_data[index])
                index += 1

    return qr_matrix


def print_qr_code(qr_matrix):
    for row in qr_matrix:
        print(''.join(['██' if col else '  ' for col in row]))


data = "HELLO"
qr_matrix = create_qr_matrix(data)
print_qr_code(qr_matrix)
