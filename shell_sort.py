import time


def shell_sort(arr):
    lista = arr.copy()
    n = len(lista)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista


def main():
    print("--- MÉTODO SHELLSORT ---")
    try:
        cantidad = int(input("¿Cuántos números deseas ingresar?: "))
        numeros = [
            int(input(f"Ingresa el número {i + 1}: ")) for i in range(cantidad)
        ]

        print(f"\nLista original: {numeros}")
        inicio = time.perf_counter()
        resultado = shell_sort(numeros)
        fin = time.perf_counter()

        print(f"Lista ordenada: {resultado}")
        print(f"Tiempo de ejecución: ${(fin - inicio) * 1000:.4f}$ ms")
    except ValueError:
        print("Error: Por favor ingresa solo números enteros.")


if __name__ == "__main__":
    main()