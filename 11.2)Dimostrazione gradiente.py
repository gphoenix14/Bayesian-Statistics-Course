import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ipywidgets import interact, FloatSlider

# Funzione scalare
def f(x, y):
    return x**2 + y**2

# Gradiente
def grad_f(x, y):
    return np.array([2*x, 2*y])

# Visualizzazione
def plot_grad(x0, y0):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Griglia per la superficie
    x = np.linspace(-4, 4, 50)
    y = np.linspace(-4, 4, 50)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # Superficie
    ax.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis', edgecolor='none')

    # Punto di interesse
    z0 = f(x0, y0)
    grad = grad_f(x0, y0)
    dx, dy = grad
    dz = dx*x0 + dy*y0  # Proiezione visiva

    # Vettore gradiente visualizzato come freccia
    ax.quiver(x0, y0, z0, dx, dy, 0, color='red', linewidth=2, arrow_length_ratio=0.15)

    # Punto origine e etichette
    ax.scatter(x0, y0, z0, color='black', s=50)
    ax.text(x0, y0, z0 + 2, f"∇f = ({dx:.1f}, {dy:.1f})\n|∇f| = {np.linalg.norm(grad):.2f}", color='red')

    ax.set_xlim([-4, 4])
    ax.set_ylim([-4, 4])
    ax.set_zlim([0, 35])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.set_title("Gradiente di f(x, y) = x² + y²")

    plt.tight_layout()
    plt.show()

# Slider per il punto su cui calcolare il gradiente
interact(plot_grad,
         x0=FloatSlider(min=-3.5, max=3.5, step=0.1, value=1.0, description='x₀'),
         y0=FloatSlider(min=-3.5, max=3.5, step=0.1, value=1.0, description='y₀'))
