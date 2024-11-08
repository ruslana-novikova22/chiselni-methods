import numpy as np

def f(x):
    out = np.sin(2*x)/(7+np.cos(2*x))
    return out

def Fp(x):
    out = -1/2 * np.log(7+np.cos(2*x))
    return out

a = 1  # нижня границя
b = 2  # верхня границя
Ip = Fp(b) - Fp(a)
print("Точне значення інтегралу:", Ip)
n = 100
epsilon = 1e-5  # бажана точність


# Метод прямокутників
def rectangular_integration(a, b, n):
    h=(b-a)/n
    s=0
    for i in range(n):
        xi=a+i*h
        s+=f(xi+h/2)
        #ліві прямокутники
        #s+=f(xi)
        #праві прямокутники
        #s+=(xi+h)
    s*=h
    return s

# Метод трапеції
def trapezoidal_integration(a, b, n):
    h=(b-a)/n
    s=0
    for i in range(n):
        xi=a+i*h
        s+=f(xi)+f(xi+h)
    s*=h/2
    return s

# Метод Сімпсона
def simpson_integration(a, b, n):
    h=(b-a)/n
    s=0
    for i in range(n):
        xi=a+i*h
        s+=f(xi)+f(xi+h)+4*f(xi+h/2)
    s*=h/6
    return s

# Апріорна оцінка похибки методів чисельного інтегрування.
def apriori_error_estimate(n, method):
    if method == rectangular_integration:
        return (b - a) ** 2 / (2 * n) * (np.abs(np.sin(2*b)/(7+np.cos(2*b))))  # Для методу прямокутників
    elif method == trapezoidal_integration:
        return (b - a) ** 2 / (12 * n**2) * (2 * np.abs(np.sin(2*b)/(7+np.cos(2*b))))  # Для методу трапецій
    elif method == simpson_integration:
        return (b - a) ** 5 / (180 * n**4) * (np.abs(np.sin(2*b)/(7+np.cos(2*b))))  # Для методу Сімпсона
    else:
        return None

# Апостеріорні оцінки похибки з урахуванням заданої точності
def integration_with_tolerance(a, b, n, epsilon, method):
    n=1
    I1 = method(a,b,n)
    I2 = method(a,b,n*2)
    while abs(I2-I1) > epsilon/2:
        n *= 2
        I1 = method(a,b,n)
        I2 = method(a,b,n*2)
    return [I1,n]


# Підрахунок функцій
rectangular_result = rectangular_integration(a, b, n)
trapezoidal_result = trapezoidal_integration(a, b, n)
simpson_result = simpson_integration(a, b, n)

apriori_r = apriori_error_estimate(n, rectangular_integration)
apriori_t = apriori_error_estimate(n, trapezoidal_integration)
apriori_s = apriori_error_estimate(n, simpson_integration)

[Ir, nr] = integration_with_tolerance(a,b,n,epsilon, rectangular_integration)
[It, nt] = integration_with_tolerance(a,b,n,epsilon, trapezoidal_integration)
[Is, ns] = integration_with_tolerance(a,b,n,epsilon, simpson_integration)

#print("Метод прямокутників:", rectangular_result)
#print(f"Точність: {[Ir, nr]}, Апріорна похибка: {apriori_r}")
#print("Метод трапеції:", trapezoidal_result)
#print(f"Точність: {[It, nt]}, Апріорна похибка: {apriori_t}")
#print("Метод Сімпсона:", simpson_result)
#print(f"Точність: {[Is, ns]}, Апріорна похибка: {apriori_s}")

print(np.max(np.abs(Ip-rectangular_result)))
print(np.max(np.abs(Ip-trapezoidal_result)))