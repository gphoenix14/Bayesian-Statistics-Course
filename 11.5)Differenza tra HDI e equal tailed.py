# pip install numpy matplotlib arviz

import numpy as np
import matplotlib.pyplot as plt
import arviz as az

# 1. Generazione di una distribuzione asimmetrica (posterior simulato)
np.random.seed(42)
samples = np.random.beta(a=2, b=5, size=10000)  # distribuzione asimmetrica verso destra

# 2. Calcolo Equal-Tailed Credible Interval (95%)
alpha = 0.05
lower_et, upper_et = np.percentile(samples, [100*alpha/2, 100*(1 - alpha/2)])

# 3. Calcolo HDI (95%) con ArviZ
hdi_bounds = az.hdi(samples, hdi_prob=0.95)
lower_hdi, upper_hdi = hdi_bounds[0], hdi_bounds[1]

# 4. Plot della distribuzione + intervalli
fig, ax = plt.subplots(figsize=(10, 6))

# Istogramma della distribuzione
ax.hist(samples, bins=100, density=True, alpha=0.5, color='gray', label="Posterior")

# Intervallo equal-tailed
ax.axvline(lower_et, color='blue', linestyle='--', label=f'Equal-Tailed: [{lower_et:.3f}, {upper_et:.3f}]')
ax.axvline(upper_et, color='blue', linestyle='--')

# Intervallo HDI
ax.axvline(lower_hdi, color='green', linestyle='-', label=f'HDI: [{lower_hdi:.3f}, {upper_hdi:.3f}]')
ax.axvline(upper_hdi, color='green', linestyle='-')

# Legenda e dettagli
ax.set_title("Distribuzione a posteriori simulata (Beta(2,5))", fontsize=14)
ax.set_xlabel("θ (es. parametro bayesiano)")
ax.set_ylabel("Densità")
ax.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Output testuale
print(f"\nEqual-Tailed 95% CrI = [{lower_et:.4f}, {upper_et:.4f}]")
print(f"HDI         95% CrI = [{lower_hdi:.4f}, {upper_hdi:.4f}]")
