NFL Play-by-Play Sorting Project

Descripción

Este proyecto procesa datos de jugadas de la NFL obtenidos del repositorio nflscrapRdata. Se enfoca en identificar y ordenar jugadas de despeje (punts) utilizando diferentes algoritmos de ordenamiento, considerando varios criterios de comparación.

Estructura del Proyecto

Archivos Principales

punt_play.py: Contiene la clase PuntPlay, que representa una jugada de despeje con los siguientes atributos:

ID del juego

Equipos involucrados en formato VIS @ CASA

Total de yardas ganadas

Cuarto en que ocurrió la jugada

Métodos sobrecargados para permitir comparaciones entre objetos

lector_data.py: Define la clase LectorData, que procesa los archivos de datos, filtra las jugadas de despeje sin fumbles y devuelve una lista de objetos PuntPlay.

sorting_algorithms.py: Implementa los siguientes algoritmos de ordenamiento adaptados para ordenar objetos PuntPlay:

Bubble Sort

Insertion Sort

Merge Sort (recursivo y no recursivo)

Quick Sort (recursivo y no recursivo)

Métodos modificados para contar comparaciones e intercambios (en la primera parte del proyecto)

main.py:

Coordina la lectura de archivos y ejecución de los algoritmos de ordenamiento.

Mide y muestra en pantalla los tiempos de ejecución de cada algoritmo.

Genera archivos de salida con los resultados de cada algoritmo.

Ubicación de los Archivos de Datos

Los archivos de datos deben estar en la siguiente ubicación:

Mac: \data\primeraprogramada

Windows: C:\data\primeraprogramada

⚠️ Si el programa no encuentra los archivos en esta ubicación, la nota máxima será de 75.

Segunda Parte

Implementación de una clase PlayComparator con un método compare() para ordenar jugadas bajo los siguientes criterios:

Fecha de la jugada (columna Date)

Cuarto en que ocurrió (columna qtr)

Distancia recorrida

En caso de empate en la distancia, se prioriza la jugada más temprana en el tiempo (time).

Salida del Programa

Archivos CSV con las jugadas ordenadas por cada algoritmo, nombrados como:

XXXXX-resultado.csv (para la primera parte)

XXXXX-resultado-segunda.csv (para la segunda parte)

Tiempos de ejecución de cada algoritmo mostrados en pantalla.

Estadísticas de comparaciones e intercambios en la primera parte.

Ejecución

Para ejecutar el programa:

python main.py

Asegúrese de que todos los archivos requeridos están en la ubicación correcta antes de correr el programa.

