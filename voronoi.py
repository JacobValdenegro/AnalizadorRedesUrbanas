import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Función para leer datos desde el archivo
def leer_datos(archivo):
    with open(archivo, 'r') as file:
        # Leer el número de colonias
        n = int(file.readline().strip())

        # Leer la matriz de distancias
        distancias = [list(map(int, file.readline().split())) for _ in range(n)]

        # Leer la matriz de capacidades máximas de flujo
        capacidades = [list(map(int, file.readline().split())) for _ in range(n)]

        # Leer la lista de ubicaciones de las centrales
        centrales = [tuple(map(float, coord.replace(' ', ',').strip('()\n').split(','))) for coord in file]

    return n, np.array(distancias), np.array(capacidades), centrales

# Leer datos desde el archivo
archivo_entrada = 'datos.txt'
n, distancias, capacidades, centrales = leer_datos(archivo_entrada)

# Crear una lista de puntos para las ubicaciones de las centrales
centrales_puntos = np.array(centrales)

# Calcular los polígonos de Voronoi
vor = Voronoi(centrales_puntos)

# Imprimir los puntos generados por Voronoi
print("Puntos generados por Voronoi:")
print(vor.vertices)

# Graficar los polígonos de Voronoi
voronoi_plot_2d(vor)

# Mostrar las ubicaciones de las centrales en la gráfica
plt.plot(centrales_puntos[:, 0], centrales_puntos[:, 1], 'b*')

# Configuración de la gráfica
plt.title('Diagrama de Voronoi con Centrales')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')

# Mostrar la gráfica
plt.show()
