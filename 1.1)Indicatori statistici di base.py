# Importazione delle librerie necessarie
import numpy as np
import pandas as pd
from scipy import stats

# Impostazione del seed per garantire la riproducibilità dei risultati
np.random.seed(42)

# Generazione di un dataset di 20 numeri interi casuali tra 10 e 99
data = np.random.randint(10, 100, size=20)

# Creazione di una Serie Pandas a partire dal dataset
serie = pd.Series(data)

# Visualizzazione del dataset
print("Dataset:")
print(serie.to_list())
print("\n--- ANALISI STATISTICA ---\n")

# Calcolo della media aritmetica
# La media è la somma di tutti i valori divisa per il numero totale di valori
media = np.mean(serie)
print(f"Media: {media:.2f}")

# Calcolo della mediana
# La mediana è il valore centrale del dataset ordinato
mediana = np.median(serie)
print(f"Mediana: {mediana}")

# Calcolo della moda e della sua frequenza
# La moda è il valore che appare con maggiore frequenza nel dataset
moda_result = stats.mode(serie, keepdims=True)
moda = moda_result.mode[0]
frequenza_moda = moda_result.count[0]
print(f"Moda: {moda} (frequenza: {frequenza_moda})")

# Calcolo della varianza della popolazione
# La varianza misura la dispersione dei dati rispetto alla media
# Per la popolazione intera, si divide per N (numero totale di osservazioni)
var_pop = np.var(serie)
print(f"Varianza (popolazione): {var_pop:.2f}")

# Calcolo della varianza del campione
# Quando si lavora con un campione, si utilizza la correzione di Bessel
# Si divide per (n - 1) invece di n per ottenere uno stimatore non distorto
var_camp = np.var(serie, ddof=1)
print(f"Varianza (campione): {var_camp:.2f}")

# Calcolo della deviazione standard della popolazione
# La deviazione standard è la radice quadrata della varianza
std_pop = np.std(serie)
print(f"Deviazione standard (popolazione): {std_pop:.2f}")

# Calcolo della deviazione standard del campione
# Anche qui si applica la correzione di Bessel con ddof=1
std_camp = np.std(serie, ddof=1)
print(f"Deviazione standard (campione): {std_camp:.2f}")

# Calcolo del range
# Il range è la differenza tra il valore massimo e minimo del dataset
range_val = np.max(serie) - np.min(serie)
print(f"Range: {range_val}")

# Calcolo dei quartili e dell'IQR (Interquartile Range)
# Q1 è il 25° percentile, Q3 è il 75° percentile
# L'IQR misura la dispersione dei dati centrali
q1 = np.percentile(serie, 25)
q3 = np.percentile(serie, 75)
iqr = q3 - q1
print(f"Q1 (25° percentile): {q1}")
print(f"Q3 (75° percentile): {q3}")
print(f"IQR (Interquartile Range): {iqr}")

# Calcolo del Coefficiente di Variazione (CV)
# Il CV è il rapporto tra la deviazione standard e la media, espresso in percentuale
# Indica la variabilità relativa dei dati rispetto alla media
cv = (std_camp / media) * 100
print(f"Coefficiente di Variazione: {cv:.2f}%")
