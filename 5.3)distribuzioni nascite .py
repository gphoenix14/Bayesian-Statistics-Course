import matplotlib.pyplot as plt

# Mesi
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Nati con nome "Giuseppe" (dalla tabella convertita)
giuseppe_counts = [57, 14, 22, 20, 20, 28, 11, 10, 8, 80, 95, 100]

# Creazione del grafico
plt.figure(figsize=(12, 6))
plt.bar(months, giuseppe_counts, color='steelblue', edgecolor='black')

# Etichette e titolo
plt.xlabel("Mese di nascita")
plt.ylabel("Numero di bambini chiamati Giuseppe")
plt.title("Distribuzione mensile dei nati con il nome 'Giuseppe'")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Layout ordinato
plt.tight_layout()
plt.show()
