import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generiamo dati sintetici
np.random.seed(0)
n = 20
x = np.linspace(0, 10, n)
true_theta0 = 3
true_theta1 = 2
y = true_theta0 + true_theta1 * x + np.random.normal(0, 2, size=n)

# Griglia di valori di theta0 e theta1
theta0_vals = np.linspace(0, 6, 100)
theta1_vals = np.linspace(0, 4, 100)
T0, T1 = np.meshgrid(theta0_vals, theta1_vals)

# Funzione costo S(θ0, θ1)
def cost_function(t0, t1):
    preds = t0[:, None] + t1[:, None] * x  # shape (len(t1), n)
    residuals = y - preds
    return np.sum(residuals**2, axis=1)

# Calcoliamo la funzione costo su tutta la griglia
S = np.zeros_like(T0)
for i in range(T0.shape[0]):
    for j in range(T0.shape[1]):
        t0 = T0[i, j]
        t1 = T1[i, j]
        y_pred = t0 + t1 * x
        S[i, j] = np.sum((y - y_pred)**2)

# Calcolo stima OLS esplicita
X = np.column_stack((np.ones(n), x))  # colonna di 1 per intercetta
theta_hat = np.linalg.inv(X.T @ X) @ X.T @ y
theta0_hat, theta1_hat = theta_hat

# Grafico 3D della funzione costo
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(T0, T1, S, cmap='viridis', alpha=0.8)
ax.set_xlabel(r'$\theta_0$')
ax.set_ylabel(r'$\theta_1$')
ax.set_zlabel(r'$S(\theta_0, \theta_1)$')
ax.set_title('Superficie della funzione di costo OLS')

# Punto minimo (stima OLS)
ax.scatter(theta0_hat, theta1_hat, np.min(S), color='red', s=80, label=r'Minimo: $\hat{\theta}_{OLS}$')
ax.legend()

plt.tight_layout()
plt.show()
