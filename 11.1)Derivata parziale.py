import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider
from mpl_toolkits.mplot3d import Axes3D

# Funzione da visualizzare: esempio di "temperatura"
def T(x, y):
    return np.sin(x) * np.cos(y) + 0.5 * x

# Griglia per superficie 3D
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = T(X, Y)

# Derivata parziale rispetto a x
def partial_x(x_val):
    fig = plt.figure(figsize=(12, 5))

    # Plot 3D della superficie
    ax = fig.add_subplot(121, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
    ax.set_title("Superficie T(x,y)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("T")

    # Sezione per y fissato
    y_fixed = x_val
    x_line = np.linspace(-5, 5, 200)
    y_line = np.full_like(x_line, y_fixed)
    z_line = T(x_line, y_line)

    ax.plot(x_line, y_line, z_line, color='red', linewidth=3, label='T(x, y=fisso)')
    ax.legend()

    # Sezione 2D
    ax2 = fig.add_subplot(122)
    ax2.plot(x_line, z_line, label=f'y={y_fixed:.2f}', color='red')
    ax2.set_xlabel('x')
    ax2.set_ylabel('T(x, y_fixed)')
    ax2.set_title("Sezione: derivata parziale ∂T/∂x")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.show()

# Derivata parziale rispetto a y
def partial_y(y_val):
    fig = plt.figure(figsize=(12, 5))

    # Plot 3D della superficie
    ax = fig.add_subplot(121, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.7)
    ax.set_title("Superficie T(x,y)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("T")

    # Sezione per x fissato
    x_fixed = y_val
    y_line = np.linspace(-5, 5, 200)
    x_line = np.full_like(y_line, x_fixed)
    z_line = T(x_line, y_line)

    ax.plot(x_line, y_line, z_line, color='blue', linewidth=3, label='T(x=fisso, y)')
    ax.legend()

    # Sezione 2D
    ax2 = fig.add_subplot(122)
    ax2.plot(y_line, z_line, label=f'x={x_fixed:.2f}', color='blue')
    ax2.set_xlabel('y')
    ax2.set_ylabel('T(x_fixed, y)')
    ax2.set_title("Sezione: derivata parziale ∂T/∂y")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.show()

print("📈 Derivata parziale rispetto a x (y fissato):")
interact(partial_x, x_val=FloatSlider(value=0.0, min=-5.0, max=5.0, step=0.1))

print("📉 Derivata parziale rispetto a y (x fissato):")
interact(partial_y, y_val=FloatSlider(value=0.0, min=-5.0, max=5.0, step=0.1))
