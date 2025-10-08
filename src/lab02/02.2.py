def transpose(mat):
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Строки разной длины, матрица рваная")
    result = []
    for i in range(row_length):
        new_row = []
        for j in range(len(mat)):
            new_row.append(mat[j][i])
        result.append(new_row)
    return result


def row_sums(mat):
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Строки разной длины, матрица рваная")
    result = []
    for row in mat:
        total = 0
        for num in row:
            total += num
        result.append(total)
    return result


def col_sums(mat):
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Строки разной длины, матрица рваная")
    result = []
    for i in range(row_length):
        total = 0
        for j in range(len(mat)):
            total += mat[j][i]
        result.append(total)
    return result

print("transpose: ")
matrix1 = [[1, 2, 3]]
matrix2 = [[1], [2], [3]]
matrix3 = [[1, 2], [3, 4]]
matrix4 = []
matrix5 = [[1, 2], [3]]
print(transpose(matrix1))
print(transpose(matrix2))
print(transpose(matrix3))
print(transpose(matrix4))
# print(transpose(matrix5))

print("row sums: ")
matrix6 = [[1, 2, 3], [4, 5, 6]]
matrix7 = [[-1, 1], [10, -10]]
matrix8 = [[0, 0], [0, 0]]
matrix9 = [[1, 2], [3]]
print(row_sums(matrix6))
print(row_sums(matrix7))
print(row_sums(matrix8))
# print(row_sums(matrix9))

print("col sums: ")
print(col_sums(matrix6))
print(col_sums(matrix7))
print(col_sums(matrix8))
# print(col_sums(matrix9))