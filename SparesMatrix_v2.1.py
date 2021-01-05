import time
import random


class MatrixEntry:
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.nextNode = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __eq__(self, other):
        if isinstance(other, MatrixEntry):
            return self.col == other.col
        else:
            return self.col == other

    def __lt__(self, other):
        if isinstance(other, MatrixEntry):
            return self.col < other.col
        else:
            return self.col < other

    def __gt__(self, other):
        return not self.__lt__(other) and not self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return not self.__gt__(other)


class LinkedList:
    def __init__(self, defaultValue):
        self.head = None
        self.defaultValue = defaultValue

    def addNode(self, col, value):
        if value is None:
            value = self.defaultValue
        node = MatrixEntry(col, value)
        if self.head is None:
            self.head = node
        else:
            if self.contain(node):
                if not node.value == self.defaultValue:
                    next_node = self.head
                    while next_node:
                        if next_node.col == node.col:
                            next_node.value = node.value
                        next_node = next_node.nextNode
                elif node.value == self.defaultValue:
                    next_node = self.head
                    if next_node == self.head:
                        self.head = next_node.nextNode
                    else:
                        previous_node = next_node
                        while next_node:
                            if next_node.col == node.col:
                                previous_node.nextNode = next_node.nextNode
                            previous_node = next_node
                            next_node = next_node.nextNode

            else:
                ptr = self.head
                self.head = node
                self.head.nextNode = ptr

    def contain(self, node):
        if self.head is None:
            return False
        else:
            p = self.head
            while p is not None:
                if p.col == node.col:
                    return True
                p = p.nextNode
            return False

    def getElement(self, row, col):
        next_node = self.head
        while next_node:
            if next_node.col == col:
                return next_node.value
            next_node = next_node.nextNode
        return self.defaultValue

    def __str__(self):
        res = ""
        ptr = self.head
        while ptr:
            res += str(ptr.value) + ", "
            ptr = ptr.nextNode
        res = res.strip(", ")
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"


class SparseMatrix:
    def __init__(self, r, c, default_value):
        self.row = r
        self.col = c
        self.default_value = default_value
        self.matrix = []
        for row in range(self.row):
            self.matrix.append(LinkedList(self.default_value))

    def set(self, r, c, value):
        if r < 0 or r >= self.row or c < 0 or c >= self.col:
            raise IndexError("Ooops!")
        else:
            if self.matrix[r] is None:
                self.matrix[r] = LinkedList(self.default_value)
            self.matrix[r].addNode(c, value)

    def get(self, r, c):
        if r < 0 or r >= self.row or c < 0 or c >= self.col:
            raise IndexError("Ooops!")
        else:
            return self.matrix[r].getElement(r, c)

    def clear(self):
        self.matrix = []
        for row in range(self.row):
            self.matrix.append(LinkedList(self.default_value))

    def show_sub_square(self, start, size):
        for row in range(start, start + size):
            print('  '.join(['%.2f' % float(self.matrix[row].getElement(row, col))
                             for col in range(start, start + size)]))


class SparseMatrixMult(SparseMatrix):

    def __init__(self, r, c, default_value):
        super().__init__(r, c, default_value)

    @staticmethod
    def multiply_matrices(mat_one, mat_two):
        new_mat = SparseMatrixMult(MAT_SIZE, MAT_SIZE, 0)

        # generate small fraction of non-default values between 0 and 1
        small_fraction = round(MAT_SIZE * MAT_SIZE * .01)
        # small_fraction = 7 # This value is editable to remove more Zero values

        for i in range(small_fraction):
            row = random.randint(0, (MAT_SIZE - 1))
            col = random.randint(0, (MAT_SIZE - 1))
            value = random.uniform(0, 1)
            new_mat.set(row, col, value)

        for i in range(MAT_SIZE):
            for j in range(MAT_SIZE):
                for k in range(MAT_SIZE):
                    value = new_mat.get(i, j) + (mat_one.get(i, k) * mat_two.get(k, j))
                    new_mat.set(i, j, value)
        return new_mat


MAT_SIZE = 10


