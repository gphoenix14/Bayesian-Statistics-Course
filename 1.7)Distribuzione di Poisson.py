import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parametro della distribuzione di Poisson
lambda_val = 4

# Valori discreti da considerare
x = np.arange(0, 15)

# PMF teorica della distribuzione di Poisson
pmf_values = poisson.pmf(x, mu=lambda_val)

# Generazione di campioni per confronto empirico
samples = np.random.poisson(lambda_val, 1000)

# Creazione del plot
plt.figure(figsize=(10, 6))

# Plot della PMF teorica
plt.bar(x, pmf_values, width=0.6, label='PMF Teorica', alpha=0.7, color='orange', edgecolor='black')

# Istogramma dei campioni simulati (frequenze relative)
values, counts = np.unique(samples, return_counts=True)
plt.scatter(values, counts / len(samples), color='blue', label='Frequenza empirica', zorder=5)

# Annotazioni
plt.title('Distribuzione di Poisson (λ = 4)')
plt.xlabel('Numero di eventi (k)')
plt.ylabel('Probabilità / Frequenza relativa')
plt.xticks(x)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
