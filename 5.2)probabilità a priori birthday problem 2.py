import matplotlib.pyplot as plt
import numpy as np

# Mesi (ipotesi)
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Probabilità prior informativa
# Diamo a Febbraio e Maggio valore 0.20 ciascuno
# Il resto dei 0.60 viene equamente distribuito tra gli altri 10 mesi (0.06 ciascuno)
values = [0.06, 0.20, 0.06, 0.06, 0.20, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]

# Controllo che somma faccia 1.00 (opzionale)
assert abs(sum(values) - 1.0) < 1e-6, "La somma delle probabilità non è 1.00"

# Colori per effetto prospettico simulato
colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(months)))

# Creazione figura
plt.figure(figsize=(12, 6))

# Disegna le barre
bars = plt.bar(months, values, color=colors, edgecolor='black')

# Limiti e label
plt.ylim(0, 1.00)
plt.ylabel('Prior Probability')
plt.xlabel('Hypotheses (Months)')
plt.title('Figure 6.2: Informative Prior Probability Distribution')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Mostra
plt.tight_layout()
plt.show()
