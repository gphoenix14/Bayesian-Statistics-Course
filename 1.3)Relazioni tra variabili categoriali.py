import matplotlib.pyplot as plt
import numpy as np

# Etichette delle categorie
categorie_difficolta = ["Very", "Somewhat", "Not very", "Not at all", "Not sure"]
reddito_labels = ["< $40K", "$40K - $80K", "> $80K", "Refused"]

# Matrice dei dati (riga: fascia di reddito, colonna: livello di difficoltà)
dati = np.array([
    [128, 54, 17, 3, 0],   # < $40K
    [63, 71, 7, 6, 1],     # $40K - $80K
    [31, 61, 27, 5, 0],    # > $80K
    [9, 10, 7, 0, 0]       # Refused
])

# ----------------------
# Segmented Bar Plot
# ----------------------
percentuali = dati / dati.sum(axis=1, keepdims=True)  # Calcolo percentuali per fascia di reddito
fig, ax = plt.subplots(figsize=(10, 6))
bottom = np.zeros(len(reddito_labels))

for i, categoria in enumerate(categorie_difficolta):
    ax.bar(reddito_labels, percentuali[:, i], bottom=bottom, label=categoria)
    bottom += percentuali[:, i]

ax.set_title("Segmented Bar Plot - Difficoltà nel risparmiare per fascia di reddito")
ax.set_ylabel("Frequenza relativa")
ax.set_xlabel("Fascia di Reddito")
ax.legend(title="Difficoltà", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# ----------------------
# Mosaic Plot simulato con matplotlib
# ----------------------

# Calcolo dimensioni rettangoli per simulare mosaic plot
totale = dati.sum()
larghezze = dati.sum(axis=1) / totale  # Larghezza proporzionale ai totali per reddito

fig, ax = plt.subplots(figsize=(10, 6))
x_start = 0

for i, (label_reddito, gruppo) in enumerate(zip(reddito_labels, dati)):
    group_tot = gruppo.sum()
    altezza = gruppo / group_tot  # altezza relativa
    y_start = 0
    for j, (label_difficolta, h) in enumerate(zip(categorie_difficolta, altezza)):
        ax.bar(x=x_start, height=h, width=larghezze[i], bottom=y_start, label=label_difficolta if i == 0 else "", align='edge')
        y_start += h
    x_start += larghezze[i]

ax.set_title("Mosaic Plot Simulato - Reddito vs Difficoltà nel risparmiare")
ax.set_xticks(np.cumsum(np.insert(larghezze[:-1], 0, 0)) + np.array(larghezze) / 2)
ax.set_xticklabels(reddito_labels)
ax.set_ylabel("Frequenza relativa all'interno del gruppo")
ax.legend(title="Difficoltà", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
