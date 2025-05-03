import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funzione per disegnare la PDF aggiornata
def update_plot(lambda_val):
    lambda_val = float(lambda_val)
    x = np.linspace(0, 10, 1000)
    y = expon.pdf(x, scale=1/lambda_val)

    ax.clear()
    ax.plot(x, y, color='blue', label=f"$\lambda = {lambda_val:.2f}$")
    ax.fill_between(x, y, color='lightblue', alpha=0.3)
    ax.set_title("PDF della distribuzione esponenziale")
    ax.set_xlabel("x (tempo)")
    ax.set_ylabel("f(x)")
    ax.set_ylim(0, max(y)*1.2)
    ax.grid(True)
    ax.legend()
    canvas.draw()

# --- GUI TKINTER ---
root = tk.Tk()
root.title("Distribuzione Esponenziale - PDF Interattiva")

# Figura Matplotlib
fig, ax = plt.subplots(figsize=(7, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Slider per λ
slider_label = ttk.Label(root, text="λ (lambda):")
slider_label.pack()

lambda_slider = ttk.Scale(root, from_=0.1, to=5.0, value=1.0, orient='horizontal', length=400,
                          command=update_plot)
lambda_slider.pack()

# Avvio iniziale
update_plot(lambda_slider.get())

root.mainloop()
