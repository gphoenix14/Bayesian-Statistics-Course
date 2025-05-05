import numpy as np
from collections import Counter
import time

# Stati: A = 0, B = 1, C = 2
state_names = {0: 'A (Casa)', 1: 'B (Lavoro)', 2: 'C (Palestra)'}

P = np.array([
    [0.5, 0.3, 0.2],  # A → A,B,C
    [0.2, 0.6, 0.2],  # B → A,B,C
    [0.3, 0.3, 0.4]   # C → A,B,C
])

n_steps = 100
states = [0]  # Inizializzo dallo stato A

print("Simulazione della catena di Markov:")
print("-" * 50)
print(f"Stato iniziale: {state_names[states[0]]}")
print("-" * 50)

# Simulazione con log
for step in range(1, n_steps + 1):
    current = states[-1]
    next_state = np.random.choice([0, 1, 2], p=P[current])
    print(f"Passo {step:03d}: {state_names[current]} → {state_names[next_state]} "
          f"(con probabilità: {P[current, next_state]:.2f})")
    states.append(next_state)
    # time.sleep(0.05)  # opzionale per rallentare leggermente la stampa

# Frequenze empiriche finali
counts = Counter(states)
frequencies = [counts[i] / len(states) for i in range(3)]

print("\n" + "=" * 50)
print("Frequenze empiriche finali dopo 100 transizioni:")
for i in range(3):
    print(f"{state_names[i]}: {frequencies[i]:.3f}")
print("=" * 50)
