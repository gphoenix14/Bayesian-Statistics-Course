import matplotlib.pyplot as plt
import numpy as np

# Esempio Bar Plot (variabile categoriale)
categorie = ['Very', 'Somewhat', 'Not very', 'Not at all', 'Not sure']
conteggi = [231, 196, 58, 14, 1]

plt.figure(figsize=(8, 5))
plt.bar(categorie, conteggi)
plt.title("Bar Plot - Difficoltà nel risparmiare (variabile categoriale)")
plt.xlabel("Categoria")
plt.ylabel("Frequenza")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Esempio Istogramma (variabile numerica)
# Generiamo un esempio di distribuzione di età
np.random.seed(0)
eta = np.random.normal(loc=35, scale=10, size=200)

plt.figure(figsize=(8, 5))
plt.hist(eta, bins=10, edgecolor='black')
plt.title("Istogramma - Distribuzione dell'età (variabile numerica)")
plt.xlabel("Età")
plt.ylabel("Frequenza")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
