#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Calcolo posterior con confronto grafico
# (dati estratti dalle slide “The Birthday Problem”)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------ DATI ------------------------
mesi = [
    "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
    "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"
]

totale_nati_maschili = [1180, 963, 899, 1190, 862, 976, 1148, 906, 1147, 945, 907, 917]
n_giuseppe           = [  57,  14,  22,   20,  20,  28,   11,  10,    8,  80,  95, 100]

# prior informativo: Febbraio e Maggio favoriti
#prior = [0.06, 0.20, 0.06, 0.06, 0.20, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]

# prior non informativa
prior = [1/12] * 12


# -------------------- CALCOLI BAYES -------------------
df = pd.DataFrame(
    {
        "Totale_nati": totale_nati_maschili,
        "Giuseppe":    n_giuseppe,
        "Prior":       prior
    },
    index=mesi
)

df["Likelihood"] = df["Giuseppe"] / df["Totale_nati"]
df["Prodotto"]   = df["Likelihood"] * df["Prior"]
evidence         = df["Prodotto"].sum()
df["Posterior"]  = df["Prodotto"] / evidence

# ---------------------- OUTPUT ------------------------
print("Probabilità a posteriori (4 decimali):\n")
print(df["Posterior"].round(4).to_string())

# ------------------------ GRAFICO ---------------------
x = np.arange(len(mesi))
width = 0.25

plt.figure(figsize=(14, 6))
plt.bar(x - width, df["Prior"],      width, label="Prior")
plt.bar(x,         df["Likelihood"], width, label="Likelihood")
plt.bar(x + width, df["Posterior"],  width, label="Posterior")

plt.ylabel("Probabilità")
plt.title("Confronto fra Prior, Likelihood e Posterior")
plt.xticks(x, mesi, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
