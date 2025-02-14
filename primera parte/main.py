from lector_data import DataLector
from sorting_algorithms import SortingAlgorithms
import time
import csv
import os
def save_results(filename, plays, start_time, duration, end_time, comparisons, swaps, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            ["start_time", "duracion", "end_time", "comparisons", "swaps", "game_id", "teams", "yards", "qtr"])
        for play in plays:
            writer.writerow(
                [f"{start_time:.4f}", f"{duration:.4f}s", f"{end_time:.4f}", comparisons, swaps, play.game_id,
                 play.teams, play.yards, play.qtr])
    print(f"Results saved to {file_path}")


def process_files_in_directory(directory, output_dir):
    # List all CSV files in the specified directory
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
                start_time = time.time()  # Tiempo inicial
                sorted_plays, comparisons, swaps, duration = sort_function(plays[:])  # Copia de plays
                end_time = time.time()  # Tiempo final
                print(f"Inicio: {start_time:.4f} | Duración: {duration:.4f}s | Fin: {end_time:.4f}")
                print(f"Comparaciones: {comparisons} | Intercambios: {swaps}\n")
                result_filename = f"primera_parte_{name}_resultado_{filename}"
                save_results(result_filename, sorted_plays, start_time, duration, end_time, comparisons, swaps,
                             output_dir)
if __name__ == "__main__":
    directory = "/Users/pablogarro/data/primeraprogramada"
    output_dir = "/Users/pablogarro/data/resultados"
    process_files_in_directory(directory, output_dir)
