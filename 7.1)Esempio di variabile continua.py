import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametri della distribuzione normale
mu = 0        # media
sigma = 1     # deviazione standard

# Generazione dei dati della PDF
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = norm.pdf(x, mu, sigma)

# Punto esatto da evidenziare
punto_esatto = 0
pdf_punto_esatto = norm.pdf(punto_esatto, mu, sigma)

# Intervallo da evidenziare
a, b = -1, 1
x_fill = np.linspace(a, b, 1000)
pdf_fill = norm.pdf(x_fill, mu, sigma)

# Grafico della PDF
plt.figure(figsize=(10,6))
plt.plot(x, pdf, label='PDF Distribuzione Normale')
plt.title('Variabile Casuale Continua: Distribuzione Normale')
plt.xlabel('Valore della Variabile (x)')
plt.ylabel('Densità di Probabilità (PDF)')

# Evidenzia il punto esatto
plt.vlines(punto_esatto, 0, pdf_punto_esatto, colors='r', linestyles='--', 
           label=f'Probabilità esatta in x={punto_esatto} (zero)')
plt.scatter([punto_esatto], [pdf_punto_esatto], color='red')

# Evidenzia intervallo
plt.fill_between(x_fill, pdf_fill, alpha=0.3, color='cyan', 
                 label=f'Probabilità Intervallo [{a},{b}] > 0')

# Annotazione importante
plt.annotate(f'Probabilità in x={punto_esatto} è 0',
             xy=(punto_esatto, pdf_punto_esatto), xycoords='data',
             xytext=(punto_esatto+1.5, pdf_punto_esatto+0.05),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10, color='red')

# legenda e griglia
plt.legend()
plt.grid(True)
plt.show()
