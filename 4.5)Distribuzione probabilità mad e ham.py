import matplotlib.pyplot as plt
import numpy as np

# Etichette delle ipotesi
labels = ['Hamilton', 'Madison']

# Probabilità a priori (corrette!)
prior = [0.5, 0.5]

# Probabilità a posteriori (dopo osservazione upon = 0.996)
posterior = [0.1304, 0.8696]

# Posizione delle barre
x = np.arange(len(labels))
width = 0.35

# Creazione del grafico
fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, prior, width, label='Prior Distribution', color='red')
bars2 = ax.bar(x + width/2, posterior, width, label='Posterior Distribution', color='lightblue')

# Etichette e layout
ax.set_ylabel('Probability')
ax.set_title('Prior and Posterior Distributions')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylim(0, 1.05)
ax.legend()

# Etichette sopra le barre
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(bars1)
autolabel(bars2)

plt.tight_layout()
plt.show()
