import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Imposta seed per riproducibilità
np.random.seed(42)

# Generazione di due campioni da popolazioni normali
# Gruppo A: media 100, deviazione 15, n=50
# Gruppo B: media 110, deviazione 15, n=50

gruppo_a = np.random.normal(loc=100, scale=15, size=50)
gruppo_b = np.random.normal(loc=110, scale=15, size=50)

# Esegui il test t per campioni indipendenti (varianze uguali presupposte)
statistica, p_value = ttest_ind(gruppo_a, gruppo_b)

# Output dei risultati
print(f"Media Gruppo A: {np.mean(gruppo_a):.2f}")
print(f"Media Gruppo B: {np.mean(gruppo_b):.2f}")
print(f"Statistica t: {statistica:.4f}")
print(f"p-value: {p_value:.4f}")

# Interpretazione
alpha = 0.05
if p_value < alpha:
    print("Conclusione: Rifiutiamo l'ipotesi nulla → Le medie sono significativamente diverse.")
else:
    print("Conclusione: Non possiamo rifiutare l'ipotesi nulla → Nessuna differenza significativa tra le medie.")

# Visualizzazione dei due campioni
plt.hist(gruppo_a, bins=15, alpha=0.6, label='Gruppo A', edgecolor='black')
plt.hist(gruppo_b, bins=15, alpha=0.6, label='Gruppo B', edgecolor='black')
plt.axvline(np.mean(gruppo_a), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(np.mean(gruppo_b), color='orange', linestyle='dashed', linewidth=1)
plt.legend()
plt.title('Distribuzioni dei due gruppi')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.grid(True)
plt.tight_layout()
plt.show()
