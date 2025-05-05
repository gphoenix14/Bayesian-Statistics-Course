import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf

# Simula una catena AR(1) con autocorrelazione
np.random.seed(0)
N = 10000
rho_true = 0.9
chain = [0.0]
for _ in range(N - 1):
    chain.append(rho_true * chain[-1] + np.random.normal())

chain = np.array(chain)
f_vals = chain  # identità: f(θ) = θ

# Autocorrelazione fino al lag 100
lags = 100
autocorrs = acf(f_vals, nlags=lags, fft=True)

# Stima dell'Effective Sample Size (ESS)
ess = N / (1 + 2 * np.sum(autocorrs[1:]))
ess = round(ess, 2)

# Grafico autocorrelazione
plt.figure(figsize=(10, 5))
plt.stem(range(lags + 1), autocorrs)  # <-- fix qui
plt.title(f'Autocorrelazione della funzione f(θ), ESS ≈ {ess}')
plt.xlabel('Lag k')
plt.ylabel(r'$\rho_k$')
plt.grid(True)
plt.tight_layout()
plt.show()
