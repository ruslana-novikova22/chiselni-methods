import numpy as np
import matplotlib.pyplot as plt

# Параметри задачі
alpha = 3            # Початок проміжку
beta = 4             # Кінець проміжку
n = 10               # Кількість вузлів інтерполяції
m = 10000            # Кількість точок для оцінки похибки

# Функція, яку інтерполюємо
def f(x):
    return np.log(4 + 5 * x**2)

# Побудова рівномірної сітки для інтерполяції
x_nodes = np.linspace(alpha, beta, n + 1)
y_nodes = f(x_nodes)
h = (beta - alpha) / n

# Функція для обчислення таблиці кінцевих різниць
def finite_diffs(y):
    n = len(y)
    diffs = np.zeros((n, n))
    diffs[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            diffs[i, j] = diffs[i + 1, j - 1] - diffs[i, j - 1]
    return diffs

# Обчислення таблиці кінцевих різниць
diff_table = finite_diffs(y_nodes)

# Функція для інтерполяційного многочлена Н'ютона вперед
def newton_forward(x, x_nodes, diff_table):
    n = len(x_nodes) - 1
    result = diff_table[0, 0]
    term = 1
    for i in range(1, n + 1):
        term *= (x - x_nodes[i - 1]) / (i * h)
        result += term * diff_table[0, i]
    return result

# Функція для інтерполяційного многочлена Н'ютона назад
def newton_backward(x, x_nodes, diff_table):
    n = len(x_nodes) - 1
    result = diff_table[n, 0]
    term = 1
    for i in range(1, n + 1):
        term *= (x - x_nodes[n - i + 1]) / (i * h)
        result += term * diff_table[n - i, i]
    return result

# Підрахунок похибок
x_eval = np.linspace(alpha, beta, m + 1)
f_values = f(x_eval)
errors_forward = np.abs(f_values - [newton_forward(x, x_nodes, diff_table) for x in x_eval])
errors_backward = np.abs(f_values - [newton_backward(x, x_nodes, diff_table) for x in x_eval])

epsilon_B = np.max(errors_forward)
epsilon_H = np.max(errors_backward)

# Виведення результатів
print("Максимальна похибка для інтерполяції вперед ε_m^(B):", epsilon_B)
print("Максимальна похибка для інтерполяції назад ε_m^(H):", epsilon_H)

# Побудова графіків
plt.figure(figsize=(12, 6))
plt.plot(x_eval, f_values, label="f(x) = ln(4 + 5x^2)", color="black")
plt.plot(x_eval, [newton_forward(x, x_nodes, diff_table) for x in x_eval], label="Інтерполяція вперед", linestyle="--", color="blue")
plt.plot(x_eval, [newton_backward(x, x_nodes, diff_table) for x in x_eval], label="Інтерполяція назад", linestyle="--", color="red")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графіки функції та інтерполяційних многочленів")
plt.grid(True)
plt.show()
