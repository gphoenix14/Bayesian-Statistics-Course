import matplotlib.pyplot as plt
import numpy as np

# Etichette dei mesi
months = [
    "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
    "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"
]

# Probabilità prior e posterior
prior_probs = [
    0.06, 0.20, 0.06, 0.06, 0.20, 0.06,
    0.06, 0.06, 0.06, 0.06, 0.06, 0.06
]

posterior_probs = [
    0.0848, 0.0848, 0.0439, 0.0292, 0.1345, 0.0497,
    0.0175, 0.0205, 0.0117, 0.1491, 0.1842, 0.1901
]

# Larghezza delle barre
bar_width = 0.4
x = np.arange(len(months))

# Creazione del grafico
plt.figure(figsize=(14, 6))
plt.bar(x - bar_width/2, prior_probs, width=bar_width, label='Prior', color='red', edgecolor='black')
plt.bar(x + bar_width/2, posterior_probs, width=bar_width, label='Posterior', color='green', edgecolor='black')

# Etichette e legenda
plt.xticks(ticks=x, labels=months, rotation=45)
plt.xlabel('Mese')
plt.ylabel('Probabilità')
plt.title('Confronto tra Distribuzione Prior (rosso) e Posterior (verde)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Layout e visualizzazione
plt.tight_layout()
plt.show()
