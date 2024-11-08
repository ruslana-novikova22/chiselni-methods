import numpy as np
import matplotlib.pyplot as plt

# Параметри інтерполяції
a = 3
b = 4
n = 10  # кількість вузлів
m = 10000  # кількість точок для побудови графіка

# Випадкові вузли інтерполяції на інтервалі [a, b]
xn = np.sort(np.random.uniform(a, b, n+1))
fn = np.log(4 + 5 * np.exp(xn))

# Ініціалізація таблиці розділених різниць
div_diff = np.zeros((n+1, n+1))
div_diff[:, 0] = fn  # перший стовпець — значення функції у вузлах

# Заповнення таблиці розділених різниць
for j in range(1, n+1):
    for i in range(n+1 - j):
        div_diff[i, j] = (div_diff[i+1, j-1] - div_diff[i, j-1]) / (xn[i+j] - xn[i])

# Функція для обчислення значень інтерполяційного многочлена Ньютона
def newton_poly(x, xn, div_diff):
    N = div_diff[0, 0]
    for j in range(1, n+1):
        term = div_diff[0, j]
        for i in range(j):
            term *= (x - xn[i])
        N += term
    return N

# Обчислення значень функції та інтерполяційного многочлена на щільній сітці xmi
xmi = np.linspace(a-1, b+1, m)
fmi = np.log(4 + 5 * np.exp(xmi))
Lmi = np.array([newton_poly(x, xn, div_diff) for x in xmi])

# Вибір контрольних точок на інтервалі [a, b]
control_points = np.random.uniform(a, b, 5)  # 5 контрольних точок
f_control = np.log(4 + 5 * np.exp(control_points))
L_control = np.array([newton_poly(x, xn, div_diff) for x in control_points])

# Обчислення похибки на контрольних точках
error = np.abs(f_control - L_control)

# Графічне представлення
plt.plot(xmi, fmi, label="f(x) - точна функція")
plt.plot(xmi, Lmi, '--', label="L_n(x) - інтерполяційний многочлен Ньютона")
plt.plot(xn, fn, 'o', label="Вузли інтерполяції")
plt.legend()
plt.show()

# Вивід результатів
#print(div_diff)
print("Контрольні точки:", control_points)
print("Значення функції в контрольних точках:", f_control)
print("Значення інтерполяційного многочлена в контрольних точках:", L_control)
print("Похибка на контрольних точках:", error)
