# Функція для методу Зейделя
def gauss_seidel_method(A, B, epsilon, max_iterations=1000):
    n = len(A)
    x = [0.0] * n
    for iteration in range(max_iterations):
        x_old = x.copy()
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += A[i][j] * x[j]
            x[i] = (B[i] - sum) / A[i][i]

        # Перевірка умови зупинки
        if max([abs(x[i] - x_old[i]) for i in range(n)]) < epsilon:
            print(f"Метод Зейделя збігся на {iteration + 1}-й ітерації")
            return x

    print("Метод Зейделя не збігся за максимальну кількість ітерацій")
    return x


# Задана система рівнянь: A * x = B
A = [
    [17, -1, 1, -1],
    [-1, 19, -3, 2],
    [1, -3, 21, -3],
    [-1, 2, -3, 10]
]

B = [16, 17, 16, 8]

# Задана точність (epsilon)
epsilon = 1e-6

# Викликаємо метод Зейделя
print("\nРозв'язок методом Зейделя:")
x_gauss_seidel = gauss_seidel_method(A, B, epsilon)
print(x_gauss_seidel)