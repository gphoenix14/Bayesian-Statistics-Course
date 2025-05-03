import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

x = np.linspace(0, 10, 1000)
lambdas = [0.5, 1, 2]

plt.figure(figsize=(10, 6))
for lam in lambdas:
    pdf = expon.pdf(x, scale=1/lam)
    plt.plot(x, pdf, label=f"$\lambda = {lam}$")

plt.title("PDF della Distribuzione Esponenziale")
plt.xlabel("x (tempo)")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
