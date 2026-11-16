import time


def counting_sort_radix(arr, exp):
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10

    for i in range(n):
        indice = (arr[i] // exp) % 10
        conteo[indice] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    i = n - 1
    while i >= 0:
        indice = (arr[i] // exp) % 10
        salida[conteo[indice] - 1] = arr[i]
        conteo[indice] -= 1
        i -= 1

    for i in range(n):
        arr[i] = salida[i]


def radix_sort(arr):
    if any(x < 0 for x in arr):
        raise ValueError("Radix Sort requiere números enteros positivos (>= 0).")
    if not arr:
        return []

    lista = arr.copy()
    max_num = max(lista)
    exp = 1
    while max_num // exp > 0:
        counting_sort_radix(lista, exp)
        exp *= 10
    return lista


def main():
    print("--- MÉTODO RADIX SORT ---")
    try:
        cantidad = int(input("¿Cuántos números deseas ingresar?: "))
        numeros = [
            int(input(f"Ingresa el número {i + 1}: ")) for i in range(cantidad)
        ]

        print(f"\nLista original: {numeros}")
        inicio = time.perf_counter()
        resultado = radix_sort(numeros)
        fin = time.perf_counter()

        print(f"Lista ordenada: {resultado}")
        print(f"Tiempo de ejecución: ${(fin - inicio) * 1000:.4f}$ ms")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()