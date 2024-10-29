# Функція для методу простої ітерації
def simple_iteration_method(A, B, epsilon, max_iterations=1000):
    # Ініціалізація
    n = len(A)
    x = [0.0] * n  # початкове наближення (всі нулі)
    
    # Перетворення системи до вигляду x = Cx + d
    C = [[0.0] * n for _ in range(n)]
    d = [0.0] * n

    for i in range(n):
        for j in range(n):
            if i != j:
                C[i][j] = -A[i][j] / A[i][i]
        d[i] = B[i] / A[i][i]

    # Ітераційний процес
    for iteration in range(max_iterations):
        x_new = [0.0] * n

        for i in range(n):
            sum_Cx = sum(C[i][j] * x[j] for j in range(n))
            x_new[i] = sum_Cx + d[i]

        # Перевірка умови зупинки
        if max([abs(x_new[i] - x[i]) for i in range(n)]) < epsilon:
            print(f"Метод простої ітерації збігся на {iteration + 1}-й ітерації")
            return x_new

        x = x_new.copy()  # Оновлюємо значення для наступної ітерації

    print("Метод простої ітерації не збігся за максимальну кількість ітерацій")
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

# Викликаємо метод простої ітерації
print("\nРозв'язок методом простої ітерації:")
x_simple_iteration = simple_iteration_method(A, B, epsilon)
print(x_simple_iteration)
