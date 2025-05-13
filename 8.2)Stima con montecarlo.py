import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, binom

# Parametri del problema
n = 10              # numero di lanci
y = 7               # numero di teste osservate
alpha_prior = 2     # parametri della Beta prior
beta_prior = 2

# Monte Carlo sampling dal prior
N = 100000
theta_samples = np.random.beta(alpha_prior, beta_prior, size=N)

# Calcolo delle probabilità a posteriori (non normalizzate)
likelihood = binom.pmf(y, n, theta_samples)
unnormalized_posterior = likelihood  # prior già usato per il sampling

# Normalizzazione
posterior_weights = unnormalized_posterior / np.sum(unnormalized_posterior)

# Resampling dei theta in base ai pesi posteriori
posterior_samples = np.random.choice(theta_samples, size=N, replace=True, p=posterior_weights)

# Plot della distribuzione a posteriori
x = np.linspace(0, 1, 1000)
posterior_pdf = beta.pdf(x, alpha_prior + y, beta_prior + n - y)

plt.figure(figsize=(10,6))
plt.hist(posterior_samples, bins=100, density=True, alpha=0.6, label="Posterior (Monte Carlo)")
plt.plot(x, posterior_pdf, 'r-', lw=2, label="Posterior (Beta aggiornata)")
plt.axvline(x=np.mean(posterior_samples), color='black', linestyle='--', label=f"Mean ≈ {np.mean(posterior_samples):.3f}")
plt.title("Posterior distribution of θ (probabilità di testa)")
plt.xlabel("θ")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
