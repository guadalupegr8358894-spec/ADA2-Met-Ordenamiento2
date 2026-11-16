import time


def heapify(arr, n, i):
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if izq < n and arr[izq] > arr[mayor]:
        mayor = izq
    if der < n and arr[der] > arr[mayor]:
        mayor = der

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor)


def heap_sort(arr):
    lista = arr.copy()
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
    return lista


def main():
    print("--- MÉTODO HEAPSORT ---")
    try:
        cantidad = int(input("¿Cuántos números deseas ingresar?: "))
        numeros = [
            int(input(f"Ingresa el número {i + 1}: ")) for i in range(cantidad)
        ]

        print(f"\nLista original: {numeros}")
        inicio = time.perf_counter()
        resultado = heap_sort(numeros)
        fin = time.perf_counter()

        print(f"Lista ordenada: {resultado}")
        print(f"Tiempo de ejecución: ${(fin - inicio) * 1000:.4f}$ ms")
    except ValueError:
        print("Error: Por favor ingresa solo números enteros.")


if __name__ == "__main__":
    main()