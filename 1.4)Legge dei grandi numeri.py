import numpy as np
import matplotlib.pyplot as plt

# Funzione per simulare il lancio di una moneta e calcolare frequenza relativa
def simula_lanci(n):
    lanci = np.random.choice([0, 1], size=n)  # 0 = croce, 1 = testa
    frequenza_testa = np.cumsum(lanci) / np.arange(1, n+1)
    return frequenza_testa

# Esegui simulazioni per 5, 10, 100 e 1000 lanci
lanci_counts = [5, 10, 100, 1000]
result = {n: simula_lanci(n) for n in lanci_counts}

# Plot
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.flatten()

for i, n in enumerate(lanci_counts):
    axs[i].plot(range(1, n+1), result[n], label=f'Lanci = {n}')
    axs[i].axhline(0.5, color='red', linestyle='--', label='Probabilità teorica')
    axs[i].set_title(f'Convergenza per {n} lanci')
    axs[i].set_xlabel('Numero di lanci')
    axs[i].set_ylabel('Frequenza relativa di testa')
    axs[i].legend()
    axs[i].grid(True)

plt.tight_layout()
plt.show()
