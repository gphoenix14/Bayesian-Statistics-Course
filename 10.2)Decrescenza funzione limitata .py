import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Funzione f(θ) = 1 / (1 + |θ|)
def f(theta):
    return 1 / (1 + np.abs(theta))

# Dominio per il grafico
theta = np.linspace(-20, 20, 1000)
y = f(theta)

# Plot della funzione
plt.figure(figsize=(10, 5))
plt.plot(theta, y, label=r'$f(\theta) = \frac{1}{1 + |\theta|}$', color='darkblue')
plt.title("Funzione non normalizzabile: decrescita troppo lenta")
plt.xlabel(r'$\theta$')
plt.ylabel(r'$f(\theta)$')
plt.grid(True)
plt.legend()
plt.show()

# Tentativo di integrazione su R
integral, error = quad(f, -np.inf, np.inf)

print(f"Integrale su ℝ: {integral} (Errore stimato: {error})")
