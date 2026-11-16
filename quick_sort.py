import time


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivote]
    centro = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    return quick_sort(izquierda) + centro + quick_sort(derecha)


def main():
    print("--- MÉTODO QUICKSORT ---")
    try:
        cantidad = int(input("¿Cuántos números deseas ingresar?: "))
        numeros = [
            int(input(f"Ingresa el número {i + 1}: ")) for i in range(cantidad)
        ]

        print(f"\nLista original: {numeros}")
        inicio = time.perf_counter()
        resultado = quick_sort(numeros)
        fin = time.perf_counter()

        print(f"Lista ordenada: {resultado}")
        print(f"Tiempo de ejecución: ${(fin - inicio) * 1000:.4f}$ ms")
    except ValueError:
        print("Error: Por favor ingresa solo números enteros.")


if __name__ == "__main__":
    main()