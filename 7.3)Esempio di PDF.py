import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametri della normale
mu = 0
sigma = 1
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Plot della curva normale
plt.figure(figsize=(12,6))
plt.plot(x, y, color='blue', label='PDF Normale ($\mu=0$, $\sigma=1$)')

# Intervalli empirici 1σ, 2σ, 3σ
sigma_levels = [(mu-1*sigma, mu+1*sigma, '68.26%'),
                (mu-2*sigma, mu+2*sigma, '95.44%'),
                (mu-3*sigma, mu+3*sigma, '99.73%')]

colors = ['#a6cee3', '#1f78b4', '#b2df8a']
for (a, b, label), color in zip(sigma_levels, colors):
    plt.fill_between(x, y, where=(x>=a)&(x<=b), alpha=0.4, color=color, label=label)

# Linee verticali per media e sigma
for k in range(-3, 4):
    plt.axvline(mu + k*sigma, linestyle='--', color='gray', alpha=0.6)

plt.title('Distribuzione Normale e Regola 68–95–99.7')
plt.xlabel('x')
plt.ylabel('Densità di Probabilità')
plt.legend()
plt.grid(True)
plt.show()
