import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# ---------------------------
# Impostazione delle ipotesi
# ---------------------------
hyp_labels = ['H1: p = 0.5', 'H2: p = 0.4']
prior = np.array([0.5, 0.5])        # probabilità a priori

# ---------------------------
# Dati osservati
# ---------------------------
n_lanci = 3     # lanci totali
k_teste = 2     # teste osservate

# ---------------------------
# Verosimiglianze
# ---------------------------
likelihood = np.array([
    binom.pmf(k_teste, n_lanci, 0.5),   # H1
    binom.pmf(k_teste, n_lanci, 0.4)    # H2
])

# ---------------------------
# Aggiornamento bayesiano
# ---------------------------
unnormalised_post = likelihood * prior
posterior = unnormalised_post / unnormalised_post.sum()

# ---------------------------
# Output numerico
# ---------------------------
print('--- Confronto ipotesi ---')
for lbl, p0, p1, L in zip(hyp_labels, prior, posterior, likelihood):
    print(f'{lbl:12}  prior={p0:.3f}  likelihood={L:.3f}  posterior={p1:.3f}')

# ---------------------------
# Grafico affiancato
# ---------------------------
x = np.arange(len(hyp_labels))  # posizione delle etichette
width = 0.35                    # larghezza barre

plt.figure()
plt.bar(x - width/2, prior, width, label='Prior', color='skyblue')
plt.bar(x + width/2, posterior, width, label='Posterior', color='mediumpurple')

plt.xticks(x, hyp_labels)
plt.ylim(0, 1)
plt.ylabel('Probabilità')
plt.title('Confronto: Prior vs Posterior')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
