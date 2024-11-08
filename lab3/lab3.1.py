import numpy as np
import matplotlib.pyplot as plt

a = 3
b = 4
n = 10

xn = np.zeros(n+1)
fn = np.zeros(n+1)
Ln = np.zeros(n+1)

for i in range(n+1):
    xn[i] = (b+a)/2 + (b-a)/2*np.cos(np.pi*(2*i+1)/(2*(n+1)))

fn[:] = np.log(4 + 5 * np.exp(xn[:]))
plt.plot(xn, fn, 'o', label = "f(x)")

#plt.show()

for kn in range(n+1):
    S = 0
    for k in range(n+1):
        L=1
        for i in range(k):
            L *= (xn[kn] - xn[i])/(xn[k] - xn[i])
        for i in range(k+1, n+1):
            L *= (xn[kn] - xn[i])/(xn[k] - xn[i])
        L*= fn[k]
        S += L
    Ln[kn] = S

eps = np.max(np.abs(fn - Ln))

plt.plot(xn, Ln, label = "Ln(x)")
plt.legend()
plt.show()