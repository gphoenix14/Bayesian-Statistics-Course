import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametri della distribuzione normale
mu = 0
sigma = 1
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Creazione del plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Distribuzione Normale Standard', color='black')

# Area 68%
x_fill_68 = np.linspace(mu - sigma, mu + sigma, 1000)
plt.fill_between(x_fill_68, norm.pdf(x_fill_68, mu, sigma), alpha=0.4, label='68% (~1σ)', color='skyblue')

# Area 95%
x_fill_95 = np.linspace(mu - 2*sigma, mu + 2*sigma, 1000)
plt.fill_between(x_fill_95, norm.pdf(x_fill_95, mu, sigma), alpha=0.3, label='95% (~2σ)', color='orange')

# Area 99.7%
x_fill_997 = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
plt.fill_between(x_fill_997, norm.pdf(x_fill_997, mu, sigma), alpha=0.2, label='99.7% (~3σ)', color='green')

# Aggiunta linee verticali
for i in range(-3, 4):
    plt.axvline(mu + i*sigma, color='grey', linestyle='--', linewidth=0.8)

# Dettagli del grafico
plt.title('Distribuzione Normale')
plt.xlabel('Valore')
plt.ylabel('Densità di probabilità')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
