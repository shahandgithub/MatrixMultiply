import random
import time
import numpy as np

MAT_SIZE = 800


def multiply_matrices(mat_one, mat_two):
    if len(mat_one) == len(mat_two) and len(mat_one[0]) == len(mat_two[0]):
        new_mat = np.zeros((len(mat_one), len(mat_one[0])), dtype=float)
        new_mat = np.dot(mat_one, mat_two)
        return new_mat
    else:
        return None


def show_sub_square(matrix, start, size):
    for row in range(start, start + size):
        print('  '.join(['%.2f' % float(matrix[row, col])
                         for col in range(start, start + size)]))


def main():
    matrix = np.zeros((MAT_SIZE, MAT_SIZE), dtype=float)
    # generate small fraction of non-default values between 0 and 1
    small_fraction = round(MAT_SIZE * MAT_SIZE * .01)
    # small_fraction = 7 # This value is editable to remove more Zero values

    for i in range(small_fraction):
        row = random.randint(0, (MAT_SIZE - 1))
        col = random.randint(0, (MAT_SIZE - 1))
        value = random.uniform(0, 1)
        matrix[row, col] = value

    print("Matrix to Square: ")
    show_sub_square(matrix, 0, MAT_SIZE)

    start_time = time.perf_counter()
    new_mat = multiply_matrices(matrix, matrix)

    stop_time = time.perf_counter()
    elapsed = stop_time - start_time
    print("Product:")
    show_sub_square(new_mat, 0, MAT_SIZE)
    print("Calculation time:", elapsed, "seconds")


if __name__ == "__main__":
    main()

# MAT_SIZE | TIME
#    5     | 6.279999999997399e-05 seconds
#   10     | 5.070000000001462e-05 seconds
#   20     | 5.1499999999982116e-05 seconds
#   40     | 7.719999999999949e-05 seconds
#   80     | 0.0003721999999999892 seconds
#   100    | 0.0004270000000000107 seconds
#   140    | 0.000695100000000004 seconds
#   200    | 0.0013534000000000046 seconds
#   400    | 0.0044208000000000025 seconds
#   800    | 0.036617200000000016 seconds
