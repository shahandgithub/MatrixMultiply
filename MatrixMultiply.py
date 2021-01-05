import random
import time

MAT_SIZE = 10


def create_matrix(rows, cols):
    new_mat = [[0 for col in range(cols)] for row in range(rows)]
    return new_mat


def multiply_matrices(mat_one, mat_two):
    if len(mat_one) == len(mat_two) and len(mat_one[0]) == len(mat_two[0]):
        new_mat = create_matrix(len(mat_one), len(mat_one[0]))
        for i in range(len(mat_one)):
            for j in range(len(mat_two[0])):
                for k in range(len(mat_two)):
                    new_mat[i][j] += mat_one[i][k] * mat_two[k][j]
        return new_mat
    else:
        return None


def show_sub_square(matrix, start, size):
    for row in range(start, start + size):
        print('  '.join(['%.2f' % float(matrix[row][col])
                         for col in range(start, start + size)]))


def main():
    # proof of correctness
    mat_one = [[1, 2, 3, 4, 5], [-1, -2, -3, -4, -5], [1, 3, 1, 3, 5], [0, 1, 0, 1, 0], [-1, -1, -1, -1, -1]]
    mat_two = [[2, 1, 5, 0, 2], [1, 4, 3, 2, 7], [4, 4, 4, 4, 4], [7, 1, -1, -1, -1], [0, 0, 8, -1, -6]]

    print("Test Matrix One:")
    show_sub_square(mat_one, 0, 5)
    print()
    print("Test Matrix Two:")
    show_sub_square(mat_two, 0, 5)
    print()
    print("Test Product:")
    new_mat = multiply_matrices(mat_one, mat_two)
    if new_mat is not None:
        print()
        show_sub_square(new_mat, 0, 5)
        print()

        matrix = create_matrix(MAT_SIZE, MAT_SIZE)
        # generate small fraction of non-default values between 0 and 1
        small_fraction = round(MAT_SIZE * MAT_SIZE * 0.01)
        # small_fraction = 7 # This value is editable to remove more Zero values

        for i in range(small_fraction):
            row = random.randint(0, (MAT_SIZE - 1))
            col = random.randint(0, (MAT_SIZE - 1))
            value = random.uniform(0, 1)
            matrix[row][col] = value

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

# 1. Just looking at your code, what is your estimate for the time complexity of this algorithm?
# We'll call this the theoretical complexity.
# Theoretical Complexity of this Algorithm is O(n)3
# 2. What was the smallest MAT_SIZE that took more than a second to calculate?
# Smallest MAT_SIZE that took more than a second was 140
# 3. What happened when you doubled MAT_SIZE , doubled it again, doubled it again? Give several M values and their times in a table.
# MAT_SIZE | TIME
#    5     | 6.649999999999712e-05 seconds
#   10     | 0.00041280000000000483 seconds
#   20     | 0.0031371999999999928 seconds
#   40     | 0.026313100000000006 seconds
#   80     | 0.18374199999999996 seconds
#   100    | 0.47169679999999997 seconds
#   140    | 1.0989208 seconds
#   200    | 2.9862916 seconds
#   400    | 24.0924637 seconds
#   800    | 84.4655826 seconds

# 4. How large a MAT_SIZE can you use before the program refuses to run (exception or run-time error due to memory overload) or it takesso long you can't wait for the run?
# At round MAT_SIZE 1000, it started taking too long

# 5.How did the data agree or disagree with your original time complexity estimate? What are your thoughts about this?
# The resulting data definitely agreed with the original time complexity.
