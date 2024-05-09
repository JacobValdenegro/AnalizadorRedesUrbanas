Minimum Spanning Tree (KruskalMST):

Este consistió en encontrar un árbol de expansión mínima para las colonias, conectando todas las colonias con la menor distancia posible. Este árbol representa las conexiones mínimas necesarias para conectar todas las colonias de manera eficiente. La complejidad del algoritmo de Kruskal es de O(E log V), donde E es el número de aristas y V es el número de vértices. En este caso, E es proporcional a N^2 (ya que hay conexiones entre todas las colonias) y V es el número de colonias (N).

Algoritmo del Vecino más Cercano (findShortestTSPNearestNeighbor):

El algoritmo de Nearest Neighbour se basó en encontrar una ruta de comercio viajante (TSP)
utilizando el enfoque del vecino más cercano. La ruta encontrada representa el camino más
corto que un mensajero podría tomar para visitar todas las colonias exactamente una vez y
regresar al punto de partida. La complejidad de este algoritmo es O(N^2) ya que, en el peor
de los casos, cada colonia se compara con todas las demás para encontrar la más cercana.

Algoritmo de Ford-Fulkerson Flujo Máximo (maxFlow):
Este algoritmo trata sobre encontrar el flujo máximo de información desde un nodo fuente
hasta un nodo sumidero en una red. Puede modelar el flujo de correspondencia entre las colonias como una red de flujo, donde las capacidades en las aristas representan la capacidad
de enviar correspondencia entre las colonias. Este tiene una complejidad de O(VE^2), donde
V es el número de nodos y E es el número de aristas en la red residual.
Algoritmo Genético:
Su propósito es encontrar una solución aproximada para el problema del TSP mediante la
evolución de poblaciones de soluciones candidatas. Se utiliza para buscar una ruta de
comercio viajante que sea óptima en términos de distancia. La complejidad de un algoritmo
genético depende del número de generaciones, el tamaño de la población y la complejidad de
las operaciones de selección, cruce y mutación. En este caso, se ejecuta durante un número
fijo de generaciones, por lo que la complejidad no es fácil de expresar de manera general.
Voronoi:
El código utiliza el algoritmo de Voronoi para generar polígonos basados en las ubicaciones
geográficas de las centrales. Estos polígonos ayudan a la empresa a tomar decisiones sobre la
asignación de nuevas contrataciones de servicios a las centrales más cercanas
geográficamente. La complejidad del algoritmo de Voronoi es típicamente O(n log n), donde
n es el número de centrales, dependiendo de la implementación específica de la biblioteca
utilizada.
