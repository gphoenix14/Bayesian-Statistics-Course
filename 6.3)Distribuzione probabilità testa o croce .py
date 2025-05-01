import matplotlib.pyplot as plt

# Valori della variabile aleatoria y
y_values = [0, 1, 2, 3]

# Probabilità corrispondenti P(Y = y)
probabilities = [0.125, 0.375, 0.375, 0.125]

# Creazione del grafico a barre
plt.figure(figsize=(8, 5))
plt.bar(y_values, probabilities, color='skyblue', edgecolor='black')

# Etichettatura
plt.title("Distribuzione di Probabilità per Y = numero di teste in 3 lanci")
plt.xlabel("Valori di Y")
plt.ylabel("P(Y = y)")
plt.xticks(y_values)
plt.ylim(0, 0.5)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
