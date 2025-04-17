import matplotlib.pyplot as plt
import numpy as np

# Etichette delle ipotesi
labels = ['Prior Distribution', 'Posterior Distribution']

# Nuovi dati:
# Prior: Hamilton 0.75, Madison 0.25
# Posterior: Hamilton 0.3103, Madison 0.6897
hamilton = [0.75, 0.3103]
madison = [0.25, 0.6897]

# Asse X
x = np.arange(len(labels))
width = 0.35

# Grafico
fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, hamilton, width, label='Hamilton', color='red')
bars2 = ax.bar(x + width/2, madison, width, label='Madison', color='lavender')

# Etichette e stile
ax.set_ylabel('Probability')
ax.set_title('Prior and Posterior Distributions (Updated Priors)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylim(0, 1.05)
ax.legend()

# Annotazioni sopra le barre
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
