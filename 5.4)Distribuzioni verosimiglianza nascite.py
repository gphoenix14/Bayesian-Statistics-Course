import matplotlib.pyplot as plt
import numpy as np

# Dati dalla tabella
months = [
    "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
    "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"
]
probabilities = [
    0.0483, 0.0145, 0.0245, 0.0168, 0.0232, 0.0287,
    0.0096, 0.0110, 0.0070, 0.0847, 0.1047, 0.1091
]

# Colori per effetto prospettico simulato
colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(months)))

# Creazione figura
plt.figure(figsize=(12, 6))

# Disegna le barre
bars = plt.bar(months, probabilities, color=colors, edgecolor='black')

# Limiti e label
plt.ylim(0, 0.12)  # Aggiustato per adattarsi ai dati
plt.ylabel('Probabilità P(Giuseppe | Mese)')
plt.xlabel('Mesi')
plt.title('Distribuzione di Probabilità di Giuseppe per Mese')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Mostra
plt.tight_layout()
plt.show()
