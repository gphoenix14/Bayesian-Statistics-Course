import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametri noti
sigma = 0.5
mu_min = 4.0
mu_max = 6.0
num_points = 1000

# Input dell'utente
x_obs = float(input("Inserisci la durata osservata (in ore, es. 4.7): "))

# Spazio delle ipotesi (mu)
mu_values = np.linspace(mu_min, mu_max, num_points)

# Prior uniforme
prior = np.ones_like(mu_values) * 0.5  # densità costante su [4,6]

# Likelihood: P(x_obs | mu) usando la pdf della normale
likelihood = norm.pdf(x_obs, loc=mu_values, scale=sigma)

# Numeratore della formula bayesiana
unnormalized_posterior = likelihood * prior

# Normalizzazione: calcolo integrale con somma discreta
posterior = unnormalized_posterior / np.trapz(unnormalized_posterior, mu_values)

# Output testuale
best_mu = mu_values[np.argmax(posterior)]
print(f"Valore di μ con massima posteriori: {best_mu:.4f} ore")

# Plot
plt.plot(mu_values, posterior, label='Posteriori P(μ|data)')
plt.xlabel("μ (media ipotizzata, in ore)")
plt.ylabel("Densità Posteriori")
plt.title(f"Distribuzione Posteriori di μ dato x = {x_obs:.1f} ore")
plt.grid(True)
plt.legend()
plt.show()
