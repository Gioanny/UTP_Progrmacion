# main.py
import csv
from datetime import datetime

RAW_FILE = "DATA/RAW/voltajes_250_sucio.csv"
PROCESSED_FILE = "DATA/PROCESSED/Temperaturas_Procesado.csv"

def limpiar_valor(valor):
    if not valor or valor.upper() == "NA":
        return None
    # Convertir comas a puntos y eliminar extras
    valor = valor.replace(",", ".").replace(" ", "")
    try:
        return float(valor)
    except:
        return None

def limpiar_timestamp(ts):
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M"):
        try:
            return datetime.strptime(ts, fmt)
        except:
            continue
    return None

def voltaje_a_temperatura(v):
    return round(18*v - 64, 2)

def main():
    filas_totales = 0
    filas_validas = 0
    descartes_ts = 0
    descartes_valor = 0
    temp_min = None
    temp_max = None
    suma_temp = 0
    alertas_totales = 0

    datos_limpios = []

    with open(RAW_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            filas_totales += 1
            ts = limpiar_timestamp(row['timestamp'])
            v = limpiar_valor(row['value'])

            if ts is None:
                descartes_ts += 1
                continue
            if v is None:
                descartes_valor += 1
                continue

            temp = voltaje_a_temperatura(v)
            alerta = "ALERTA" if temp > 40 else "OK"

            datos_limpios.append({
                "Timestamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
                "Voltaje": round(v, 6),
                "Temp_C": temp,
                "Alertas": alerta
            })

            filas_validas += 1
            suma_temp += temp
            if temp_min is None or temp < temp_min:
                temp_min = temp
            if temp_max is None or temp > temp_max:
                temp_max = temp
            if alerta == "ALERTA":
                alertas_totales += 1

    # Guardar CSV procesado
    with open(PROCESSED_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Timestamp", "Voltaje", "Temp_C", "Alertas"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for d in datos_limpios:
            writer.writerow(d)

    # KPIs
    temp_prom = round(suma_temp/filas_validas, 2) if filas_validas else 0

    print(f"Filas totales: {filas_totales}")
    print(f"Filas válidas: {filas_validas}")
    print(f"Filas descartadas por timestamp inválido: {descartes_ts}")
    print(f"Filas descartadas por valor inválido: {descartes_valor}")
    print(f"Temperatura mínima: {temp_min} °C")
    print(f"Temperatura máxima: {temp_max} °C")
    print(f"Temperatura promedio: {temp_prom} °C")
    print(f"Total de alertas: {alertas_totales}")

if __name__ == "__main__":
    main()
