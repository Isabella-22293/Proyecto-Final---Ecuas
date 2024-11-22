import matplotlib.pyplot as plt

# Datos proporcionados
tiempo = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # Tiempos en minutos
temp_experimental = [35, 50, 58, 62, 64, 65, 63, 60, 56, 50, 45]  # Temperaturas experimentales (°C)
temp_simulada = [35, 48, 55, 60, 63, 65, 62, 59, 55, 50, 44]  # Temperaturas simuladas (°C)
error_relativo = [0, 4, 5.17, 3.23, 1.56, 0, 1.59, 1.67, 1.79, 0, 2.22]  # Error relativo en %

# Crear la gráfica comparativa
plt.figure(figsize=(12, 7))

# Gráfica de temperaturas
plt.subplot(2, 1, 1)  # Primera subgráfica
plt.plot(tiempo, temp_experimental, label="Experimental", marker="o", linestyle="-", color="blue")
plt.plot(tiempo, temp_simulada, label="Simulada", marker="x", linestyle="--", color="orange")
plt.xlabel("Tiempo (min)", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)
plt.title("Comparación de temperaturas experimentales y simuladas", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Gráfica de error relativo
plt.subplot(2, 1, 2)  # Segunda subgráfica
plt.plot(tiempo, error_relativo, label="Error relativo", marker="s", linestyle="-", color="red")
plt.xlabel("Tiempo (min)", fontsize=12)
plt.ylabel("Error relativo (%)", fontsize=12)
plt.title("Evolución del error relativo", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Ajustar diseño para evitar superposición
plt.tight_layout()
plt.show()
