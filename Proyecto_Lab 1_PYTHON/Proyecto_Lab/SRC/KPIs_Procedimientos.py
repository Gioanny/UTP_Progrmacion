def calcular_kpis(datos):
    if not datos:
        return None

    temperaturas = [t[1] for t in datos]

    minimo = min(temperaturas)
    maximo = max(temperaturas)
    promedio = sum(temperaturas) / len(temperaturas)

    # Definimos "alerta" como valores > 37.5°C (ejemplo)
    alertas = sum(1 for t in temperaturas if t > 37.5)

    return {
        "temperatura_minima": minimo,
        "temperatura_maxima": maximo,
        "temperatura_promedio": promedio,
        "total_alertas": alertas
    }
def mostrar_KPIs(kpis):
    print("\n===== KPIs del procesamiento =====")
    for clave, valor in kpis.items():
        print(f"{clave}: {valor}")
    print("================================\n")
