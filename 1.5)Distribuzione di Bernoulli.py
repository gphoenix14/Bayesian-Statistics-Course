import numpy as np
import matplotlib.pyplot as plt

p = 0.3
n = 1000
samples = np.random.binomial(n=1, p=p, size=n)

plt.hist(samples, bins=[-0.5, 0.5, 1.5], edgecolor='black', rwidth=0.8)
plt.xticks([0, 1])
plt.title('Distribuzione di Bernoulli (p=0.3)')
plt.xlabel('Esito (0=fallimento, 1=successo)')
plt.ylabel('Frequenza')
plt.grid(True)
plt.show()
