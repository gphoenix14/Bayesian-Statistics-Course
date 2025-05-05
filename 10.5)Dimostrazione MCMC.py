import numpy as np
import matplotlib.pyplot as plt

# Densità target (non normalizzata)
def target_density(theta):
    return np.exp(-theta**4 + theta**2)

# Proposta simmetrica: Gaussiana centrata su theta corrente
def proposal(theta, sigma=1.0):
    return np.random.normal(theta, sigma)

# Metropolis-Hastings
def metropolis_hastings(init_theta, n_samples, sigma=1.0):
    samples = []
    theta = init_theta

    for _ in range(n_samples):
        theta_prime = proposal(theta, sigma)
        r = target_density(theta_prime) / target_density(theta)
        alpha = min(1, r)
        if np.random.rand() < alpha:
            theta = theta_prime
        samples.append(theta)

    return np.array(samples)

# Eseguiamo il campionamento
samples = metropolis_hastings(init_theta=0.0, n_samples=10000, sigma=1.0)

# Plot dei risultati
plt.hist(samples, bins=100, density=True, alpha=0.6, label="Campioni MH")
x = np.linspace(-3, 3, 500)
plt.plot(x, target_density(x) / np.trapz(target_density(x), x), 'r-', label="Densità target (normalizzata)")
plt.legend()
plt.title("Metropolis-Hastings Sampling")
plt.grid(True)
plt.show()
