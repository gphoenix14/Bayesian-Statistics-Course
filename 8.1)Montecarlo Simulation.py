import numpy as np
import matplotlib.pyplot as plt

# Imposta la distribuzione a posteriori Beta(9,5)
a_post, b_post = 9, 5
N = 10000  # numero totale di campioni Monte Carlo

# Funzione di interesse f(θ) = θ (identità → stima della media)
f = lambda theta: theta

# Genera campioni da Beta(9,5)
samples = np.random.beta(a_post, b_post, N)

# Calcola la media cumulativa di f(θ) = θ
montecarlo_means = np.cumsum(f(samples)) / np.arange(1, N + 1)

# Calcolo teorico della media di una Beta(α, β): α / (α + β)
theoretical_mean = a_post / (a_post + b_post)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(montecarlo_means, label='Stima Monte Carlo', color='blue')
plt.axhline(theoretical_mean, color='red', linestyle='--', label='Valore teorico')
plt.xlabel('Numero di campioni Monte Carlo')
plt.ylabel('Stima di E[f(θ)]')
plt.title('Convergenza Monte Carlo della media a posteriori di θ')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
