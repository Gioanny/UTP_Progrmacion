# Constantes
UMBRAL_BAJO = 3.0
UMBRAL_MEDIO = 5.0
UMBRAL_ALTO = 7.0

# Entradas
alumno = input("Nombre del alumno: ")
equipo = input("Nombre del equipo: ")

try:
    l1 = float(input("Primera lectura (V): "))
    l2 = float(input("Segunda lectura (V): "))
except ValueError:
    print("❌ Error: Ingrese valores numéricos válidos.")
    exit()

# Cálculo del promedio
promedio = (l1 + l2) / 2

# Clasificación según el promedio
if promedio < UMBRAL_MEDIO:
    estado = "BAJO (< 5.00 V)"
else:
    estado = "ALTO (>= 5.00 V)"

# Reporte final
print("\n=== REPORTE DE SENSOR ===")
print(f"Alumno: {alumno} | Equipo: {equipo}")
print(f"Lecturas (V): {l1:.2f}, {l2:.2f} | Promedio: {promedio:.2f} V")
print(f"Estado: {estado}")
