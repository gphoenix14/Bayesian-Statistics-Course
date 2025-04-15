import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import matplotlib.patches as mpatches

# Dati
venn_data = {
    '10': 2,   # A ∩ ~B
    '01': 95,  # ~A ∩ B
    '11': 8    # A ∩ B
}
outside_value = 895  # ~A ∩ ~B

# Crea la figura
plt.figure(figsize=(8, 6))
v = venn2(subsets=venn_data, set_labels=('Cancro (A)', 'Test Positivo (B)'))

# Mostra solo i numeri nei cerchi
v.get_label_by_id('10').set_text('2')
v.get_label_by_id('01').set_text('95')
v.get_label_by_id('11').set_text('8')

# Imposta trasparenza e colori per visibilità
v.get_patch_by_id('10').set_color('#ff9999')  # rosso chiaro
v.get_patch_by_id('01').set_color('#99cc99')  # verde chiaro
v.get_patch_by_id('11').set_color('#ffcc99')  # arancio chiaro

# Crea la legenda (patch colorate)
legend_labels = [
    mpatches.Patch(color='#ffcc99', label='Cancro e Test Positivo (A ∩ B)'),
    mpatches.Patch(color='#ff9999', label='Cancro e Test Negativo (A ∩ ~B)'),
    mpatches.Patch(color='#99cc99', label='Senza Cancro e Test Positivo (~A ∩ B)'),
]

plt.legend(handles=legend_labels, loc='upper right', fontsize=10)

# Mostra l'area esterna ai cerchi (~A ∩ ~B)
plt.text(0.6, -0.6, f'Senza Cancro e Test Negativo (~A ∩ ~B): {outside_value}',
         fontsize=11, ha='center')

# Titolo e layout
plt.title("Diagramma di Venn - Cancro (A) vs Test Positivo (B)", fontsize=14)
plt.tight_layout()
plt.show()
