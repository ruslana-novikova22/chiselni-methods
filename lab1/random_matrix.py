import numpy as np
import matplotlib.pyplot as plt

# Генерація матриці A розміром m x m
def generate_matrix_A(m):
    return [[1 / (i + j - 1) for j in range(1, m + 1)] for i in range(1, m + 1)]

# Генерація вектора x за формулою i^2 для i = 1, ..., m
def generate_vector_x(m):
    return [i**2 for i in range(1, m + 1)]

# Обчислення добутку A * x = f
def matrix_multiply(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]

# Метод Гауса для вирішення системи рівнянь Ax = f
def gaussian_elimination(A, f):
    n = len(f)
    A = [row[:] for row in A]
    f = f[:]
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        if i != max_row:
            A[i], A[max_row] = A[max_row], A[i]
            f[i], f[max_row] = f[max_row], f[i]
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            f[k] -= factor * f[i]
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (f[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
    return x

# Обчислення інфінітної норми матриці
def matrix_norm_inf(A):
    return max(sum(abs(A[i][j]) for j in range(len(A[0]))) for i in range(len(A)))

# Обчислення оберненої матриці методом Гауса
def invert_matrix(A):
    n = len(A)
    A = [row[:] for row in A]
    inv_A = np.identity(n).tolist()
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        if i != max_row:
            A[i], A[max_row] = A[max_row], A[i]
            inv_A[i], inv_A[max_row] = inv_A[max_row], inv_A[i]
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(n):
                A[k][j] -= factor * A[i][j]
                inv_A[k][j] -= factor * inv_A[i][j]
    for i in range(n - 1, -1, -1):
        factor = A[i][i]
        for j in range(n):
            inv_A[i][j] /= factor
            A[i][j] /= factor
        for k in range(i):
            factor = A[k][i]
            for j in range(n):
                A[k][j] -= factor * A[i][j]
                inv_A[k][j] -= factor * inv_A[i][j]
    return inv_A

# Обчислення числа обумовленості матриці
def condition_number(A):
    inv_A = invert_matrix(A)
    norm_A = matrix_norm_inf(A)
    norm_inv_A = matrix_norm_inf(inv_A)
    return norm_A * norm_inv_A

# Розв'язок для різних значень m і виведення результатів
def solve_and_display():
    ms = [8, 10, 12, 14]
    for m in ms:
        print(f"\nСистема для m = {m}:")
        A = generate_matrix_A(m)
        x = generate_vector_x(m)
        f = matrix_multiply(A, x)
        x_approx = gaussian_elimination([row[:] for row in A], f[:])
        cond_num = condition_number(A)
        print("Матриця A:")
        for row in A:
            print(["{:.2f}".format(value) for value in row])
        #print("Вектор x:", x)
        #print("Вектор x':", [f"{xi:.2f}" for xi in x_approx])
        print()
        print(f"Число обумовленості: {cond_num:.2e}")

# Запуск функції для обчислень
solve_and_display()
