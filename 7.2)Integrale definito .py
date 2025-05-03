import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import quad

# Parametri della distribuzione normale standard
mu = 0
sigma = 1

# Intervallo di integrazione
a, b = -1, 1

# Definizione della PDF normale standard
def pdf(x):
    return norm.pdf(x, mu, sigma)

# Calcolo dell'integrale definito (probabilità)
area, _ = quad(pdf, a, b)

# Generazione dati per il grafico
x = np.linspace(-4, 4, 1000)
y = pdf(x)

# Plot
plt.figure(figsize=(10,6))
plt.plot(x, y, label='PDF Normale Standard', color='blue')
plt.fill_between(x, y, where=((x >= a) & (x <= b)), color='cyan', alpha=0.5,
                 label=f'Area ∫f(x) dx da {a} a {b} = {area:.4f}')

plt.title('Integrale Definito su PDF: Area sotto la curva')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axvline(a, color='black', linestyle='--')
plt.axvline(b, color='black', linestyle='--')
plt.legend()
plt.grid(True)
plt.show()
