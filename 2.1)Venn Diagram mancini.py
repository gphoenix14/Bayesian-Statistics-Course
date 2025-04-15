import matplotlib.pyplot as plt

# Creazione del diagramma di Venn semplice
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Rettangolo per rappresentare l'universo
rectangle = plt.Rectangle((1, 1), 8, 8, edgecolor='black', facecolor='none', linewidth=1.5)
ax.add_patch(rectangle)
ax.text(0.5, 9, 'Universo U = 100', fontsize=12, fontweight='bold')

# Cerchio per rappresentare l'evento A (Mancino)
circle = plt.Circle((5, 5), 3, color='lightblue', alpha=0.5)
ax.add_patch(circle)
ax.text(5, 5, 'A\nMancini\n70', fontsize=11, ha='center', va='center')

# Testo per il complementare di A (~A)
ax.text(8.3, 3, '~A\nDestri\n30', fontsize=11, ha='left', va='center')

plt.title('Diagramma di Venn ', fontsize=14)
plt.tight_layout()
plt.show()
