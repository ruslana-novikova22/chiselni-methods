# Функція для методу Якобі
def jacobi_method(A, B, epsilon, max_iterations=100):
    n = len(A)
    x_old = [0.0] * n
    x_new = [0.0] * n
    for iteration in range(max_iterations):
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += A[i][j] * x_old[j]
            x_new[i] = (B[i] - sum) / A[i][i]

        # Перевірка умови зупинки
        if max([abs(x_new[i] - x_old[i]) for i in range(n)]) < epsilon:
            print(f"Метод Якобі збігся на {iteration + 1}-й ітерації")
            return x_new

        x_old = x_new.copy()

    print("Метод Якобі не збігся за максимальну кількість ітерацій")
    return x_new

A = [
    [17, -1, 1, -1],
    [-1, 19, -3, 2],
    [1, -3, 21, -3],
    [-1, 2, -3, 10]
]

B = [16, 17, 16, 8]

# Задана точність (epsilon)
epsilon = 1e-6

# Викликаємо метод Якобі
print("Розв'язок методом Якобі:")
x_jacobi = jacobi_method(A, B, epsilon)
print(x_jacobi)