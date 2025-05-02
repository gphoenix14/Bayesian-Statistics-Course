import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, geom, hypergeom

# ==============================================================
# 1) Distribuzione Binomiale
#    Problema: 10 lanci di una moneta equa (p = 0.5).
#              Probabilità di ottenere esattamente 5 teste.
# ==============================================================

n_bin  = 10       # numero di lanci
p_bin  = 0.5      # moneta equa
k_bin  = np.arange(0, n_bin + 1)
pmf_bin = binom.pmf(k_bin, n_bin, p_bin)

print(f"Binomiale  P(X = 5) = {pmf_bin[5]:.4f}")

plt.figure()
plt.stem(k_bin, pmf_bin)
plt.title("Distribuzione Binomiale (n = 10, p = 0.5)")
plt.xlabel("k")
plt.ylabel("P(X = k)")
plt.grid(True)
plt.tight_layout()

# ==============================================================
# 2) Distribuzione di Poisson
#    Problema: λ = 3 arrivi medi di auto al minuto.
#              Probabilità di vedere esattamente 4 auto in 1 minuto.
# ==============================================================

lam    = 3
k_poi  = np.arange(0, 16)
pmf_poi = poisson.pmf(k_poi, lam)

print(f"Poisson    P(X = 4) = {pmf_poi[4]:.4f}")

plt.figure()
plt.stem(k_poi, pmf_poi)
plt.title("Distribuzione di Poisson (λ = 3)")
plt.xlabel("k")
plt.ylabel("P(X = k)")
plt.grid(True)
plt.tight_layout()

# ==============================================================
# 3) Distribuzione Geometrica
#    Problema: probabilità di successo p = 0.3 in un gioco.
#              Probabilità di vincere al 5° tentativo.
# ==============================================================

p_geo  = 0.3
k_geo  = np.arange(1, 16)
pmf_geo = geom.pmf(k_geo, p_geo)

print(f"Geometrica P(X = 5) = {pmf_geo[4]:.4f}")   # indice 4 corrisponde a k = 5

plt.figure()
plt.stem(k_geo, pmf_geo)
plt.title("Distribuzione Geometrica (p = 0.3)")
plt.xlabel("k")
plt.ylabel("P(X = k)")
plt.grid(True)
plt.tight_layout()

# --------------------------------------------------------------
plt.show()
