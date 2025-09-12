import random as rd   # Importamos la librería random

# 1. Crear una lista vacía
lista = []

# 2. Llenar la lista con 10 números aleatorios entre 1 y 100
for i in range(10):
    lista.append(rd.randint(1, 100))

print("Lista original:", lista)

# 3. Obtener la longitud de la lista
n = len(lista)

# 4. Bubble Sort (ordenamiento ascendente)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            # Intercambiar posiciones
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

# 5. Imprimir resultados
print("Ascendente:", lista)
print("Descendente:", lista[::-1])  # [::-1] invierte la lista
