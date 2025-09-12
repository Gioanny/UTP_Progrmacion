# Definición de constantes
UMBRAL_BAJO = 2.00
UMBRAL_MEDIO = 4.00
UMBRAL_ALTO = 5.00

# Solicitar entradas
nombre = input("Ingrese el nombre del alumno o equipo: ")
num_muestras = input("Ingrese el número de muestras/serie (entero): ")

# Intentar convertir la cantidad de muestras a entero
try:
    num_muestras = int(num_muestras)
except ValueError:
    print("❌ Error: El número de muestras debe ser un valor entero.")
    exit(1)

# Inicializar una lista para almacenar las lecturas
lecturas = []

# Solicitar las lecturas al usuario
for i in range(num_muestras):
    lectura = input(f"Ingrese la lectura {i+1} (ej. 4.5): ")
    try:
        lectura = float(lectura)
        lecturas.append(lectura)
    except ValueError:
        print(f"❌ Error: La lectura {i+1} no es un número válido.")
        exit(1)

# Calcular el promedio de las lecturas
promedio = sum(lecturas) / len(lecturas)

# Clasificar el estado según el promedio
if promedio >= UMBRAL_ALTO:
    estado = "ALTO"
elif promedio >= UMBRAL_MEDIO:
    estado = "MEDIO"
else:
    estado = "BAJO"

# Reporte final
print("\n=== REPORTE DE SENSOR ===")
print(f"Alumno/Equipo: {nombre}")
print("Lecturas (V):", ", ".join(f"{x:.2f}" for x in lecturas))
print(f"Promedio: {promedio:.2f} V")
print(f"Estado: {estado}")
