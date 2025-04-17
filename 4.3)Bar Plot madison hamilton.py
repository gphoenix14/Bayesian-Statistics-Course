import matplotlib.pyplot as plt

# Dati delle probabilità a priori
authors = ['Hamilton', 'Madison']
prior_probabilities = [0.5, 0.5]
colors = ['red', 'lavender']

# Creazione del grafico a barre
plt.figure(figsize=(5, 4))
bars = plt.bar(authors, prior_probabilities, color=colors, edgecolor='black')
plt.ylim(0, 1)
plt.ylabel('Prior Probability')
plt.title('Prior Probability Distribution')

plt.show()
