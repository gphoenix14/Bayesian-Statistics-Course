import matplotlib.pyplot as plt

# Setup del diagramma
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Rettangolo dell’universo
rect = plt.Rectangle((1, 1), 10, 8, edgecolor='black', facecolor='none', linewidth=1.5)
ax.add_patch(rect)
ax.text(0.5, 9, 'Universo U = 100', fontsize=12, fontweight='bold')

# Cerchio per Mancini (A)
circle_A = plt.Circle((4, 5), 3, color='lightblue', alpha=0.6, ec='black')
ax.add_patch(circle_A)
ax.text(4, 5, '70', fontsize=12, ha='center', va='center')
ax.text(3.3, 8, 'Mancini (A)', fontsize=11)

# Cerchio per Miopi (B) – disgiunto da A
circle_B = plt.Circle((9, 5), 1.7, color='lightcoral', alpha=0.6, ec='black')
ax.add_patch(circle_B)
ax.text(9, 5, '15', fontsize=12, ha='center', va='center')
ax.text(8.5, 7.2, 'Miopi (B)', fontsize=11)

# Testo per ~A ∩ ~B = 15 (Destrorsi e Non Miopi)
ax.text(8.5, 2.5, 'Destrorsi e Non Miopi\n(~A ∩ ~B) = 15', fontsize=11, ha='center')

plt.title('Diagramma di Venn - Miopi (B) vs Mancini (A)', fontsize=14)
plt.tight_layout()
plt.show()
