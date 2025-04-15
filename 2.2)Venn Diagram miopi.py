import matplotlib.pyplot as plt

# Creazione del diagramma
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Rettangolo per rappresentare l'universo
rectangle = plt.Rectangle((1, 1), 8, 8, edgecolor='black', facecolor='none', linewidth=1.5)
ax.add_patch(rectangle)
ax.text(0.5, 9, 'Universo U = 100', fontsize=12, fontweight='bold')

# Cerchio per rappresentare l'evento B (Miopi) - più piccolo
circle = plt.Circle((3, 5), 1.5, color='lightcoral', alpha=0.5)
ax.add_patch(circle)
ax.text(3, 5, 'B\nMiopi\n15', fontsize=11, ha='center', va='center')

# Testo per il complementare di B (~B)
ax.text(8.3, 3, '~B\nNon miopi\n85', fontsize=11, ha='left', va='center')

plt.title('Diagramma di Venn - Miopi vs Non Miopi', fontsize=14)
plt.tight_layout()
plt.show()
