def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1, result2, result3, sep="\n")

n = int(input('Строки :'))
m = int(input('Столбцы :'))
value = int(input('значение матрицы :'))
matrix = get_matrix(n, m, value)
if n <= 0:
    print(n)
elif m <= 0:
    print(m)
else:
    print()
    for i in matrix:
        print(*i)
