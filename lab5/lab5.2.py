import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Функція для апроксимації
def f(x):
    return np.log(4 + 5 * np.exp(x))

# Параметри задачі
alpha, beta = 6, 8
N = 45
m_values = [1, 3, 5]

# Точки на інтервалі
x_values = np.linspace(alpha, beta, N + 1)
y_values = f(x_values)

# Обчислення поліноміальної апроксимації та похибки
errors = {}
approximations = {}

for m in m_values:
    # Поліноміальна апроксимація степеня m
    coeffs = np.polynomial.polynomial.polyfit(x_values, y_values, m)
    P_m = Polynomial(coeffs)
    
    # Зберігаємо апроксимацію для графіку
    approximations[m] = P_m
    
    # Обчислення похибки за заданою формулою
    error = np.sqrt(np.sum((y_values - P_m(x_values))**2) / (N + 1))
    errors[m] = error

# Виведення похибок
for m, error in errors.items():
    print(f"Похибка для полінома степеня {m}: {error:.4f}")

# Побудова графіків
x_plot = np.linspace(alpha, beta, 500)
plt.figure(figsize=(10, 6))
plt.plot(x_plot, f(x_plot), label="f(x) = ln(4 + 5e^x)", color='black')

for m, P_m in approximations.items():
    plt.plot(x_plot, P_m(x_plot), label=f"P_{m}(x), степінь {m}")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Апроксимація функції f(x) поліномами")
plt.legend()
plt.grid(True)
plt.show()
