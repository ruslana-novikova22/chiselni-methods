def sor_method(A, B, omega, epsilon, max_iterations=1000):
    n = len(A)
    x = [0.0] * n  # початкове наближення (всі нулі)

    for iteration in range(max_iterations):
        x_old = x.copy()

        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i)) #обчислює суму всіх елементів у рядку A[i], помножених на відповідні значення з x
            sum2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n)) #обчислює суму для елементів з індексами від i + 1 до n, використовуючи значення з попередньої ітерації
            x[i] = (1 - omega) * x_old[i] + omega * (B[i] - sum1 - sum2) / A[i][i]

        # Перевірка умови зупинки
        if max([abs(x[i] - x_old[i]) for i in range(n)]) < epsilon:
            print(f"Метод верхньої релаксації збігся на {iteration + 1}-й ітерації")
            return x

    print("Метод верхньої релаксації не збігся за максимальну кількість ітерацій")
    return x

# Задана система рівнянь: A * x = B
A = [
    [17, -1, 1, -1],
    [-1, 19, -3, 2],
    [1, -3, 21, -3],
    [-1, 2, -3, 10]
]

B = [16, 17, 16, 8]

# Параметр релаксації (omega)
omega = 1.25  # вибираємо експериментально

# Точність (epsilon)
epsilon = 1e-6

# Викликаємо метод верхньої релаксації
print("\nРозв'язок методом верхньої релаксації:")
x_sor = sor_method(A, B, omega, epsilon)
print(x_sor)
