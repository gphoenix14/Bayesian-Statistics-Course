import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# 1. Distribuzione target non normalizzata
def unnormalized_pi(theta):
    return np.exp(-theta**2 / 2) + 0.3 * np.exp(-(theta - 4)**2)

# 2. Metropolis-Hastings
def metropolis_hastings(pi, initial_theta, proposal_std, n_samples):
    samples = [initial_theta]
    current_theta = initial_theta
    accepted = 0

    for _ in range(n_samples):
        proposal = np.random.normal(current_theta, proposal_std)
        acceptance_ratio = pi(proposal) / pi(current_theta)
        if np.random.rand() < min(1, acceptance_ratio):
            samples.append(proposal)
            current_theta = proposal
            accepted += 1
        else:
            samples.append(current_theta)
    
    acceptance_rate = accepted / n_samples
    return np.array(samples), acceptance_rate

# 3. Parametri
np.random.seed(0)
initial = 0.0
proposal_std = 1.0
n_samples = 20000
burn_in = 2000

# 4. Esecuzione MH
samples, acc_rate = metropolis_hastings(unnormalized_pi, initial, proposal_std, n_samples)
samples = samples[burn_in:]  # rimuovi burn-in

# 5. Visualizzazione
x = np.linspace(-5, 9, 1000)
target_values = unnormalized_pi(x)
target_values /= np.trapz(target_values, x)  # normalizza numericamente per confronto

plt.figure(figsize=(12, 6))
plt.plot(x, target_values, label='Distribuzione target (normalizzata numericamente)', color='red')
plt.hist(samples, bins=100, density=True, alpha=0.6, label='Istogramma campioni MCMC', color='blue')
plt.title("Campionamento MCMC da distribuzione non normalizzabile")
plt.xlabel("θ")
plt.ylabel("Densità")
plt.legend()
plt.grid(True)
plt.show()

print(f"Rate di accettazione: {acc_rate:.3f}")
