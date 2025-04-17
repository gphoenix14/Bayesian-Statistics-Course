import matplotlib.pyplot as plt
import numpy as np

# Dati della tabella
rate_bins = ["0", "(0,1]", "(1,2]", "(2,3]", "(3,4]", "(4,5]", "(5,6]", "(6,7]", "(7,8]"]
hamilton_freq = [0, 1, 10, 11, 11, 10, 3, 1, 1]
madison_freq = [41, 7, 2, 0, 0, 0, 0, 0, 0]

x = np.arange(len(rate_bins))  # posizioni delle barre
width = 0.35  # larghezza delle barre

# Creazione del barplot
plt.figure(figsize=(10, 5))
plt.bar(x - width/2, hamilton_freq, width, label='Hamilton', color='red', edgecolor='black')
plt.bar(x + width/2, madison_freq, width, label='Madison', color='lavender', edgecolor='black')

plt.xlabel('Rate of Upon per 1000 Words')
plt.ylabel('Frequency')
plt.title("Figure 5.3 – Hamilton's and Madison's rates of 'upon'")
plt.xticks(ticks=x, labels=rate_bins)
plt.legend()
plt.tight_layout()
plt.show()
