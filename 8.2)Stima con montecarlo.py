import numpy as np

# Parametri posteriori
a_post = 9
b_post = 5
N = 10000

# Campionamento da Beta(9,5)
samples = np.random.beta(a_post, b_post, N)

# Media a posteriori
posterior_mean = np.mean(samples)

# Probabilità che theta > 0.6
prob_theta_gt_06 = np.mean(samples > 0.6)

print(f"Media a posteriori: {posterior_mean:.4f}")
print(f"P(θ > 0.6 | y): {prob_theta_gt_06:.4f}")
