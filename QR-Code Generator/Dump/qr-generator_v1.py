import os
from PIL import Image


SIZE = 21


def initialize_qr_matrix():
    return [[0] * SIZE for _ in range(SIZE)]


def add_finder_patterns(matrix):
    def add_finder(x, y):
        for i in range(-1, 8):
            for j in range(-1, 8):
                if 0 <= x + i < SIZE and 0 <= y + j < SIZE:
                    if (0 <= i <= 6 and (j == 0 or j == 6)) or (0 <= j <= 6 and (i == 0 or i == 6)) or (
                            2 <= i <= 4 and 2 <= j <= 4):
                        matrix[x + i][y + j] = 1
                    else:
                        matrix[x + i][y + j] = 0

    add_finder(0, 0)
    add_finder(0, SIZE - 7)
    add_finder(SIZE - 7, 0)


def add_timing_patterns(matrix):
    for i in range(8, SIZE - 8):
        if i % 2 == 0:
            matrix[i][6] = matrix[6][i] = 1


def add_data(matrix, data):
    binary_data = ''.join([format(ord(char), '08b') for char in data])
    index = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if index < len(binary_data):
                if matrix[i][j] == 0:
                    matrix[i][j] = int(binary_data[index])
                    index += 1


def save_qr_to_image(matrix, file_path, scale=10):
    img_size = SIZE * scale
    image = Image.new('1', (img_size, img_size), 'white')
    pixels = image.load()

    for i in range(SIZE):
        for j in range(SIZE):
            color = 0 if matrix[i][j] == 1 else 1
            for x in range(scale):
                for y in range(scale):
                    pixels[i * scale + x, j * scale + y] = color

    image.save(file_path)


data = "Hello"
qr_matrix = initialize_qr_matrix()
add_finder_patterns(qr_matrix)
add_timing_patterns(qr_matrix)
add_data(qr_matrix, data)

output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file_path = os.path.join(output_dir, "qr_code.png")
save_qr_to_image(qr_matrix, output_file_path)

print(f"QR-Code wurde in {output_file_path} gespeichert.")
