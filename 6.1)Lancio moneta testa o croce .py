import tkinter as tk
from PIL import Image, ImageTk
import random
from collections import Counter
import matplotlib.pyplot as plt

# Percorsi immagini
HEADS_IMAGE_PATH = "source/testa.jpg"
TAILS_IMAGE_PATH = "source/croce.jpg"

# Lista per salvare i risultati dei lanci
results = []

# Funzione per visualizzare il grafico
def mostra_grafico():
    conteggio = Counter(results)
    etichette = ['testa', 'croce']
    valori = [conteggio.get('testa', 0), conteggio.get('croce', 0)]

    plt.figure(figsize=(6, 4))
    plt.bar(etichette, valori, color=['skyblue', 'salmon'])
    plt.title("Andamento risultati")
    plt.xlabel("Risultato")
    plt.ylabel("Frequenza")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Funzione per lanciare la moneta
def flip_coin():
    result_label.config(text="")
    coin_label.config(image="")

    def animate(count=0):
        if count < 10:
            angle = (count * 36) % 360
            rotated_img = ImageTk.PhotoImage(original_image.rotate(angle))
            coin_label.config(image=rotated_img)
            coin_label.image = rotated_img
            root.after(100, animate, count + 1)
        else:
            risultato = random.choice(["testa", "croce"])
            finale_img = heads_img if risultato == "testa" else tails_img
            coin_label.config(image=finale_img)
            coin_label.image = finale_img
            result_label.config(text=risultato.upper())
            results.append(risultato)

    animate()

# GUI
root = tk.Tk()
root.title("Simulatore di Lancio Moneta")

# Caricamento immagini
original_image = Image.open(HEADS_IMAGE_PATH).resize((200, 200))
heads_img = ImageTk.PhotoImage(original_image)
tails_img = ImageTk.PhotoImage(Image.open(TAILS_IMAGE_PATH).resize((200, 200)))

# Interfaccia grafica
coin_label = tk.Label(root)
coin_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 18))
result_label.pack(pady=10)

flip_button = tk.Button(root, text="Lancia la moneta", command=flip_coin, font=("Helvetica", 14))
flip_button.pack(pady=5)

plot_button = tk.Button(root, text="Mostra grafico", command=mostra_grafico, font=("Helvetica", 12))
plot_button.pack(pady=5)

root.mainloop()
