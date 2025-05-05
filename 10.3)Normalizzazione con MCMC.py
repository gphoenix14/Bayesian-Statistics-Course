import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Funzione non normalizzabile: f(θ) = 1 / (1 + |θ|)
def unnormalized_f(theta):
    return 1 / (1 + np.abs(theta))

# Dominio finito per visualizzazione e normalizzazione numerica
domain_min, domain_max = -20, 20
theta_grid = np.linspace(domain_min, domain_max, 1000)
f_vals = unnormalized_f(theta_grid)

# Calcolo dell'area SOLO sull'intervallo [-20, 20]
area_finite, _ = quad(unnormalized_f, domain_min, domain_max)
f_normalized = f_vals / area_finite  # normalizzazione SOLO su [-20,20]

# Metropolis-Hastings per campionamento
def metropolis_hastings(f, init, proposal_std, n_samples):
    chain = [init]
    current = init
    accepted = 0

    for _ in range(n_samples):
        proposal = np.random.normal(current, proposal_std)
        r = f(proposal) / f(current)
        if np.random.rand() < min(1, r):
            chain.append(proposal)
            current = proposal
            accepted += 1
        else:
            chain.append(current)
    return np.array(chain), accepted / n_samples

# Campionamento MCMC
np.random.seed(42)
samples, acc_rate = metropolis_hastings(unnormalized_f, init=0.0, proposal_std=2.0, n_samples=25000)
samples = samples[2000:]  # burn-in

# Plot
plt.figure(figsize=(12, 6))
plt.hist(samples, bins=100, range=(domain_min, domain_max), density=True, alpha=0.6,
         label='Istogramma MCMC (normalizzato)', color='skyblue')
plt.plot(theta_grid, f_normalized, 'r-', lw=2, label='f(θ) normalizzata numericamente su [-20, 20]')
plt.title(r'Confronto accurato tra $f(\theta) = \frac{1}{1 + |\theta|}$ e MCMC')
plt.xlabel(r'$\theta$')
plt.ylabel('Densità')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Output aggiuntivo
print(f"Area stimata su [-20, 20]: {area_finite:.4f}")
print(f"Rate di accettazione: {acc_rate:.3f}")
