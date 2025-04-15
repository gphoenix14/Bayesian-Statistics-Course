import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Sottoinsiemi:
# '10' = solo A = A ∩ ~B
# '01' = solo B = ~A ∩ B
# '11' = A ∩ B

venn_data = {
    '10': 65,  # A ∩ ~B: Mancini e Non Miopi
    '01': 10,  # ~A ∩ B: Destrorsi e Miopi
    '11': 5    # A ∩ B: Mancini e Miopi
}

# Crea il diagramma
plt.figure(figsize=(8, 6))
v = venn2(subsets=venn_data, set_labels=('Mancini (A)', 'Miopi (B)'))

# Etichette esplicite con probabilità
v.get_label_by_id('10').set_text('A ∩ ~B\nMancini e Non Miopi\n0.65')
v.get_label_by_id('01').set_text('\n\n~A ∩ B\nDestrorsi e Miopi\n0.10')
v.get_label_by_id('11').set_text('A ∩ B\nMancini e Miopi\n0.05')

# Aggiungiamo il valore mancante: ~A ∩ ~B (fuori da A ∪ B)
outside_value = 0.20  # Destrorsi e Non Miopi
plt.text(0.65, -0.6, '~A ∩ ~B\nDestrorsi e Non Miopi\n0.20', fontsize=11, ha='center')

# Titolo
plt.title("Diagramma di Venn - Miopi (B) e Mancini (A)", fontsize=14)
plt.tight_layout()
plt.show()
