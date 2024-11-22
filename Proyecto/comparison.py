import matplotlib.pyplot as plt

# Datos experimentales simulados
tiempo = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # Tiempo en minutos
temp_centro = [35, 50, 58, 62, 64, 65, 63, 60, 56, 50, 45]  # Temperatura en el centro (°C)
temp_extremo = [35, 42, 47, 50, 52, 53, 51, 48, 45, 42, 38]  # Temperatura en el extremo (°C)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(tiempo, temp_centro, label="Centro del procesador", marker="o", linestyle="-")
plt.plot(tiempo, temp_extremo, label="Extremo del procesador", marker="s", linestyle="--")
plt.xlabel("Tiempo (min)", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)
plt.title("Evolución de la temperatura durante la carga y enfriamiento", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
