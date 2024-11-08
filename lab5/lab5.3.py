import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite  # Для поліномів Ерміта

# Параметри
a, b = 3, 4
M = 30
n_points = 100  # Кількість точок для графіку
k_values = [1, 3, 5]  # Ступені апроксимації

# Визначення функції f(x)
def f(x):
    return np.log(4 + 5 * np.exp(x))

# Обчислення точок x_j на відрізку [a, b]
x = np.linspace(a, b, M+1)
y = f(x)

# Вага для ортогональних поліномів Ерміта
def weight(x):
    return np.exp(-x**2)

# Функція для обчислення поліномів Ерміта
def hermite_poly(i, x):
    H_i = hermite(i)
    return H_i(x)

# Апроксимація поліномом Q_k(x) з ортогональними поліномами Ерміта
def Q_k(x, k, coeffs):
    approx = np.zeros_like(x)
    for i in range(k+1):
        approx += coeffs[i] * hermite_poly(i, x)
    return approx

# Функція для обчислення коефіцієнтів a_i
def compute_coeffs(x, y, k):
    A = np.zeros((k+1, k+1))
    b = np.zeros(k+1)
    w = weight(x)
    for i in range(k+1):
        for j in range(k+1):
            A[i, j] = np.sum(w * hermite_poly(i, x) * hermite_poly(j, x))
        b[i] = np.sum(w * y * hermite_poly(i, x))
    return np.linalg.solve(A, b)

# Обчислення та побудова графіків апроксимацій для кожного k
x_plot = np.linspace(a, b, n_points)
y_plot = f(x_plot)

plt.plot(x_plot, y_plot, 'k-', linewidth=2, label="f(x) = ln(4 + 5e^x)")

for k in k_values:
    coeffs = compute_coeffs(x, y, k)
    y_approx = Q_k(x_plot, k, coeffs)
    plt.plot(x_plot, y_approx, '--', label=f'Q_{k}(x), k={k}')

# Додаємо легенду та налаштовуємо графік
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Апроксимація функції f(x) узагальненими поліномами Ерміта")
plt.grid(True)
plt.show()

# Обчислення похибки для кожного k
for k in k_values:
    coeffs = compute_coeffs(x, y, k)
    y_approx = Q_k(x, k, coeffs)
    error = np.sqrt(np.sum((y - y_approx)**2) / (M + 1))
    print(f'Похибка e^{{op}}_M для k={k}: {error}')
