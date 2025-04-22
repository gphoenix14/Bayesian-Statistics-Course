import matplotlib.pyplot as plt
import numpy as np

# Mesi dell'anno
months = [
    "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
    "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"
]

# Probabilità posteriori corrispondenti a ciascun mese
posterior_probs = [
    0.0848, 0.0848, 0.0439, 0.0292, 0.1345, 0.0497,
    0.0175, 0.0205, 0.0117, 0.1491, 0.1842, 0.1901
]

# Colori sfumati per effetto estetico
colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(months)))

# Creazione figura
plt.figure(figsize=(12, 6))

# Disegna il grafico a barre
bars = plt.bar(months, posterior_probs, color=colors, edgecolor='black')

# Aggiungi le etichette del valore sopra ogni barra
for bar, prob in zip(bars, posterior_probs):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.005, f'{prob:.3f}', ha='center', va='bottom', fontsize=9)

# Etichette e formattazione
plt.ylabel('Probabilità P(Mese | Giuseppe)')
plt.xlabel('Mese di nascita')
plt.title('Distribuzione della Probabilità a Posteriori di Giuseppe per Mese')
plt.xticks(rotation=45)
plt.ylim(0, max(posterior_probs) + 0.03)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Layout e visualizzazione
plt.tight_layout()
plt.show()
