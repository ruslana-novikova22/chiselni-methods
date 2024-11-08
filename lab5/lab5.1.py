# Точкове середньоквадратичне наближення
import numpy as np
import matplotlib.pyplot as plt

a=3
b=4
n=100
x = np.linspace(a,b,n)

def f(x):
    out = np.log(4 + 5 * np.exp(x[:]))
    return out
y = f(x)

plt.plot(x,y, linewidth = 2)

def P(x,a):
    (n,) = x.shape
    (m,) = a.shape
    out = np.zeros(n)
    for i in range (m):
        out[:] += a[i]*x[:]**i
    return out

def mk_sys(x,y,m):
    m+=1
    A = np.zeros([m,m])
    b = np.zeros(m)
    for i in range(m):
        b[i] = np.sum(x[:]**i * y[:])
        for j in range(m):
            A[i,j] = np.sum(x[:]**i*x[:]**j)
    return [A,b]

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

m=1
[m,v] = mk_sys(x,y,m)
#A = np.linalg.solve(m,v)
A= gauss_seidel_method(m,v,10**(-4), 1000)
ym = P(x,np.array(A))
plt.plot(x,ym,"--", label = 'm=1')

m=2
[m,v] = mk_sys(x,y,m)
#A = np.linalg.solve(m,v)
A= gauss_seidel_method(m,v,10**(-4), 1000)
ym = P(x,np.array(A))
plt.plot(x,ym,"--", label = 'm=2')

m=3
[m,v] = mk_sys(x,y,m)
#A = np.linalg.solve(m,v)
A= gauss_seidel_method(m,v,10**(-4), 1000)
ym = P(x,np.array(A))
plt.plot(x,ym,"--", label = 'm=3')


print(A)
plt.legend()
plt.xlim(a,b)
plt.show()