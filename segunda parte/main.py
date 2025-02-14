import time
import csv
import os
from lector_data import DataLector
from sorting_algorithms import SortingAlgorithms
from punt_play import PuntPlay


def save_results(filename, plays, start_time, duration, end_time):
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")

        writer.writerow(["start_time", "duracion", "end_time", "game_id", "teams", "yards", "qtr", "date", "time"])

        for play in plays:
            writer.writerow(
                [f"{start_time:.4f}", f"{duration:.4f}s", f"{end_time:.4f}", play.game_id, play.teams, play.yards,
                 play.qtr, play.date, play.time])

    print(f"Resultados guardados en: {filename}")


def process_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            print(f"Procesando archivo: {file_path}")
            lector = DataLector(file_path)
            plays = lector.process_plays()

            if not plays:
                print(f"No se encontraron jugadas de despeje en {filename}.")
                continue

            print(f"Total de jugadas de despeje encontradas en {filename}: {len(plays)}\n")

            sorting_algorithms = {
                "bubble_sort": SortingAlgorithms.bubble_sort,
                "insertion_sort": SortingAlgorithms.insertion_sort,
                "merge_sort_recursive": SortingAlgorithms.merge_sort_recursive,
                "merge_sort_iterative": SortingAlgorithms.merge_sort_iterative,
                "quick_sort_recursive": SortingAlgorithms.quick_sort_recursive,
                "quick_sort_iterative": SortingAlgorithms.quick_sort_iterative
            }

            for name, sort_function in sorting_algorithms.items():
                print(f"Ejecutando {name}...")

                start_time = time.time()
                sorted_plays, duration = sort_function(plays[:])
                end_time = time.time()

                print(f"Inicio: {start_time:.4f} | Duración: {duration:.4f}s | Fin: {end_time:.4f}\n")

                result_filename = f"segunda_parte_{name}_resultado_{filename}"
                save_results(result_filename, sorted_plays, start_time, duration, end_time)


if __name__ == "__main__":
    directory = "/Users/pablogarro/data/primeraprogramada"
    process_files_in_directory(directory)