def main():
    mat = SparseMatrix(MAT_SIZE, MAT_SIZE, 0)
    mat2 = SparseMatrix(MAT_SIZE, MAT_SIZE, 0)

    mat.set(0, 0, 1.00)
    mat.set(0, 1, 2.00)
    mat.set(0, 2, 3.00)
    mat.set(0, 3, 4.00)
    mat.set(0, 4, 5.00)

    mat.set(1, 0, -1.00)
    mat.set(1, 1, -2.00)
    mat.set(1, 2, -3.00)
    mat.set(1, 3, -4.00)
    mat.set(1, 4, -5.00)

    mat.set(2, 0, 1.00)
    mat.set(2, 1, 3.00)
    mat.set(2, 2, 1.00)
    mat.set(2, 3, 3.00)
    mat.set(2, 4, 1.00)

    mat.set(3, 0, 0.00)
    mat.set(3, 1, 1.00)
    mat.set(3, 2, 0.00)
    mat.set(3, 3, 1.00)
    mat.set(3, 4, 0.00)

    mat.set(4, 0, -1.00)
    mat.set(4, 1, -1.00)
    mat.set(4, 2, -1.00)
    mat.set(4, 3, -1.00)
    mat.set(4, 4, -1.00)

    mat2.set(0, 0, 2.00)
    mat2.set(0, 1, 1.00)
    mat2.set(0, 2, 5.00)
    mat2.set(0, 3, 0.00)
    mat2.set(0, 4, 2.00)

    mat2.set(1, 0, 1.00)
    mat2.set(1, 1, 4.00)
    mat2.set(1, 2, 3.00)
    mat2.set(1, 3, 2.00)
    mat2.set(1, 4, 7.00)

    mat2.set(2, 0, 4.00)
    mat2.set(2, 1, 4.00)
    mat2.set(2, 2, 4.00)
    mat2.set(2, 3, 4.00)
    mat2.set(2, 4, 4.00)

    mat2.set(3, 0, 7.00)
    mat2.set(3, 1, 1.00)
    mat2.set(3, 2, -1.00)
    mat2.set(3, 3, -1.00)
    mat2.set(3, 4, -1.00)

    mat2.set(4, 0, 0.00)
    mat2.set(4, 1, 0.00)
    mat2.set(4, 2, 8.00)
    mat2.set(4, 3, -1.00)
    mat2.set(4, 4, -6.00)

    print()
    print("First Sparse Matrix: ")
    mat.show_sub_square(0, MAT_SIZE)
    print()

    print()
    print("Second Sparse Matrix: ")
    mat2.show_sub_square(0, MAT_SIZE)
    print()

    start_time = time.perf_counter()
    mat3 = SparseMatrixMult.multiply_matrices(mat, mat2)
    stop_time = time.perf_counter()
    elapsed = stop_time - start_time

    print()
    print("Sparse Product Matrix, m X n: ")
    mat3.show_sub_square(0, MAT_SIZE)
    print("Calculation time:", elapsed, "seconds")


if __name__ == "__main__":
    main()

# 1. Are the times longer or shorter than our list-of-list matrix times?
# The time of multiplication using classes was definitely longer than without classes
# Calculation time for MAT_SIZE = 5
# With Classes: 0.0008561999999999945 seconds
# Without Classes: 6.649999999999712e-05 seconds

# 2. Are the growth rates larger or smaller? By how much?
# Growth rates are longer by a factor of 15

# 3. Create a table and answer the same questions as before.
# MAT_SIZE | TIME
#    5     | 0.0008561999999999945 seconds
#   10     | 0.0078099999999999975 seconds
#   20     | 0.0473577 seconds
#   40     | 0.3405912 seconds
#   80     | 2.6555806 seconds
#   100    | 5.6744822 seconds
#   140    | 14.1135127 seconds
#   200    | 42.1313937 seconds

# 4. What was the largest MAT_SIZE you could use here, and was the reason the same or different than for dynamic arrays?
# 400. The reason was the same. It was because of the exponential increment in calculation time in co-relation to the MAT_SIZE

# 5. If you have time, modify 1% to be .5% or .1% or even less and see if the growth rates change.
# This made the calculation time a bit faster, but impact wasn't that much.
