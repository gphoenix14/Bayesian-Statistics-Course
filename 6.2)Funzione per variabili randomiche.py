import matplotlib.pyplot as plt
import numpy as np

# Funzione caotica definita su intervallo continuo
# f(x) = x * sin(x) * cos(5x) + rumore casuale
x_vals = np.linspace(-10, 10, 1000)
noise = np.random.normal(0, 1, size=len(x_vals))
y_vals = x_vals * np.sin(x_vals) * np.cos(5 * x_vals) + noise

# Plot della funzione caotica
plt.figure(figsize=(12, 6))
plt.plot(x_vals, y_vals, label='f(x) = x·sin(x)·cos(5x) + rumore', color='crimson')
plt.title("Esempio di Funzione Caotica (Pseudo-casuale)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.legend()
plt.tight_layout()
plt.show()
