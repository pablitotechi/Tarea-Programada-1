# NFL Play-by-Play Sorting Project

## Descripción

Este proyecto procesa datos de jugadas de la NFL obtenidos del repositorio `nflscrapRdata`. Se enfoca en identificar y ordenar jugadas de despeje (*punts*) utilizando diferentes algoritmos de ordenamiento.

## Estructura del Proyecto

### Archivos Principales

- **`punt_play.py`**: Contiene la clase `PuntPlay`, que representa una jugada de despeje con los siguientes atributos:
  - ID del juego
  - Equipos involucrados
  - Total de yardas ganadas
  - Cuarto en que ocurrió la jugada

- **`lector_data.py`**: Define la clase `LectorData`, que procesa los archivos de datos, filtra las jugadas de despeje sin *fumbles* y devuelve una lista de objetos `PuntPlay`.

- **`sorting_algorithms.py`**: Implementa los siguientes algoritmos de ordenamiento:
  - *Bubble Sort*
  - *Insertion Sort*
  - *Merge Sort* (recursivo y no recursivo)
  - *Quick Sort* (recursivo y no recursivo)

- **`main.py`**:
  - Coordina la lectura de archivos y ejecución de los algoritmos de ordenamiento.
  - Mide y muestra en pantalla los tiempos de ejecución de cada algoritmo.
  - Genera archivos de salida con los resultados.

## Ubicación de los Archivos de Datos

Los archivos de datos deben estar en la siguiente ubicación:

- **Mac**: `/data/primeraprogramada`
- **Windows**: `C:\data\primeraprogramada`

## Salida del Programa

- Archivos CSV con las jugadas ordenadas por cada algoritmo.
- Tiempos de ejecución de cada algoritmo mostrados en pantalla.

## Ejecución

Para ejecutar el programa:

```bash
python main.py

