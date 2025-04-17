import matplotlib.pyplot as plt
import numpy as np

# Mesi (ipotesi)
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Probabilità prior non-informativa
values = [1/12] * 12

# Colori sfumati per simulare prospettiva (più scuro a dx)
colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(months)))

# Creazione figura
plt.figure(figsize=(12, 6))

# Disegna barre con colore sfumato
bars = plt.bar(months, values, color=colors, edgecolor='black')

# Limite asse Y a 1.00
plt.ylim(0, 1.00)

# Etichette e titolo
plt.ylabel('Prior Probability')
plt.xlabel('Hypotheses (Months)')
plt.title('Figure 6.1: Prior Probability Distribution')

# Ruota le etichette
plt.xticks(rotation=45)

# Griglia leggera
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Mostra il grafico
plt.tight_layout()
plt.show()
