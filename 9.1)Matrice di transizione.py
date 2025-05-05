import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Matrice di transizione
P = np.array([
    [0.6, 0.3, 0.1],  # A → A,B,C
    [0.2, 0.7, 0.1],  # B → A,B,C
    [0.3, 0.3, 0.4]   # C → A,B,C
])

stati = ['Casa', 'Lavoro', 'Palestra']
state_to_index = {name: idx for idx, name in enumerate(stati)}

# Simulazione della catena
n_steps = 50
current_state = 0  # inizio dallo stato A (Casa)
sequence = [current_state]

for _ in range(n_steps):
    current_state = np.random.choice([0, 1, 2], p=P[current_state])
    sequence.append(current_state)

# Conteggio cumulativo delle frequenze per ogni stato
sequence = np.array(sequence)
frequenze = np.array([np.cumsum(sequence == i) for i in range(3)]) / (np.arange(n_steps + 1) + 1)

# Plot delle frequenze nel tempo
plt.figure(figsize=(10, 5))
for i, stato in enumerate(stati):
    plt.plot(frequenze[i], label=stato)

plt.title('Evoluzione delle frequenze empiriche degli stati')
plt.xlabel('Tempo')
plt.ylabel('Frequenza relativa')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualizza anche la matrice di transizione
plt.figure(figsize=(6, 5))
sns.heatmap(P, annot=True, cmap='YlGnBu', xticklabels=stati, yticklabels=stati, fmt=".2f")
plt.title('Matrice di Transizione')
plt.xlabel('Stato successivo')
plt.ylabel('Stato attuale')
plt.tight_layout()
plt.show()
