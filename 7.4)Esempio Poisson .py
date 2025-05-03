import numpy as np
import matplotlib.pyplot as plt

# Parametri
lambda_rate = 4  # eventi al secondo
T = 5  # intervallo osservato in secondi

# Numero di eventi simulati
num_events = np.random.poisson(lam=lambda_rate * T)
# Tempi di arrivo generati come somma cumulativa di inter-arrival times esponenziali
arrival_times = np.cumsum(np.random.exponential(scale=1/lambda_rate, size=num_events))

# Plot
plt.eventplot(arrival_times, orientation='horizontal', colors='blue')
plt.title(f'Simulazione processo di Poisson (λ={lambda_rate}, T={T})')
plt.xlabel('Tempo')
plt.yticks([])
plt.grid(True)
plt.show()
