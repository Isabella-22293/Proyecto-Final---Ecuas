import numpy as np
import matplotlib.pyplot as plt

# Parámetros físicos
L = 0.1  # Longitud del procesador (m)
alpha = 1.2e-5  # Coeficiente de difusión térmica (m^2/s)
dx = 0.01  # Espaciado espacial (m)
dt = 0.1  # Paso temporal (s)
x = np.arange(0, L + dx, dx)
t_max = 10  # Tiempo de simulación (s)
n_steps = int(t_max / dt)

# Condiciones iniciales y de frontera
u_0 = 40  # Temperatura inicial (°C)
u_amb = 25  # Temperatura ambiente (°C)
u = np.ones(len(x)) * u_0
u[0], u[-1] = u_amb, u_amb  # Condiciones de frontera

# Simulación numérica
u_t = [u.copy()]
for _ in range(n_steps):
    u_new = u.copy()
    for i in range(1, len(x) - 1):
        u_new[i] = u[i] + alpha * dt / dx**2 * (u[i+1] - 2*u[i] + u[i-1])
    u = u_new.copy()
    u_t.append(u)

# Graficar resultados
for i in range(0, n_steps, int(n_steps / 5)):
    plt.plot(x, u_t[i], label=f"t={i * dt:.1f}s")
plt.xlabel("Posición (m)")
plt.ylabel("Temperatura (°C)")
plt.title("Evolución de la temperatura (simulación)")
plt.legend()
plt.show()
